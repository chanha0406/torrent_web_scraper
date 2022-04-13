#!/usr/bin/env sh
which virtualenv
RET=`echo $?`
echo virtualenv installed, $RET
if [ "$RET" = "1" ]
then
  sudo pip3 install virtualenv
fi

#virtualenv --python=python3.7 env
python3 -m venv env
env/bin/pip install -r requirements.txt
#cp local_config/local_machine_configuration_sample.json local_config/local_machine_configuration.json
#cp local_config/program_list_sample.py local_config/program_list.py
