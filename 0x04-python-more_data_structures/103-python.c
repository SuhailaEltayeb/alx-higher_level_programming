#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - function to print python pytes object information
 * @p: PyBytesObject
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	unsigned char x, s;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		s = 10;
	else
		s = ((PyVarObject *)p)->ob_size + 1;
	printf(" first %d bytes: ", s);
	for (x = 0; x < s; x++)
	{
		printf("%02hhx", bytes->ob_sval[x]);
		if (x == (s - 1))
			printf("\n");
		else
			printf(" ");
	}
}
/**
 * print_python_list - function to print python list
 * @p:  PyBytesObject
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	int x, s, r;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	s = var->ob_size; /* size */
	r = list->allocated; /* reserved */

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", r);

	for (x = 0; x < s; x++)
	{
		type = list->ob_item[x]->ob_type->tp_name;
		printf("Element %d: %s\n", x, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[x]);
	}
}
