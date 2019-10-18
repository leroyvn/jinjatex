import jinjatex


def main():
    env = jinjatex.new_env()
    template = env.get_template("resources/test.jinjatex")
    print(template.render(world="World", some_list=[s for s in "abcdefg"]))


if __name__ == "__main__":
    main()