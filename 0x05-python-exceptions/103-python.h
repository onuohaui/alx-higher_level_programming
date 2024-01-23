#ifndef PYTHON_UTILS_H
#define PYTHON_UTILS_H

#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);
void print_python_int(PyObject *p);
void print_python_tuple(PyObject *p);

#endif /* PYTHON_UTILS_H */
