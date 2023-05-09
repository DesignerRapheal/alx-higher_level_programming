#include "lists.h"
/**
 * check_cycle - Determines whether a cycle exists in a given list
 * @list: the list to be checked
 *
 * Return: (0) if no cycle is found and (1) if a cycle is found
 */

int check_cycle(listint_t *list)
{
        listint_t *current, *check;

        if (list == NULL || list->next == NULL)
                return (0);
        current = list;
        check = current->next;

        while (current != NULL && check->next != NULL
                && check->next->next != NULL)
        {
                if (current == check)
                        return (1);
                current = current->next;
                check = check->next->next;
        }
        return (0);
}
