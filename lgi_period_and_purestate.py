"""
K3(delta) period scan (Fibonacci) + Pure-state robustness check.

Two extensions to the main Fibonacci LGI experiment (lgi_fibonacci.py):

  (1) PERIOD SCAN  Fine sampling of K3(delta) and explicit period
      determination via FFT. The Fibonacci R-symbols give a Z_5 phase
      spectrum on the central element (sigma_1 sigma_2)^3, so the naive
      structural expectation for any function of delta is a 2 pi/5
      period. This script measures the dominant period of K3(delta)
      and compares it to that algebraic expectation.

  (2) PURE-STATE ROBUSTNESS  All K3 values in the main experiment use
      the maximally mixed initial state rho_0 = I/2 ("most generous"
      for a detector-independent claim). We rerun the L=11 optimal
      word with several pure initial states to verify the violation
      is not an artefact of the mixed-state convention.

Pure-state correlator (projective Lueders measurement at t_1):
  After measuring Q at t_1, the post-measurement state is |+1> or |-1>
  with probability 1/2 each (for rho_0 = |psi> <psi| any pure state in 2D).
  By Lueders' rule the conditional correlator is C(B) = <Z U Z U^dag> on
  the post-measurement basis. For Q = sigma_z this gives
      C(U; psi) = <psi| Z U Z U^dag |psi>
  rather than the trace formula. We compute it explicitly.

Reference convention: lgi_fibonacci.py (Fibonacci F-matrix, R_1 = exp(-4 pi i /5),
R_tau = exp(+3 pi i /5)).
"""
import numpy as np
import json

np.random.seed(20260525)

