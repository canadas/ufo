#!/usr/bin/env python
# test
import os
from pprint import pprint
import re

class Candidate:
	def __init__(self,line):
		candidate = re.split("\s+",line.strip())

		self.nickname = candidate[0]
		self.ra = candidate[1]
		self.dec = candidate[2]

		self.remote_f1 = "/tmp/out_" + self.nickname + "_ft1.fits"
		self.remote_f2 = "/tmp/out_" + self.nickname + "_ft2.fits"

		try:
			os.mkdir(self.nickname)
		except OSError:
			pass

		self.gen_sources()
		self.bring_sources()
		self.delete_remote_sources()
		self.create_friends()
		self.create_gtselect()
		self.create_gtmktime()
		self.create_gtexpmap()
		self.create_XML()
		self.create_gtlike()

	def gen_sources(self):
		# genera en remoto las sources (ft1 y ft2)
		# Input files: candidates
		# Input parameters: ra, dec
		remote_ft1 = self.remote_f1
		remote_ft2 = self.remote_f2

		gen_ft1 = "ssh canadas@noric.slac.stanford.edu" + \
				" /afs/slac.stanford.edu/u/gl/glast/astroserver/prod/astro " +   \
				" --output-ft1 " + remote_ft1 + \
				" --event-sample P6_public_v1 " + \
				" --minEnergy 100.0 --maxEnergy 200000.0 " + \
				" --minTimestamp 2.39557414E8 --ra " + self.ra +  \
				" --dec " + self.dec + " --radius 10.0 --eventClass 'EVENT_CLASS = 3' store" 
		gen_ft2 = "ssh canadas@noric.slac.stanford.edu" + \
				" /afs/slac.stanford.edu/u/gl/glast/astroserver/prod/astro " +   \
				" --output-ft2-30s " + remote_ft2 + \
				" --event-sample P6_public_v1 " + \
				" --minEnergy 100.0 --maxEnergy 200000.0 " + \
				" --minTimestamp 2.39557414E8 --ra " + self.ra +  \
				" --dec " + self.dec + " --radius 10.0 --eventClass 'EVENT_CLASS = 3' storeft2" 
		print gen_ft1
		print gen_ft2

	def bring_sources(self):
		# trae ft1 y ft2 a local 
		remote_ft1 = self.remote_f1
		remote_ft2 = self.remote_f2
		bring_ft1 = "scp canadas@noric.slac.stanford.edu:" + remote_ft1 + " " + self.nickname + "/ "
		bring_ft2 = "scp canadas@noric.slac.stanford.edu:" + remote_ft2 + " " + self.nickname + "/ "
		print bring_ft1
		print bring_ft2

	def delete_remote_sources(self):
		remote_ft1 = self.remote_f1
		remote_ft2 = self.remote_f2
		rm_ft1 = "ssh canadas@noric.slac.stanford.edu rm " + remote_ft1
		rm_ft2 = "ssh canadas@noric.slac.stanford.edu rm " + remote_ft2
		print rm_ft1
		print rm_ft2

	def create_friends(self):
		# ejecuta region_sources.f (necesitamos expect)
		# Input files: candidates
		# Input parameters: 
		pass

	def create_gtselect(self):
		# ejecutamos gtselect
		# Input files:
		# Input parameters:
		cmd = "gtselect infile=./" + self.nickname + "/"+ self.nickname +"-ft1.fits outfile=" + self.nickname + "-ft1_select.fits ra=" + self.ra + " dec=" + self.dec + " rad=10 tmin=239557418 tmax=272363953 emin=100 emax=200000 zmax=105 clobber=yes"
		print cmd

	def create_gtmktime(self):
		# ejecutamos gtmktime
		# Input files:
		# Input parameters:
		pass

	def create_gtexpmap(self):
		# ejecutamos gtexpmap
		# Input files:
		# Input parameters:
		pass

	def create_XML(self):
		# creamos archivo XML
		# Input files:
		# Input parameters:
		pass

	def create_gtlike(self):
		#creamos gtlike
		# Input files:
		# Input parameters:
		pass

c = open('candidates')
for line in c:
	candidate = Candidate(line)
	break
	


#Leemos ra y dec del fichero candidates, que tiene este aspecto:
#
#NickName     RA           DEC          GLON         GLAT         Test_Sta     ID_Numbe     Variabil
#  EMS0044      10.91749     34.42352    121.11111    -28.42072    163.74054          0     16.75069
#  EMS0055      12.90408    -62.71276    302.89688    -54.41553    158.67787          0      9.14921
#  etc.
#
#Luego hay que hacer un login a este pc:
#
#ssh canadas@noric.slac.stanford.edu
#passwd:*********
#
#y ejecutar el siguiente comando:
#
#/afs/slac.stanford.edu/u/gl/glast/astroserver/prod/astro \
#      --output-ft1 /tmp/out_nickname_ft1.fits \
#      --event-sample P6_public_v1 \
#      --minEnergy 100.0 --maxEnergy 200000.0 \
#      --minTimestamp 2.39557414E8 --ra 10.9174
#      --dec 34.42352 --radius 10.0 --eventClass "EVENT_CLASS = 3" store
#
#ASEGURARME DE LA EVENT CLASS, TIMESTAMP y ENERGY LIMITS.
#
#analogamente para el archivo ft2:
#
#/afs/slac.stanford.edu/u/gl/glast/astroserver/prod/astro \
#      --output-ft2-30s /tmp/out_nickname_ft2.fits \
#      --event-sample P6_public_v1 \
#      --minEnergy 100.0 --maxEnergy 200000.0 \
#      --minTimestamp 2.39557414E8 --ra 10.9174
#      --dec 34.42352 --radius 10.0 --eventClass "EVENT_CLASS = 3" store
#
#
#
#luego creamos un directorio que se llame como la fuente:
#
#mkdir EMS0044
#
#y copiamos canadas@noric.slac.stanford.edu:/tmp/out.fits a ./home/beatriz/sources/EMS0044 (for example...)
#
#
#Este proceso se repite para todas las fuentes interesantes.
#
#REFERENCIAS SOBRE LA DESCARGA DE DATOS USANDO LA LINEA DE COMANDOS EN:
#
#http://confluence.slac.stanford.edu/pages/viewpage.action?pageId=26478024
#
#LA DESCARGA DE DATOS SE PUEDE HACER TAMBIEN A TRAVES DE LA INTERFAZ WEB, 
#MUCHO MAS USER FRIENDLY: (PESTANA ASTRO SERVER EN EL DATA PORTAL)
#
#http://glast-ground.slac.stanford.edu/DataPortal/
#
#
#A continuacion pasamos al analisis.
#

