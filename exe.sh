# /usr/bin/sh

pip uninstall NONLINEAR-MODELS
rm /usr/local/lib/python2.7/dist-packages/modulesNLM -R
python setup.py install
cd bin/checks/
python launcherClusteringScan.py -d ../../dataSetsDemo/testing/vhl/dataCSV.csv -o 1 -p ../../dataSetsDemo/testing/vhl/result/ -r Clinical -k 1 -t 10 -s 100

#-t  0.9 coli -r c9
#python testModelo.py -d ../../dataSetsDemo/class/Ecoli/ecoli.csv -o 1 -p ../../dataSetsDemo/class/Ecoli/result/ -r c9 -k 1 -t 0.9 -s 100

#-t 16.9 mamo


#-t 2.9 tharo
#python testModelo.py -d ../../dataSetsDemo/class/ThoracicSurgery/ThoraricSurgery.csv -o 1 -p ../../dataSetsDemo/class/ThoracicSurgery/result/ -r c9 -k 1 -t 2.9 -s 100