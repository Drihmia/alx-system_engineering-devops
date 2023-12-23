#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

/**
 * infinite_while - a function that loops infinitly.
 * Return: 0 if succeeded, otherwise 0.
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
 * main - Entry to this program
 * Return: u if succeeded, otherwise 0.
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if ((pid < 0))
		{
			perror("fork");
			exit(1);
		}

		if (pid == 0)
			exit(0);

		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();

	return (0);
}

