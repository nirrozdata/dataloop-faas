import dtlpy as dl
import logging

logger = logging.getLogger(name='dtlpy')


class ServiceRunner(dl.BaseServiceRunner):
    """
    Package runner class

    """

    def __init__(self, **kwargs):
        """
        Init package attributes here

        :param kwargs: config params
        :return:
        """

    def run(self, item, item_1, progress=None):
        """
        Write your main package function here

        :param item:
        :param progress: Use this to update the progress of your package
        :return:
        """
        assert item.filename == item_1.filename, "Expected to get same item"
        return item


if __name__ == "__main__":
    """
    Run this main to locally debug your package
    """
    dl.packages.test_local_package()
