from api.schemas.base import BaseSchema


class GroupSchema(BaseSchema):
    id: str
    name: str


class UserSchema(BaseSchema):
    id: str
    email: str
    groups: list[GroupSchema]


class EmailMessageSchema(BaseSchema):
    title: str
    message: str
    recipients: list[str]