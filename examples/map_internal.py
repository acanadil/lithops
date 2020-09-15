"""
Simple PyWren example using the call_async method.
to spawn an internal map execution.
"""
import lithops


def my_map_function(x):
    print("I'm activation number {}".format(id))
    return x + 7


def scheduler(total):
    iterdata = range(total)
    pw = lithops.ibm_cf_executor()
    return pw.map(my_map_function, iterdata)


if __name__ == "__main__":
    pw = lithops.ibm_cf_executor()
    pw.call_async(scheduler, 5)
    print(pw.get_result())
    pw.clean()
