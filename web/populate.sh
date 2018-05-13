#!/bin/env bash

# create device
http --form POST http://127.0.0.1/device/ name="device1"
http --form POST http://127.0.0.1/device/ name="device2"
http --form POST http://127.0.0.1/device/ name="device3"

# create user
http --form POST http://127.0.0.1/auth/registration/ username="user1" password1="Pedaso#78000" password2="Pedaso#78000"

# associate user to device
http --form POST http://127.0.0.1/user/device device=1 owner=1


