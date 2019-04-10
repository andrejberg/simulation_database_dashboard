from simulation_database_dashboard.preferences import blueprint
from simulation_database_dashboard import db
from simulation_database_dashboard.base.models import Database
from flask import render_template, request, flash, current_app
import os


@blueprint.route('/')
def preferences_index():

    # if a path and comment are provided
    # add this DB to list of selectable DBs
    # try:
    #     name = request.form['db_name']
    # except:
    #     name = False
    # try:
    #     path = request.form['db_path']
    # except:
    #     path = False
    # try:
    #     comment = request.form['db_comment']
    # except:
    #     comment = ""
    #
    # if name and path:
    #     db.session.add(Database(name=name, path=path, comment=comment))
    #     db.session.commit()
    #     flash('Entry added successfully!')

    databases = db.session.query(Database).all()
    # for d in databases:
    #     if os.path.exists((d.path)):
    #         print("Hey")

    # render the template
    return render_template(
        'preferences_index.html',
        databases = databases
    )

@blueprint.route('/edit_db_table')
def edit_db_table():

    id = request.args['id']
    name = request.args['name']
    path = request.args['path']
    comment = request.args['comment']

    if id == "":
        sim_db = Database(name = name,
                          path = path,
                          comment = comment)
        db.session.add(sim_db)
    else:
        id = int(id)
        sim_db = db.session.query(Database).filter_by(id = id).first()
        sim_db.name = name
        sim_db.path = path
        sim_db.comment = comment

    db.session.commit()

    return str(sim_db.id)

@blueprint.route('/delete_db_from_table')
def delete_db_from_table():

    id = request.args.get('id')
    sim_db = db.session.query(Database).filter_by(id = id).first()
    db.session.delete(sim_db)
    db.session.commit()

    # no idea why but it has to return a sting at least (bool does not work)
    return "Done"

@blueprint.route('/select_db')
def select_db():

    id = request.args.get('id')

    if id:
        id = int(id)
        if id == current_app.config['SELECTED_DATABASE']['id']:
            current_app.config['SELECTED_DATABASE'] = { "id"   : None,
                                                        "name" : None,
                                                        "path" : None,
                                                        "comment" : None}
            return "deselected"

        else:
            sim_db = db.session.query(Database).filter_by(id = id).first()
            current_app.config['SELECTED_DATABASE'] = sim_db.__dict__
            return "selected"
    else:
        return "No database ID given."