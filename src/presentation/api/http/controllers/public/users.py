from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.post("", summary="Creates a new user")
async def create_user(): ...


@router.delete(
    "", summary="Deletes the logged user and notifies other services about this action"
)
async def delete_user(): ...


@router.post("/login", summary="Generates a new JWT pair")
async def login(): ...


@router.post("/logout", summary="Invalidates all of the JWT pairs of the logged user")
async def logout(): ...


@router.get(
    "/confirm-email/{token}",
    summary="Receives the confirmation token and marks the email as valid",
)
async def confirm_email(token: str): ...


@router.post(
    "/forgot-password",
    summary="Sends an email with instructions to change the password",
)
async def forgot_password(): ...


@router.post(
    "/reset-password/{token}",
    summary=(
        "Receives the new password together with the confirmation token and invalidates "
        "all of the previous JWT pairs"
    ),
)
async def reset_password(token: str): ...


@router.post(
    "/refresh-access-token",
    summary="Generates a new JWT access token for the logged user",
)
async def refresh_access_token(): ...


@router.post(
    "/refresh-pair",
    summary=(
        "Generates a new JWT pair for the logged user and invalidates all of the "
        "previous pairs"
    ),
)
async def refresh_pair(): ...


@router.post(
    "/change-password",
    summary=(
        "Changes the logged user's password and invalidates all of the current valid "
        "JWT pairs"
    ),
)
async def change_password(): ...
