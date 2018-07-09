# @file miscUtils
# whatever utilities go here! sometimes for testing, sometimes for convenience!
import idaapi
import idautils

idaapi.require("IDAItems.Data")
idaapi.require("IDAItems.Function")
idaapi.require("TerminalModule")

from Definitions import Architecture, Paths

import idc
from IDAItems import Function, Data
import TerminalModule


class fix(TerminalModule.TerminalModule, object):
    def __init__(self, fmt='[+] fix (emergency room utils for your IDB)'):
        """
        This module is responsible for printing disassemblies and necessary compoents
        of disassemblies
        """
        super(fix, self).__init__(fmt)

        self.registerCommand(self, self.remFuncChunks, "remFuncChunks", "")
        self.registerCommand(self, self.replNameParen, "replNameParen", "")

    @staticmethod
    def remFuncChunks():
        """
        deletes all functions that have function chunks in them
        and appends "function_chunks_" to their names
        """
        foundProblem = False
        for seg in idautils.Segments():
            for ea in idautils.Functions(start=idc.SegStart(seg),end=idc.SegEnd(seg)):
                f = idaapi.get_func(ea)
                # chunk f
                if f.tailqty > 0:
                    foundProblem = True
                    print("Removing chunk function @ %07X" % f.startEA)
                    idaapi.del_func(f.startEA)
                    name = idc.Name(f.startEA)
                    newName = 'function_chunks_%s' % name
                    print("Renaming %s -> %s" % ((name, newName)))
                    idc.MakeName(f.startEA, newName)

        if foundProblem:
            print("Removed all function chunks!")
        else:
            print("No function chunks detected!")

    def replNameParen(self):
        """
        IDA treats the presence of a paranthesis as '_'. But visually still shows '_'.
        Just replace all of those '(' and ')'s with an actual '_'
        :return:
        """
        fixedName = False
        for ea, name in idautils.Names():
            newName = name
            if '(' in name:
                newName = newName.replace('(', '_')
            if ')' in name:
                newName = newName.replace(')', '_')

            if newName != name:
                fixedName = True
                print('%07X: Replacing %s -> %s...' % (ea, name, newName))
                idc.MakeName(ea, newName)
        if fixedName:
            print("Finished replacing all parenthesis!")
        else:
            print("No parenthesis found to fix!")

    @staticmethod
    def makeRedundantInstsData():
        """
        Some instructions, like add r0, r0, #0 can be optimized to add r0, #0 by assemblers.
        This gets in the way of disassembly. This attempts to fix that by replacing all such occurrances with
        purely their data format, and it also adds a comment on that line specifying the original inst.
        :return:
        """
        raise(NotImplemented())