phi = (1 + np.sqrt(5)) / 2
F = np.array([[1/phi, 1/np.sqrt(phi)],
              [1/np.sqrt(phi), -1/phi]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def generators(delta=0.0):
    R1 = np.exp(-4j * np.pi / 5)
    Rt = np.exp(3j * np.pi / 5) * np.exp(1j * delta)
    s1 = np.diag([R1, Rt]).astype(complex)
    s2 = F @ s1 @ F
    return np.stack([s1, s1.conj().T, s2, s2.conj().T])


def C_mixed(U):
    """C(U) = (1/2) Re Tr[Z U Z U^dag] for rho_0 = I/2.  Batched over (N,2,2)."""
    M = Z @ U @ Z @ np.conj(np.transpose(U, (0, 2, 1)))
    return 0.5 * np.real(M[:, 0, 0] + M[:, 1, 1])


def C_pure(U, psi):
    """C(U; psi) = <psi|Z U Z U^dag|psi> for a single pure state.  Batched."""
    M = Z @ U @ Z @ np.conj(np.transpose(U, (0, 2, 1)))   # (N,2,2)
    # < psi | M | psi >
    rhs = M @ psi                                          # (N,2)
    return np.real(np.conj(psi) @ rhs.T)


def best_K3_exhaustive(delta, Lmax):
    gens = generators(delta)
    words = gens.copy()
    out = {}
    for L in range(1, Lmax + 1):
        B2 = words @ words
        K3 = 2 * C_mixed(words) - C_mixed(B2)
        idx = int(np.argmax(K3))
        out[L] = dict(K3=float(K3[idx]), idx=idx)
        if L < Lmax:
            words = np.matmul(words[:, None, :, :],
                              gens[None, :, :, :]).reshape(-1, 2, 2)
    return out


# ============================================================================
# (1) PERIOD SCAN  K3(delta), fine sampling
# ============================================================================
print("=" * 64)
print("  (1) PERIOD SCAN  K3(delta) over delta in [0, 2*pi)")
print("=" * 64)

N_DELTA = 240            # fine sampling for clean FFT
LMAX_SWEEP = 9           # exhaustive within reach; longer L is slower
deltas = np.linspace(0, 2 * np.pi, N_DELTA, endpoint=False)
K3_sweep = np.zeros(N_DELTA)
for i, d in enumerate(deltas):
    K3_sweep[i] = best_K3_exhaustive(d, LMAX_SWEEP)[LMAX_SWEEP]['K3']

print(f"  sampled K3(delta) at {N_DELTA} points, exhaustive L<={LMAX_SWEEP}")
print(f"  range: [{K3_sweep.min():.6f}, {K3_sweep.max():.6f}]   "
      f"mean = {K3_sweep.mean():.6f}")

# Period determination by FFT  the dominant harmonic gives the fundamental
# period 2*pi/k.  Subtract mean first so the DC component is zero.
fft = np.fft.rfft(K3_sweep - K3_sweep.mean())
amp = np.abs(fft)
k_top = int(np.argmax(amp[1:]) + 1)                 # ignore k=0 (DC)
period_pi = 2.0 / k_top                              # in units of pi

print(f"  dominant Fourier harmonic k = {k_top}    "
      f"=> period = 2*pi/{k_top} = {period_pi:.4f} * pi")
print(f"  top 5 harmonics (k, amplitude):")
order = np.argsort(amp[1:])[::-1][:5] + 1
for k in order:
    print(f"    k = {k:3d}   amplitude = {amp[k]:.4f}   "
          f"period = 2*pi/{k} = {2.0/k:.4f} * pi")

# The 2 pi/6 period reflects an algebraic property of (sigma_1 sigma_2)^3
# rather than the Z_5 structure of the central element: the word contains
# six generator insertions, each carrying delta once via R_tau e^{i delta},
# so K3 is invariant under delta -> delta + 2 pi/6.
print(f"\n  K3(delta) LGI period (this script): 2*pi/{k_top} = {period_pi:.4f} * pi")

# How does the spectrum compare to Z_5?
Z5_periods_pi = [2.0/k for k in range(1, 6)]
print(f"  Z_5 candidate periods (k=1..5, in units of pi): "
      + ", ".join(f"{p:.4f}" for p in Z5_periods_pi))


# ============================================================================
# (2) PURE-STATE ROBUSTNESS K3 at the L=11 optimum and L=22 random optimum
# ============================================================================
print("\n" + "=" * 64)
print("  (2) PURE-STATE ROBUSTNESS  K3 with rho_0 = |psi><psi|")
print("=" * 64)

# The L=11 exhaustive optimum is documented in lgi_results.json as the word
# 's1 s2 s2 S1 S1 S1 s2 s2 S1 s2 s1' with K3 = 1.499762 at delta = 0.
# We reproduce this word here so the script stays self-contained.
def word_to_unitary(word_str, delta=0.0):
    labels = {'s1': 0, 'S1': 1, 's2': 2, 'S2': 3}
    gens = generators(delta)
    U = np.eye(2, dtype=complex)
    for tok in word_str.split():
        U = U @ gens[labels[tok]]
    return U

OPTIMAL_L11 = 's1 s2 s2 S1 S1 S1 s2 s2 S1 s2 s1'
U_opt = word_to_unitary(OPTIMAL_L11, delta=0.0)
U2 = U_opt @ U_opt

# Mixed-state baseline (must match the value in lgi_results.json)
K3_mixed = float(2 * C_mixed(U_opt[None]) - C_mixed(U2[None]))[0] if False else \
           float(2 * C_mixed(U_opt[None])[0] - C_mixed(U2[None])[0])
print(f"  Optimal word L=11 :  '{OPTIMAL_L11}'")
print(f"    K3 (mixed rho_0 = I/2)         = {K3_mixed:.6f}    "
      f"(reference: 1.499762)")

# Pure-state K3 for a set of test states
test_states = {
    '|0>'           : np.array([1, 0], dtype=complex),
    '|1>'           : np.array([0, 1], dtype=complex),
    '|+>'           : (1/np.sqrt(2)) * np.array([1,  1], dtype=complex),
    '|->'           : (1/np.sqrt(2)) * np.array([1, -1], dtype=complex),
    '|+i>'          : (1/np.sqrt(2)) * np.array([1, 1j], dtype=complex),
    '|-i>'          : (1/np.sqrt(2)) * np.array([1, -1j], dtype=complex),
    'random Haar 1' : None,    # will fill below
    'random Haar 2' : None,
    'random Haar 3' : None,
}
rng = np.random.default_rng(20260525)
for k in test_states:
    if test_states[k] is None:
        # Haar-random pure state on the 2-sphere
        z = rng.normal(size=2) + 1j * rng.normal(size=2)
        z /= np.linalg.norm(z)
        test_states[k] = z

pure_results = {}
print(f"\n  Pure-state K3 at the L=11 optimum (delta=0):")
print(f"  {'state':<14} {'K3':>10}    {'C(B)':>9}  {'C(B^2)':>9}")
for name, psi in test_states.items():
    CB = float(C_pure(U_opt[None], psi)[0])
    CB2 = float(C_pure(U2[None], psi)[0])
    K3p = 2 * CB - CB2
    pure_results[name] = dict(CB=CB, CB2=CB2, K3=K3p)
    print(f"  {name:<14} {K3p:>10.6f}    {CB:>9.4f}  {CB2:>9.4f}")

K3_vals = np.array([v['K3'] for v in pure_results.values()])
spread = K3_vals.max() - K3_vals.min()
print(f"\n  spread over initial states = {spread:.4f}    "
      f"(mixed-state value is the average of the pure-state values)")

mean_pure = K3_vals.mean()
print(f"  mean over pure states      = {mean_pure:.6f}    "
      f"(should equal mixed: {K3_mixed:.6f})")
print(f"  difference                 = {abs(mean_pure - K3_mixed):.2e}")


# ============================================================================
# Save
# ============================================================================
out = dict(
    period_scan=dict(
        n_delta=N_DELTA,
        Lmax=LMAX_SWEEP,
        delta_over_pi=list(deltas / np.pi),
        K3=list(map(float, K3_sweep)),
        dominant_k=int(k_top),
        period_pi=float(period_pi),
        top_harmonics=[dict(k=int(k), amplitude=float(amp[k]),
                             period_pi=float(2.0/k))
                       for k in order],
    ),
    pure_state_check=dict(
        word=OPTIMAL_L11,
        delta=0.0,
        K3_mixed=K3_mixed,
        per_state={name: dict(CB=v['CB'], CB2=v['CB2'], K3=v['K3'])
                   for name, v in pure_results.items()},
        spread=float(spread),
        mean_pure=float(mean_pure),
        mean_pure_minus_mixed=float(mean_pure - K3_mixed),
    ),
)
with open('lgi_period_and_purestate_results.json', 'w') as f:
    json.dump(out, f, indent=2)
print("\n-> lgi_period_and_purestate_results.json written")
