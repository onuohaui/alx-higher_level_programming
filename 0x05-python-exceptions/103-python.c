#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;
	const char *type;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			type = item->ob_type->tp_name;
			printf("Element %zd: %s\n", i, type);
		}
	}
	else
	{
		printf("[ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: PyObject bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		str = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

		for (i = 0; i < size && i < 10; i++)
		{
			printf(" %02x", str[i] & 0xff);
		}
		printf("\n");
	}
	else
	{
		printf("[ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: PyObject float object
 */
void print_python_float(PyObject *p)
{
	double val;

	if (PyFloat_Check(p))
	{
		val = PyFloat_AsDouble(p);
		printf("[.] float object info\n");
		printf("  value: %g\n", val);
	}
	else
	{
		printf("[ERROR] Invalid Float Object\n");
	}
}
