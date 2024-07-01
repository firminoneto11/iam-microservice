from fastapi import APIRouter

router = APIRouter(prefix="/users")


func = lambda: None  # noqa


router.add_api_route(
    path="",
    endpoint=func,
    methods=["POST"],
    summary="Creates a new user",
)

router.add_api_route(
    path="",
    endpoint=func,
    methods=["POST"],
    summary="Creates a new user",
)

router.post("", summary="Creates a new user")
router.post("/login", summary="Generates a new JWT pair")
router.get(
    "/confirm-email/{token}",
    summary="Receives the confirmation token and marks the email as valid",
)
router.post(
    "/forgot-password",
    summary="Sends an email with instructions to change the password",
)
router.post(
    "/forgot-password/{token}",
    summary=(
        "Receives the new password together with the confirmation token and invalidates"
        " all of the previous JWT pairs based on the current time"
    ),
)


router.post(
    "/logout",
    summary=(
        "Invalidates all of the JWT pairs of the current user based on the current time"
    ),
)

router.post(
    "/refresh-access-token",
    summary="Generates a new JWT access token for the current user",
)
router.post(
    "/refresh-pair",
    summary=(
        "Generates a new JWT pair for the current user and invalidates all of the "
        "previous pairs based on the current time"
    ),
)


router.post(
    "/change-password",
    summary=(
        "Changes the current user's password and invalidates all of the current "
        "valid JWT pairs based on the current time"
    ),
)

router.delete(
    "", summary="Deletes the current user and notifies other services about this action"
)
