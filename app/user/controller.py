from flask import request
from flask_restplus import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List

# from .schema import UserSchema
from .service import UserService
from .model import User
from .interface import UserInterface
from .schema import UserDTO

api = UserDTO.api
_user = UserDTO.user

@api.route('/')
class UserResource(Resource):
    '''Users'''

    @api.doc('list_users')
    @api.marshal_list_with(_user)
    def get(self) -> List[User]:
        '''Get all Users'''

        return UserService.get_all()

    @api.doc('create_user')
    @api.expect(_user)
    @api.marshal_with(_user, code=201)
    def post(self) -> User:
        '''Create a Single User'''
        return UserService.create(api.payload)


@api.route('/<int:userId>')
@api.param('userId', 'User database ID')
class UserIdResource(Resource):

    @api.marshal_with(_user, code=201)
    def get(self, userId: int) -> User:
        '''Get Single User'''

        return UserService.get_by_id(userId)

    def delete(self, userId: int) -> Response:
        '''Delete Single User'''
        from flask import jsonify

        id = UserService.delete_by_id(userId)
        return jsonify(dict(status='Success', id=id))

    @api.expect(_user)
    @api.marshal_with(_user, code=201)
    def put(self, userId: int) -> User:
        '''Update Single User'''

        changes: UserInterface = api.payload
        User = UserService.get_by_id(userId)
        return UserService.update(User, changes)
