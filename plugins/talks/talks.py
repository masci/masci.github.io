# -*- coding: utf-8 -*-
from nikola.plugin_categories import Task
from nikola.utils import LOGGER


class Plugin(Task):

    name = "talks"

    def gen_tasks(self):

        # This function will be called when the task is executed
        def say_hi(bye):
            if bye:
                LOGGER.notice('BYE WORLD')
            else:
                LOGGER.notice('HELLO WORLD')

        # Never fail because a config key is missing.
        bye = self.site.config.get('BYE_WORLD', False)

        # Yield a task for Doit
        yield {
            'basename': 'hello_world',
            'actions': [(say_hi, [bye])],
            'uptodate': [False],
        }
