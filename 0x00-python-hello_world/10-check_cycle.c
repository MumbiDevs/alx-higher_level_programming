#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: head of the linked list
 *
 * Description: This function checks if a given linked list contains a cycle.
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0); /* Empty list, no cycle */

	slow = list;
	fast = list->next;

	while (fast && fast->next)
	{
		if (slow == fast)
			return (1); /* Cycle detected */

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0); /* No cycle */
}
