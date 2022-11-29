#include "lists.h"
/**
 * check_cycle - checks for cycle in a linked list
 * @list: linked list to check
 * Return: 1 if cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (list != NULL)
	{
		list = list->next;
		if (list == temp)
			return (1);
	}
	return (0);
}
