from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def investing(
    session: AsyncSession
):
    projects = await session.execute(
        select(CharityProject).where(
            ~CharityProject.fully_invested
        )
    )
    donations = await session.execute(
        select(Donation).where(
            ~Donation.fully_invested
        )
    )
    projects = projects.scalars().all()
    donations = donations.scalars().all()
    p_index = 0
    d_index = 0
    while p_index < len(projects) and d_index < len(donations):
        investment = min(
            projects[p_index].full_amount -
            projects[p_index].invested_amount,
            donations[d_index].full_amount -
            donations[d_index].invested_amount
        )
        projects[p_index].invested_amount += investment
        donations[d_index].invested_amount += investment
        if (projects[p_index].invested_amount ==
                projects[p_index].full_amount):
            setattr(projects[p_index], 'fully_invested', True)
            setattr(projects[p_index], 'close_date', datetime.now())
            p_index += 1
        if (donations[d_index].invested_amount ==
                donations[d_index].full_amount):
            setattr(donations[d_index], 'fully_invested', True)
            setattr(donations[d_index], 'close_date', datetime.now())
            d_index += 1
    session.add_all(projects + donations)
    await session.commit()
