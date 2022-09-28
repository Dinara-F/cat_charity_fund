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
    p = 0
    d = 0
    while p < len(projects) and d < len(donations):
        investment = min(
            projects[p].full_amount - projects[p].invested_amount,
            donations[d].full_amount - donations[d].invested_amount
        )
        projects[p].invested_amount += investment
        donations[d].invested_amount += investment
        if projects[p].invested_amount == projects[p].full_amount:
            setattr(projects[p], 'fully_invested', True)
            setattr(projects[p], 'close_date', datetime.now())
            p += 1
        if donations[d].invested_amount == donations[d].full_amount:
            setattr(donations[d], 'fully_invested', True)
            setattr(donations[d], 'close_date', datetime.now())
            d += 1
    session.add_all(projects + donations)
    await session.commit()
