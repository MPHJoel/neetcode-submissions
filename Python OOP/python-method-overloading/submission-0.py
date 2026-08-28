class TextProcessor:

    def format_text(self, *args: string) -> string:
        if len(args) == 1:
            return args[0].upper()
        concat_string = ""
        for arg in args:
            concat_string += arg
        return concat_string




# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
