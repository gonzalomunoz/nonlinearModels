# /usr/bin/sh

pip uninstall NONLINEAR-MODELS
rm /usr/local/lib/python2.7/dist-packages/modulesNLM -R
python setup.py install
cd bin/
python launcherClusteringScan.py -d ../dataSetsDemo/vhl/dataCSV.csv -o 1 -p ../dataSetsDemo/vhl/result/ -r Clinical -k 1 -t 10 -s 100
