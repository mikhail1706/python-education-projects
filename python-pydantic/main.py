from pydantic import BaseModel, ValidationError, Field, validator, root_validator


# class Tag(BaseModel):
#     id: int
#     tag: str


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')

    # @validator('name')
    # def name_should_be_sbp(cls, v: str) -> str:
    #     if 'spb' not in v.lower():
    #         raise ValueError("Work with SPB!")
    #     return v

    @root_validator
    def name_should_be_sbp(cls, values):
        print('values: ', values)
        return values


class UserWithoutPassword(BaseModel):
    name: str
    email: str


class User(UserWithoutPassword):
    password: str


input_json = """
{
    "city_id": "123",
    "cityFullName": "Spb"
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city.json(by_alias=True,
                    exclude={"city_id"}))
    # tag = city.tags[1]
    # print(tag.json())
    # print(tag.dict())


# "tags": [{
#     "id": 1, "tag": "capital"
# },{
#     "id": 2, "tag": "big city"
# }]