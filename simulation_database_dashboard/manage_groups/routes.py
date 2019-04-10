from simulation_database_dashboard.manage_groups import blueprint
from simulation_database_dashboard import db
from simulation_database_dashboard.base.models import Database
from flask import render_template, request, flash, current_app
import simulation_database.databaseAPI as api

@blueprint.route('/')
def manage_groups_index():

    db_path = current_app.config['SELECTED_DATABASE']['path']
    session = api.connect_database(db_path=db_path)

    # get groups for display
    groups = api.get_all_groups(session, count=True)

    group_keywords = {g : api.get_group_keywords(session, g) for g, c in groups} if groups else None

    session.close()

    return render_template(
        'manage_groups_index.html',
        groups = groups,
        group_keywords = group_keywords
    )