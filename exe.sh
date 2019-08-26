# /usr/bin/sh

pip uninstall NONLINEAR-MODELS
rm /usr/local/lib/python2.7/dist-packages/modulesNLM -R
python setup.py install
cd bin/checks/
python launcherClusteringScan.py -d ../../dataSetsDemo/testing/vhl/dataCSV.csv -o 1 -p ../../dataSetsDemo/testing/vhl/result/ -r Clinical -k 1 -t 10 -s 100
