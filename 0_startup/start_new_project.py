def wait_for_enter():
    input('Press [Enter] to continue... ')
    print()


def print_with_step(context: dict, msg: str):
    print(f"{context['step_no']}. {msg}")


def input_with_step(context: dict, msg: str) -> str:
    return input(f"{context['step_no']}. {msg}")


class NameProjectStep(object):
    @staticmethod
    def run(context: dict):
        context['project_name'] = input_with_step(context, "What's the name of the project? ")
        print()


class CreateGithubRepoStep(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context,
                        f"Create a new repository on Github named '{context['project_name']}'.")
        print('   - Initialize it with a README and a LICENSE')
        print('   - Copy the clone URL to the clipboard')
        wait_for_enter()


class CloneRepoStep(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, f"Clone the repo into dev/projects/{context['project_name']}.")
        wait_for_enter()


class GenerateGitignoreStep(object):
    @staticmethod
    def run(context: dict):
        print_with_step(context, 'Navigate to https://gitignore.io and generate a .gitignore')
        print(f"   - Add the file to the {context['project_name']} directory.")
        wait_for_enter()


def start_new_project():
    context = dict(step_no=1)
    steps = [
        NameProjectStep(),
        CreateGithubRepoStep(),
        CloneRepoStep(),
        GenerateGitignoreStep(),
    ]
    print(f'There are {len(steps)} steps to start a new project. Ready? Go!\n')
    for step in steps:
        step.run(context)
        context['step_no'] += 1
    print('Done!')


if __name__ == "__main__":
    start_new_project()
