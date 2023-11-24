# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/git/2G4PhasedArray/ADS_workspace/phased_array_wrk"
	lib=r"phased_array_lib"
	subst=r"phased_array_lib/FR4.subst"
	substlib=r"phased_array_lib"
	substname=r"FR4"
	cell=r"patch_v3"
	view=r"layout"
	libS3D=r"simulation/phased_array_lib/patch_v3/_3%D%Viewer/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	hpeesof_dir=r"C:\Program Files\Keysight\ADS2016_01"

	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary, hpeesof_dir=hpeesof_dir)
