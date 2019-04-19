from flask import Blueprint
from flask_login import login_required, current_user
from webapp.user.decorator import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route("/")
@admin_required
def admin_index():
    return 'Привет админ'
