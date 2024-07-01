from fastapi import APIRouter

router = APIRouter()


router.add_api_route(
    path="/health-check",
    endpoint=lambda: None,
    methods=["GET"],
)
