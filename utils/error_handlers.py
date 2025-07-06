from flask import jsonify

def register_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(
            message="Bad Request",
            details="The request could not be understood by the server due to malformed syntax.",
            status_code=400
        ), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
            message="Resource Not Found",
            details="The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.",
            status_code=404
        ), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify(
            message="Method Not Allowed",
            details="The method is not allowed for the requested URL.",
            status_code=405
        ), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(
            message="Internal Server Error",
            details="The server encountered an internal error and was unable to complete your request.",
            status_code=500
        ), 500

    @app.errorhandler(503)
    def service_unavailable(error):
        return jsonify(
            message="Service Unavailable",
            details="The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.",
            status_code=503
        ), 503  