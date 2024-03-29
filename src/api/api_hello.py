# coding=utf-8
import logging

from flask_restx import Resource
from werkzeug.exceptions import Unauthorized

from src.extensions.namespace import Namespace
from src.extensions.response_wrapper import wrap_response

__author__ = "QuyPN"
_logger = logging.getLogger(__name__)

ns = Namespace("hello", description="Hello operations")


@ns.route("", methods=["GET"])
class HelloApi(Resource):
    """
    Hello world api
    """

    def get(self):
        """
        Get hello message
        :return:
        """
        _logger.info("Hello world API")
        return wrap_response("Hello world", "ok", 200)


@ns.route("/ex0", methods=["GET"])
class Exception0Api(Resource):
    """
    Exception api
    """

    def get(self):
        """
        Raise ZeroDivisionError exception
        :return:
        """
        1 / 0


@ns.route("/ex1", methods=["GET"])
class Exception1Api(Resource):
    """
    Exception api
    """

    def get(self):
        """
        Raise ValueError exception
        :return:
        """
        raise ValueError("Value error exception!")


@ns.route("/ex2", methods=["GET"])
class Exception2Api(Resource):
    """
    Exception api
    """

    def get(self):
        """
        Raise Unauthorized exception
        :return:
        """
        raise Unauthorized("Login required!")
