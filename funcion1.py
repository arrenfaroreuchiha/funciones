# -*- coding: utf-8 -*-
def insertar():
    # global a, b , c
    print "mayor medio y menor"
    a = int(raw_input("numero a:"))
    b = int(raw_input("numero b:"))
    c = int(raw_input("numero c:"))
    condicional(a,b,c)

def condicional(a,b,c):
    if a < b:
        if b < c:
            print "el medio es %d el menor es %d el mayor es %d" %(b, a, c)
        elif a < c:
            print "el medio es %d el menor es %d el mayor es %d" %(c, a, b)
        else:
            print "el medio es %d el menor es %d el mayor es %d" %(a, c, b)
    elif a < c:
        print "el medio es %d" % a
        print "el menor es %d" % b
        print "el mayor es %d" % c
    elif c < b:
        print "por aca"
        print "el medio es %d" % b
        print "el menor es %d" % c
        print "el mayor es %d" % a  
    else:
        print "el medio es %d" % c
        print "el menor es %d" % b
        print "el mayor es %d" % a 

def main():
    insertar()
    # condicional()

