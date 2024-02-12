from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,insert
from database import get_async_session

from operations.models import operation
from operations.schemas import OperationCreate

from fastapi.exceptions import HTTPException
import time
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/")
async def get_specific_operations(operation_type: str,session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return {
        "status": "success",
        "data": result.all(),
        "details": None
    }

@router.post("/")
async def add_specific_operation(new_operation: OperationCreate,session: AsyncSession = Depends(get_async_session)):
    try:
        stat = insert(operation).values(**new_operation.dict())
        await session.execute(stat)
        await session.commit()
        X = 1 / 0
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details":"FUcking ErROR"
        })
    
@router.get('/long_operation')
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "sdsadasdsa,mdas,das,dasdsa,dsa,"