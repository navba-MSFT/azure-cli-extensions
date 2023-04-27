# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

# from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):  # pylint: disable=unused-argument

    with self.command_group('stack-hci cluster'):
        from azext_stack_hci.custom import ClusterList
        self.command_table['stack-hci cluster list'] = ClusterList(loader=self)