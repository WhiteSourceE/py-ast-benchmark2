from flask import Blueprint, request
import subprocess

blueprint = Blueprint("interprocedural", __name__)


def get_safe_command(req):
    return "ls"


def get_vul_command(req):
    return req.args.get('key')


@blueprint.route("/ip/safe")
def safe():
    command = get_safe_command(request)
    run = subprocess.run(command) # sink. safe input
    return str(run.returncode)


@blueprint.route("/ip/vulnerable")
def vulnerable():
    source = get_vul_command(request)
    run = subprocess.run(source) # sink. compromised input
    return str(run.returncode)
