import mymodule as testing
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.txt",
)

print(testing.foo())
logging.getLogger("mymodule").setLevel(logging.CRITICAL)
print(testing.bar())

print("test ended")
