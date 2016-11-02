#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 22:12:24 2014

@author: josh
"""

import os


def texFileText(filename):
    figure_env = ["","","","","",""]
    figure_env[0] = r"\begin{figure}[!h]"+"\n"
    figure_env[1] = r"\centering"+"\n"
    figure_env[2] = r"\includegraphics[scale=1]{{{}}}".format("../Grafiken/{}".format(filename))+"\n"
    label = r"\label{{{}}}".format("fig:"+filename.split(".")[0].lower())
    figure_env[3] = r"\caption{{{}}}".format(label)+"\n"
    figure_env[4] = r"\end{figure}"
    return "".join(["\\FloatBarrier\n"]+figure_env+["\n\\FloatBarrier"])


def makeTexFile(filename, content, overwrite=False):
    #print(filename)
    filename = "fig_{}.tex".format(filename.split(".")[0])
    #print(filename)
    #print(os.listdir(os.getcwd()+"/Grafiken/"))
    if overwrite:
        with open("Grafiken/"+filename,"w") as texfile:
            texfile.write(content)

    else:
        if not filename in os.listdir(os.getcwd()+"/Grafiken/"):
            with open("Grafiken/"+filename,"w") as texfile:
                texfile.write(content)



#print texFileText("Test.pdf")
#makeTexFile("Test.pdf",texFileText("Test.pdf"))


def main():

    print("Sollen bereits existierende Dateien überschrieben werden?J/N")
    ans = input()

    cwd = os.getcwd()
    pdf_list = []

    for File in os.listdir(cwd + "/Grafiken"):
        if File.endswith(".pdf") or File.endswith(".pdg")or File.endswith(".jpg"):
            pdf_list.append(File)

    if ans == "J" or ans =="j":
        for pdf in pdf_list:
            makeTexFile(pdf, texFileText(pdf),overwrite=True)
    elif ans == "N" or ans == "n":
        for pdf in pdf_list:
            makeTexFile(pdf, texFileText(pdf))
    print("Dateien erfolgreich erstellt!")

if __name__ == "__main__":
     main()
