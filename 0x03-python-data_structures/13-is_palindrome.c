#include "lists.h"
#include <stdlib.h>
int is_palindrome(listint_t **head)
{
	int i = 0; 
	int k = 0;
	int arr[4000];
	listint_t *temp1 = *head, *temp2 = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp1 != NULL)
	{
		arr[i] = temp1->n;
		temp1 = temp1->next;
		i++;
	}
	while (k < (i / 2) - 1)
	{
		if (temp2->n == arr[i - 1])
		{
			temp2 = temp2->next;
			i--;
			k++;
		}
		else
			return (0);
	}
	return (1);
}
