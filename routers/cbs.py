from flask import Blueprint, request
import subprocess

blueprint = Blueprint("cbs", __name__)


def execute_cb(cb):
    return cb()


def execute_cb_params(cb, *params):
    return cb(*params)


def get_const():
    return "ls"


@blueprint.route("/cb/safe")
def safe():
    command = execute_cb(get_const)
    run = subprocess.run(command)  # sink. safe input
    return str(run.returncode)


@blueprint.route("/cb/safe2")
def safe2():
    command = execute_cb_params(get_const)
    run = subprocess.run(command)  # sink. safe input
    return str(run.returncode)


@blueprint.route("/cb/safe3")
def safe3():
    command = execute_cb_params(lambda x: "ls", request)
    run = subprocess.run(command)  # sink. safe input
    return str(run.returncode)


@blueprint.route("/cb/safe4")
def safe4():
    safe_sink = lambda x: subprocess.run("ls")
    command = request.args.get("key")
    run = safe_sink(command)  # sink. safe input
    return str(run.returncode)


@blueprint.route("/cb/vulnerable")
def vulnerable():
    source = request.args.get('key')
    run = subprocess.run(source)  # sink. compromised input
    return str(run.returncode)
