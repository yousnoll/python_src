import unittest

from row_state import (
    RowState,
    Severity,
)

N = RowState()
C = RowState(Severity.CAUTION)
W = RowState(Severity.WARNING)
WC = RowState([Severity.CAUTION, Severity.WARNING])
E = RowState(Severity.ERROR)
EC = RowState([Severity.CAUTION, Severity.ERROR])
EW = RowState([Severity.WARNING, Severity.ERROR])
EWC = RowState([Severity.CAUTION, Severity.WARNING, Severity.ERROR])


class TestRowStatus(unittest.TestCase):
    def test_none(self):
        state = N
        self.assertEqual(len(state), 0)

        self.assertNotIn(Severity.CAUTION, state)
        self.assertNotIn(Severity.WARNING, state)
        self.assertNotIn(Severity.ERROR, state)
        
        self.assertTupleEqual(tuple(state), ())

        self.assertIsNone(state.highest_severity)

    def test_caution(self):
        state = C
        self.assertEqual(len(state), 1)

        self.assertIn(Severity.CAUTION, state)
        self.assertNotIn(Severity.WARNING, state)
        self.assertNotIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.CAUTION,))

        self.assertEqual(state.highest_severity, Severity.CAUTION)

    def test_warning(self):
        state = W
        self.assertEqual(len(state), 1)

        self.assertNotIn(Severity.CAUTION, state)
        self.assertIn(Severity.WARNING, state)
        self.assertNotIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.WARNING,))

        self.assertEqual(state.highest_severity, Severity.WARNING)

    def test_warning_caution(self):
        state = WC
        self.assertEqual(len(state), 2)

        self.assertIn(Severity.CAUTION, state)
        self.assertIn(Severity.WARNING, state)
        self.assertNotIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.WARNING, Severity.CAUTION))

        self.assertEqual(state.highest_severity, Severity.WARNING)

    def test_error(self):
        state = E
        self.assertEqual(len(state), 1)

        self.assertNotIn(Severity.CAUTION, state)
        self.assertNotIn(Severity.WARNING, state)
        self.assertIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.ERROR,))

        self.assertEqual(state.highest_severity, Severity.ERROR)

    def test_error_caution(self):
        state = EC
        self.assertEqual(len(state), 2)

        self.assertIn(Severity.CAUTION, state)
        self.assertNotIn(Severity.WARNING, state)
        self.assertIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.ERROR, Severity.CAUTION))

        self.assertEqual(state.highest_severity, Severity.ERROR)

    def test_error_warning(self):
        state = EW
        self.assertEqual(len(state), 2)

        self.assertNotIn(Severity.CAUTION, state)
        self.assertIn(Severity.WARNING, state)
        self.assertIn(Severity.ERROR, state)

        self.assertTupleEqual(tuple(state), (Severity.ERROR, Severity.WARNING))

        self.assertEqual(state.highest_severity, Severity.ERROR)

    def test_error_warning_caution(self):
        state = EWC
        self.assertEqual(len(state), 3)

        self.assertIn(Severity.CAUTION, EWC)
        self.assertIn(Severity.WARNING, EWC)
        self.assertIn(Severity.ERROR, EWC)

        self.assertTupleEqual(tuple(state), (Severity.ERROR, Severity.WARNING, Severity.CAUTION))

        self.assertEqual(state.highest_severity, Severity.ERROR)

    def test_init_duplicate(self):
        for severity in list(Severity):
            with self.subTest(severity=severity):
                state = RowState([severity, severity])
                self.assertTupleEqual(tuple(state), (severity,))

    def test_equal(self):
        n = RowState()
        c = RowState(Severity.CAUTION)
        w = RowState(Severity.WARNING)
        wc = RowState([Severity.CAUTION, Severity.WARNING])
        e = RowState(Severity.ERROR)
        ec = RowState([Severity.CAUTION, Severity.ERROR])
        ew = RowState([Severity.WARNING, Severity.ERROR])
        ewc = RowState([Severity.CAUTION, Severity.WARNING, Severity.ERROR])

        self.assertEqual(n, N)
        self.assertEqual(c, C)
        self.assertEqual(w, W)
        self.assertEqual(e, E)
        self.assertEqual(wc, WC)
        self.assertEqual(ec, EC)
        self.assertEqual(ew, EW)
        self.assertEqual(ewc, EWC)

    def test_not_equal(self):
        n = RowState()
        c = RowState(Severity.CAUTION)
        w = RowState(Severity.WARNING)
        wc = RowState([Severity.CAUTION, Severity.WARNING])
        e = RowState(Severity.ERROR)
        ec = RowState([Severity.CAUTION, Severity.ERROR])
        ew = RowState([Severity.WARNING, Severity.ERROR])
        ewc = RowState([Severity.CAUTION, Severity.WARNING, Severity.ERROR])

        self.assertNotEqual(c, N)
        self.assertNotEqual(w, N)
        self.assertNotEqual(wc, N)
        self.assertNotEqual(e, N)
        self.assertNotEqual(ec, N)
        self.assertNotEqual(ew, N)
        self.assertNotEqual(ewc, N)

        self.assertNotEqual(n, C)
        self.assertNotEqual(w, C)
        self.assertNotEqual(wc, C)
        self.assertNotEqual(e, C)
        self.assertNotEqual(ec, C)
        self.assertNotEqual(ew, C)
        self.assertNotEqual(ewc, C)

        self.assertNotEqual(n, W)
        self.assertNotEqual(c, W)
        self.assertNotEqual(wc, W)
        self.assertNotEqual(e, W)
        self.assertNotEqual(ec, W)
        self.assertNotEqual(ew, W)
        self.assertNotEqual(ewc, W)

        self.assertNotEqual(n, WC)
        self.assertNotEqual(c, WC)
        self.assertNotEqual(w, WC)
        self.assertNotEqual(e, WC)
        self.assertNotEqual(ec, WC)
        self.assertNotEqual(ew, WC)
        self.assertNotEqual(ewc, WC)

        self.assertNotEqual(n, E)
        self.assertNotEqual(c, E)
        self.assertNotEqual(w, E)
        self.assertNotEqual(wc, E)
        self.assertNotEqual(ec, E)
        self.assertNotEqual(ew, E)
        self.assertNotEqual(ewc, E)


        self.assertNotEqual(n, EC)
        self.assertNotEqual(c, EC)
        self.assertNotEqual(w, EC)
        self.assertNotEqual(wc, EC)
        self.assertNotEqual(e, EC)
        self.assertNotEqual(ew, EC)
        self.assertNotEqual(ewc, EC)

        self.assertNotEqual(n, EW)
        self.assertNotEqual(c, EW)
        self.assertNotEqual(w, EW)
        self.assertNotEqual(wc, EW)
        self.assertNotEqual(e, EW)
        self.assertNotEqual(ec, EW)
        self.assertNotEqual(ewc, EW)

        self.assertNotEqual(n, EWC)
        self.assertNotEqual(c, EWC)
        self.assertNotEqual(w, EWC)
        self.assertNotEqual(wc, EWC)
        self.assertNotEqual(e, EWC)
        self.assertNotEqual(ec, EWC)
        self.assertNotEqual(ew, EWC)

    def test_greater(self):
        self.assertGreater(C, N)
        self.assertGreater(W, N)
        self.assertGreater(WC, N)
        self.assertGreater(E, N)
        self.assertGreater(EC, N)
        self.assertGreater(EW, N)
        self.assertGreater(EWC, N)

        self.assertGreater(W, C)
        self.assertGreater(WC, C)
        self.assertGreater(E, C)
        self.assertGreater(EC, C)
        self.assertGreater(EW, C)
        self.assertGreater(EWC, C)

        self.assertGreater(E, W)
        self.assertGreater(EC, W)
        self.assertGreater(EW, W)
        self.assertGreater(EWC, W)

        self.assertGreater(E, WC)
        self.assertGreater(EC, WC)
        self.assertGreater(EW, WC)
        self.assertGreater(EWC, WC)

    def test_greater_equal(self):
        self.assertGreaterEqual(N, N)
        self.assertGreaterEqual(C, N)
        self.assertGreaterEqual(W, N)
        self.assertGreaterEqual(WC, N)
        self.assertGreaterEqual(E, N)
        self.assertGreaterEqual(EC, N)
        self.assertGreaterEqual(EW, N)
        self.assertGreaterEqual(EWC, N)

        self.assertGreaterEqual(C, C)
        self.assertGreaterEqual(W, C)
        self.assertGreaterEqual(WC, C)
        self.assertGreaterEqual(E, C)
        self.assertGreaterEqual(EC, C)
        self.assertGreaterEqual(EW, C)
        self.assertGreaterEqual(EWC, C)

        self.assertGreaterEqual(W, W)
        self.assertGreaterEqual(WC, W)
        self.assertGreaterEqual(E, W)
        self.assertGreaterEqual(EC, W)
        self.assertGreaterEqual(EW, W)
        self.assertGreaterEqual(EWC, W)

        self.assertGreaterEqual(W, WC)
        self.assertGreaterEqual(WC, WC)
        self.assertGreaterEqual(E, WC)
        self.assertGreaterEqual(EC, WC)
        self.assertGreaterEqual(EW, WC)
        self.assertGreaterEqual(EWC, WC)

        self.assertGreaterEqual(E, E)
        self.assertGreaterEqual(EC, E)
        self.assertGreaterEqual(EW, E)
        self.assertGreaterEqual(EWC, E)

        self.assertGreaterEqual(E, EC)
        self.assertGreaterEqual(EC, EC)
        self.assertGreaterEqual(EW, EC)
        self.assertGreaterEqual(EWC, EC)

        self.assertGreaterEqual(E, EW)
        self.assertGreaterEqual(EC, EW)
        self.assertGreaterEqual(EW, EW)
        self.assertGreaterEqual(EWC, EW)

        self.assertGreaterEqual(E, EWC)
        self.assertGreaterEqual(EC, EWC)
        self.assertGreaterEqual(EW, EWC)
        self.assertGreaterEqual(EWC, EWC)

    def test_lesser(self):
        self.assertLess(N, C)

        self.assertLess(N, W)
        self.assertLess(C, W)

        self.assertLess(N, E)
        self.assertLess(C, E)
        self.assertLess(W, E)
        self.assertLess(WC, E)

        self.assertLess(N, EC)
        self.assertLess(C, EC)
        self.assertLess(W, EC)
        self.assertLess(WC, EC)

        self.assertLess(N, EW)
        self.assertLess(C, EW)
        self.assertLess(W, EW)
        self.assertLess(WC, EW)

        self.assertLess(N, EWC)
        self.assertLess(C, EWC)
        self.assertLess(W, EWC)
        self.assertLess(WC, EWC)

    def test_lesser_equal(self):
        self.assertLessEqual(N, N)

        self.assertLessEqual(N, C)
        self.assertLessEqual(C, C)

        self.assertLessEqual(N, W)
        self.assertLessEqual(C, W)
        self.assertLessEqual(W, W)
        self.assertLessEqual(WC, W)

        self.assertLessEqual(N, WC)
        self.assertLessEqual(C, WC)
        self.assertLessEqual(W, WC)
        self.assertLessEqual(WC, WC)

        self.assertLessEqual(N, E)
        self.assertLessEqual(C, E)
        self.assertLessEqual(W, E)
        self.assertLessEqual(WC, E)
        self.assertLessEqual(E, E)
        self.assertLessEqual(EC, E)
        self.assertLessEqual(EW, E)
        self.assertLessEqual(EWC, E)

        self.assertLessEqual(N, EC)
        self.assertLessEqual(C, EC)
        self.assertLessEqual(W, EC)
        self.assertLessEqual(WC, EC)
        self.assertLessEqual(E, EC)
        self.assertLessEqual(EC, EC)
        self.assertLessEqual(EW, EC)
        self.assertLessEqual(EWC, EC)

        self.assertLessEqual(N, EW)
        self.assertLessEqual(C, EW)
        self.assertLessEqual(W, EW)
        self.assertLessEqual(WC, EW)
        self.assertLessEqual(E, EW)
        self.assertLessEqual(EC, EW)
        self.assertLessEqual(EW, EW)
        self.assertLessEqual(EWC, EW)

        self.assertLessEqual(N, EWC)
        self.assertLessEqual(C, EWC)
        self.assertLessEqual(W, EWC)
        self.assertLessEqual(WC, EWC)
        self.assertLessEqual(E, EWC)
        self.assertLessEqual(EC, EWC)
        self.assertLessEqual(EW, EWC)
        self.assertLessEqual(EWC, EWC)

    def test_defined(self):
        self.assertEqual(RowState.EMPTY, N)
        self.assertEqual(RowState.CAUTION, C)
        self.assertEqual(RowState.WARNING, W)
        self.assertEqual(RowState.ERROR, E)
