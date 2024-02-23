#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - function with an infinite loop
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function to create zombie processes
 * Return: always 0
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("Error creating child process");
			exit(EXIT_FAILURE);
		}

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}

	infinite_while();

	return (0);
}
