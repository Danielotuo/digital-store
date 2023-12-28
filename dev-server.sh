#!/bin/bash
export FLASK_APP="store:create_app"
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run &
flask shell


