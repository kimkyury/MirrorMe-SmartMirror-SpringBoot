import base64
import time

def Encryption(Sentence : str, n : int, e : int) -> str: return "".join([chr(pow(i,e,n)) for i in base64.b64encode(Sentence.encode('utf-8'))])
def Decryption(Sentence: str, n: int, d: int) -> str: return base64.b64decode("".join([chr(pow(j,d,n)) for j in [ord(i) for i in Sentence]])).decode('utf-8')



N = 1517
PNA = 1421
PNB = 1061

print(Encryption("6rBZ68bBiJ46ntHGBfJP",N,PNA))

n ="""
 
Electrodynamics, Quantum
 
W. P. Healy
RMIT University
I.	Introduction
II.	Nonrelativistic Quantum ElectrodynamicsIII. Relativistic Quantum Electrodynamics
GLOSSARY
Anomalous magnetic moment Difference between the intrinsic magnetic moment of a charged spin-  particle and that predicted by the single-particle Dirac theory.
Coherent state State of the quantized radiation field in which the average electric and magnetic fields and the averageenergyarethesameasthecorrespondingquantities for a state of the classical electromagnetic field.
C, P, and T symmetries Invariance of quantum electrodynamics under the operations of charge conjugation (or matter–antimatter interchange), parity (or left–right interchange), and time reversal, respectively.
Dirac equation Four-component relativistic quantum mechanical wave equation for a spin-  particle.
Einstein’s A and B coefficients Factors determining the rates of spontaneous emission, induced emission, and absorption of radiation by atoms.
Feynman diagram Pictorial representation of a process inquantumelectrodynamicsinwhichstatesofparticles or atoms are depicted as lines and their interactions as vertices where two or more lines meet.
Gauge invariance Independence of a quantity of the choice of potentials used to represent the electromagnetic field.
Lamb shift Change in atomic energy levels (from the values predicted by the single-particle Dirac theory) caused by electromagnetic interactions, or the splitting of spectral lines due to this change.
Leptons Spin-  particles subject to the weak and, if charged, the electromagnetic force, but not subject to the strong nuclear force, and including electrons, muons, tauons, neutrinos, and their antiparticles.
Maxwell’s equations General fundamental equations for the electromagnetic field, summarizing the basic laws of electromagnetism.
Occupation-number state State of a quantized field (such as the Maxwell or Dirac field) that has a definite number of particles or quanta in each field mode.
Photon Particle or quantum of the electromagnetic field that travels at the speed of light, has no charge or rest mass, and has intrinsic spin 1.
Renormalization Elimination of unobservable mass and charge of bare particles in favor of observed mass and charge of physical particles.
S-matrix element Probability amplitude for a scattering process in which the incoming and outgoing particles are specified by their momenta and polarization or spin states.
 	199
QUANTUM ELECTRODYNAMICS is the fundamental theory of electromagnetic radiation and its interaction with microscopic charged particles, particularly electrons and positrons. In its most accurate form, the theory combines the methods of quantum mechanics with the principles of special relativity; often, however, it is sufficient to treat the charged particles in nonrelativistic approximation. Each part of the complete dynamical system of radiation and charges displays a characteristic wave–particle duality. Thus, electrons behave in many circumstances as particles, but they can also exhibit wave properties such as interference and diffraction. Similarly, electromagnetic radiation,whichwasconsideredclassicallyasawavefield, may have particle properties ascribed to it under suitable conditions (e.g., in scattering experiments). The particles or quanta associated with the electromagnetic field are called photons.
Quantumelectrodynamicsisahighlysuccessfultheory, despite certain mathematical and interpretational difficulties inherent in its formulation. Its success is due in part to the weakness of the coupling between the radiation and the charges, which makes possible a perturbative treatment of the interaction of the two parts of the system. The theory accounts for many phenomena, including the emission or absorption of radiation by atoms or molecules, the scattering of photons or electrons, and the creation or annihilation of electron–positron pairs. Its most famous predictions concern the electromagnetic shift of energy levels observed in atomic spectra and the anomalous magnetic moment of the electron; both of these predictions are in good agreement with experimental results. Quantum electrodynamics also includes the interaction of photons with muons and tauons (which differ from electrons only in mass)andtheirantiparticles.Thevalidityofthetheoryhas beentestedinhigh-energycollisionexperimentsinvolving these particles down to distances less than 10−16 cm.
I. INTRODUCTION
A. Early Theories of Light
Since quantum electrodynamics is the modern theory of electromagnetic radiation, including visible light, it is instructive to begin with a brief historical review of previous theories. The nature of light has long been a subject of interest to philosophers and scientists. In the fifth century B.C., Empedocles of Acragas held that light takes time to travel from one place to another but that we cannot perceive its motion. He knew that the moon shines by light reflected from the sun and was also aware of the cause of solar eclipses. Heron of Alexandria, who is thought to have lived in the first or second century A.D., discussed the rectilinear propagation properties of light. In his book Catoptrica he derived the law of reflection using a principle of minimal distance. The law of refraction was not formulated until 1621, when it was discovered experimentally by Snell. Snell’s law was later derived theoretically from Fermat’s celebrated principle of least time.
From about the middle of the seventeenth century to the end of the nineteenth century there were two competing, and mutually contradictory, theories of light. The wave theory was initiated by Hooke and Huygens following the first observations of interference and diffraction. Huygens enunciated a principle, based on the wave theory, from which he derived the laws of reflection and refraction. He also discovered the polarization properties of light. These properties, as well as the law of rectilinear propagation, were difficult to explain by the wave theory, which at that time dealt only with longitudinal waves in a hypothetical “aether,” analogous to sound waves in air. These difficultiesledNewtontoproposeacorpusculartheory,according to which light is emitted from luminous bodies in a stream of small particles or corpuscles. Newton’s views inhibited any further advances in the wave theory until about the beginning of the nineteenth century. In the meantime, the fact that light has a finite speed was confirmed by Romer¨ through observations of eclipses of the moons of Jupiter. This occurred in 1675, more than two millenia after the time of Empedocles. (The speed of light in empty space is denoted by c and is approximately 2.998×1010 cm/sec in cgs units.)
B. Classical Electrodynamics
The revival of the wave theory began with Young’s interpretationofinterferenceexperiments.Inparticular,thedestructive interference of two light beams at certain points in space seemed totally inexplicable on the corpuscular hypothesis but was readily accounted for by the wave theory. Young also suggested that light waves execute transverseratherthanlongitudinalvibrations,asthiscouldthen explain the observed polarization properties. The wave theory was further developed by Fresnel, who applied it to phenomena involving diffraction, interference of polarized light, and crystal optics. An important test of the theory was provided by the comparison of the speeds of light in media with different refractive indexes. According to the wave theory, light travels slower in an optically denser medium, but according to the corpuscular theory it travels faster. The results of experiments carried out in 1850 agreed with the predictions of the wave theory.
The wave theory was in a certain sense completed when Maxwellestablishedhisequationsfortheelectromagnetic fieldandshowedthattheyhavesolutionscorrespondingto transverse electromagnetic waves in which both the electric and magnetic induction field vectors oscillate perpendicularly to the direction of propagation. The speed of these waves in empty space could be calculated from constants (the permittivity and permeability of the vacuum) obtained by purely electric and magnetic measurements and was found to be the speed of light. This conclusion becamethebasisoftheelectromagnetictheoryoflight.Itwas subsequently found that the frequencies of visible light form only a small part of the complete spectrum of electromagnetic radiation, which also includes radio waves, microwaves, and infrared radiation on the low-frequency side, and ultraviolet radiation, X-rays, and gamma rays on the high-frequency side.
C. Photons
Despite the success of classical electromagnetic theory in dealing with the propagation, interference, and scattering of light, experiments carried out about the end of the nineteenth century and the beginning of the twentieth century led to the reintroduction of the corpuscular theory, though in a form different to that proposed by Newton. The departure from classical concepts began in 1900 when Planck published his law of black-body radiation. In this law the quantum of action h (approximately 6.626×10−27 erg sec), now known as Planck’s constant, made its first appearance in physics. Planck’s law for the variation with frequency of the energy in black-body radiation at a given temperature is closely related to the existence of discrete energy levels for the electromagnetic field, even though Planck, in his original derivation of the law, did not consider the field itself to be quantized. A black body is one that absorbs all the electromagnetic energy incident on it. It was shown by Kirchhoff in 1860 that when such a body is heated, the emitted radiation does not depend on the detailed composition of the body but only on its absolute temperature. Radiation confined in a state of thermal equilibrium in a cavity with perfectly reflecting walls behaves as black-body radiation. According to classical electromagnetic theory, the cavity radiation can undergo simple harmonic motion at a number of certain allowed or characteristic frequencies ν, the values of which depend on the shape and size of the enclosure. These so-called radiation oscillators may be quantized, as in ordinary quantum mechanics. Then for each nonnegative integer n, an oscillator with frequency ν has a nondegenerate stationary state with energy nhν above the ground-state energy (see
Fig. 1). The possible values of the energy at this frequency thus form a discrete set 0, hν, 2hν, 3hν, ... instead of a continuum. It can be shown that quantization of the oscillators in this way for all the allowed frequencies leads directly to Planck’s law.
In 1905, Einstein made use of the idea of light quanta in order to explain the photoelectric effect and later applied it to the emission as well as the absorption of radiation by
 
FIGURE1 The horizontal lines represent the discrete energy levels of a quantized harmonic oscillator of frequency ν. The energy of the ground state is taken to be 0 and the equally spaced levels 0,hν, 2hν,...,nhν,... are labeled by the quantum numbers 0, 1, 2,...,n,..., respectively. Excitation of the radiation field at frequency ν to level nhν corresponds to the addition of n photons, each with energy hν, to the field.
atoms. The light quantum hypothesis states not only that the energy of monochromatic radiation of frequency ν is made up of integral multiples of the quantum hν, but also that the momentum is made up of integral multiples of the quantum h/λ, where λ is the wavelength of the radiation (ν andλ are related by the equation νλ=c). This hypothesis contrasts sharply with the classical picture in which the energy and momentum are regarded as continuously variable. The existence of discrete light quanta, or photons, is not immediately evident on a macroscopic scale, however. Due to the smallness of Planck’s constant, even in a weak electromagneticfieldthereisanenormousnumberofphotons, provided the frequency is not too high. For example, black-body radiation at a temperature of 300 K (room temperature) contains about 5.5×108 photons/cm3, most of which correspond to frequencies in the infrared part of the electromagnetic spectrum. At a temperature of 6000 K (roughlythatatthesurfaceofthesun),thebulkoftheradiation has frequencies in the visible spectrum, and there are about 4.4×1012 photons/cm3. (The total number of photons in black-body radiation is proportional to the cube of the absolute temperature.)
Individual photons manifest themselves only through their interaction with atomic systems. According to Einstein’s treatment of the absorption and emission of radiation, for example, an atom in a stationary state can make a transition to a lower or a higher energy level accompanied
 
FIGURE 2 An atom can make a transition from a higher energy level Er to a lower level Es while emitting a photon of frequency ν, where hν = Er − Es. The emission may be spontaneous or induced by radiation. The atom can make the upward transition from level Es to level Er by absorbing a photon of frequency ν.
bythecreationorannihilation,respectively,ofaphoton.If theatomicenergiesare Er and Es,where Er > Es,thenthe energyhν ofthephotonmustequalthedifference Er − Es
(see Fig. 2). This is called Bohr’s frequency condition and is equivalent to the law of conservation of energy applied to the complete system of atom and radiation; any energy lost or gained by the atom is given up to or abstracted from the radiation field in the form of photons. It should be noted that the number of photons in the radiation field need not be constant—photons can be created or annihilated through the interaction of the field with atoms.
ThescatteringofX-raysbyfreeelectronsalsofurnishes direct evidence for the corpuscular properties of radiation. In 1922, Compton discovered that when X-rays of wavelength λ are incident on a graphite target, the scattered X-rays have intensity peaks at two wavelengths, λ and λ, where  . The shift in wavelength given by λ  is a function of the angle of scattering (i.e., the angle between the direction of the incident and scattered X-rays) but is independent of wavelength and the target material. The X-rays with unchanged wavelength λ were understood to have been elastically scattered by atoms, which suffer no appreciable recoil, and they could readily be accounted for on the basis of classical electrodynamics. The scattered X-rays with shifted wavelength λ, however, required a new interpretation. If it is assumed that the incident X-rays consist of photons, then these may collide with essentially free electrons in the target. In this case a photon gives up some of its energy hν to an electronandisscatteredwithalowerfrequencyν andalonger wavelength λ, where  .
The wavelength shift λ can be calculated as a function of scattering angle by using the laws of conservation of energy and momentum. By treating the problem relativistically and taking the electron to be at rest initially (see Fig. 3), one can easily show that λ depends on the scattering angle θ alone through the formula
 
FIGURE 3 Photon and electron in the Compton effect (a) before collision and (b) after collision. The scattering angleθ is the angle between the initial and final directions of the photon.
λ = λc(1 − cos θ),
where the constant λc is the Compton wavelength given by
λc = h/mc .
Here m is the rest mass of the electron (approximately 9.11×10−28 g).Thisformulawasverifiedexperimentally. The energy and distribution of the recoil electrons and scattered X-rays were also in accord with the predictions of the photon theory.
D. Quantum Electrodynamics
The use of the photon concept to explain certain phenomena does not imply a return to a naive classical particle view of light and other forms of electromagnetic radiation. A proper account must also be given of the wave properties of radiation, such as interference and diffraction. Indeed, the formulas for the energy and momentum of the photons—hν and h/λ—are based on the assumption that the photons are associated with waves of definite frequency and wavelength. The nature of electromagnetic radiationissuchthatitappears,underdifferentexperimental conditions, sometimes to have particle properties and sometimes to have wave properties—these two aspects are said to be complementary. A single coherent theory that encompassed the dual nature of radiation, and with it settled the age-old controversy between the wave theory and the corpuscular theory, was made possible only by the development of quantum mechanics in the mid-1920s. In 1927, Dirac used the new methods of quantization, which had been successfully applied to atomic systems, to quantize the radiation field enclosed in a cavity, and was thus able to give a fully dynamical treatment of the emission and absorption of light by atoms. The beginning of quantum electrodynamics may be taken to date from this time.
The wave properties of radiation can be adequately described by using Maxwell’s equations for the electromagnetic field, and these are retained as operator equations in the quantum theory of radiation. Suppose, for example, that the electromagnetic field has a node (i.e., a point where the field amplitudes always vanish) due to interference at P. Then an atom placed at P has, in so far as it can be regarded as a geometrical point, zero probability of absorbing a photon from the field. The field amplitudes are, however, subject to uncertainty relations, involving Planck’s constant h, which are analogous to the Heisenberg uncertainty relations for the position and momentum of a particle in ordinary quantum mechanics. The origin of the uncertainty relations for the fields may be understood by considering a simple example.
Let ¯ denote the average value of a component of the electricfieldoveravolume V andatimeinterval T.(Since a field component at a definite point in space and a definite instant of time appears an abstraction from physical reality, only such average values need be considered.) Now ¯ may be found by measuring the change produced by the field in the momentum of a charged test body occupying the volume during this time. Although the position and momentum of the test body are uncertain by amounts q and p that satisfy the Heisenberg uncertainty relation q p ∼h, it can be shown that this does not impair the accuracy of the field measurement, provided a sufficiently massive and highly charged body (which is therefore part of a macroscopic measuring instrument) is used. The charge Q on the body must be such that the product
Qq is large; ¯ can then be measured to any desired accuracy ¯. However, in the measurement of two average field strengths ¯ and  (taken over two space regions V and V  during two times intervals T and T , respectively), it may not be possible to make both ¯ and   as small as desired. If the separation distance L between V and V 
(see Fig. 4) is such that most light signals emitted from V during the time interval T will reach V  during the time interval T , then the measurement of ¯ will influence that of  in a way that is to some extent unknown. The field produced by the test body used to measure ¯ is superim-
 
FIGURE 4 Regions V and V in which the average electric fields ¯ and   are measured during time intervals T and T, respectively. The separation distance L is such that most light signals emitted from V during the interval T will reach V during the interval T.
posed on  and cannot be fully subtracted out, as its value is somewhat uncertain (due to the uncertainty q in the position of the test body). This field, and hence  , can indeed be made as small as desired by making the product Qq sufficiently small, but then ¯ becomes relatively large. The experimental conditions for measurements of ¯ and  are complementary—those that serve to measure ¯ more precisely will meaeure  less precisely, and vice versa. The order of magnitude of the uncertainly product is given by
  h/L3T
and is independent of both Q and q. Thus, only for wellseparated regions or over long intervals of time can both averages be measured with unlimited accuracy.
E. Electrons and Positrons
Dirac’s original radiation theory had to be modified to bring it into line with the special theory of relativity. This was true particularly of the treatment of the charged particles with which the electromagnetic field interacts. In 1928, Dirac had developed a one-particle relativistic wave equation for the electron that automatically accounted for theobservedelectronspinandpredictedvaluesforthefine structure of the energy levels of the hydrogen atom and of hydrogen-like ions that were in agreement with the experimental data of that time. The Dirac equation, however, also has extraneous solutions corresponding to negativeenergystates.Toeliminatethese,Diracintroducedin1930 the so-called hole theory, according to which most of the negative-energystatesareoccupied,eachhavingoneelectron. Any unoccupied states, or holes, may be interpreted asparticleswithpositiveenergyandpositivecharge.These particles were at first thought by Dirac to be protons, but were later identified as positrons, or antiparticles of electrons.
The experimental discovery of the positron by Anderson in 1932 lent support to Dirac’s hole theory. Nevertheless, difficulties remained, such as the infinite (but unobservable) charge density associated with the “sea” of negative-energy electrons. These difficulties can be removed, however, by treating Dirac’s one-particle wave equation for the electron as a field equation and subjecting it to a process of quantization, similar in some respects to the quantization of the classical electromagnetic field. This method, which is often referred to as second quantization, was applied to the Dirac equation by Heisenberg and others and resulted in the appearance of electrons and positrons, on an equal footing, as quanta of the Dirac field, just as photons appear as quanta of the Maxwell field. There are, however, some differences between the methodsofsecondquantizationusedfortheDiracandMaxwell fields, which stem from the different characteristics of the associatedparticlesorquanta.Photonshavezerorestmass (but have nonzero momentum because they travel at the speedoflight),areelectricallyneutral,havespin1(inunits of h✏, which is Planck’s constant divided by 2π), and are bosons (i.e., any number of photons can occupy a given state). Electrons and positrons have the same nonzero rest mass, carry equal but oppositely signed charges (by convention, this is negative for the electron and positive for the positron), have spin  , and are fermions (i.e., not more than one electron or positron can occupy a given state). It was shown by Pauli that there is a connection between the spinofaparticleanditsso-calledstatistics—particleswith integer spin are bosons and are not subject to the exclusion principle, whereas particles with half odd-integer spin are fermions and are subject to the exclusion principle. It is necessary for photons to be bosons in order that the quantized electromagnetic field may have a classical counterpart, which is realized in the limit of large photon occupation numbers. The quantized Dirac field, on the other hand, does not have a physically realizable classical limit.
F. Divergences and Renormalization
Inquantumelectrodynamics,asinclassicalelectrodynamics, there are no known exact solutions to the equations for the complete dynamical system of radiation and charges. Indeed, from a purely mathematical viewpoint, the question of even the existence of such solutions is still an open one. Approximate solutions may be found by assuming that the coupling between the two parts of the system is weak and using perturbation theory. This is justified by the smallness of the fine-structure constant α, which gives a measure of the strength of the coupling:
 ,
where e is the magnitude of the charge on the electron and rationalized cgs units are being used (e ≈1.355× 10−10 g1/2cm3/2/sec).
It was found in the 1930s and 1940s that the calculations for many processes, when taken beyond the first approximation, gave divergent results. Some divergences (the so-called infrared divergences) were due to deficiencies in the approximation method itself. Others (ultraviolet divergences) were associated with the problem of the structure and self-energy of the electron and other elementary particles. This problem had also arisen in classical electrodynamics, where the electron was assumed to have a structure-dependent electromagnetic contribution included in its inertial mass. In quantum electrodynamics, however, there occurred additional divergences of a radically different nature, due to effects that have no classical analogues. For example, the possibility of electron– positron pair creation gave rise to an infinite vacuum polarization in an external field and also implied an infinite self-energy for the photon.
The need to extract finite results from the formalism became acute when refinements in experimental technique revealed small discrepancies between the observed fine structure of the energy levels of atomic hydrogen and that given by Dirac’s one-particle relativistic wave equation. These differences, whose existence had been suspected for some time, were measured accurately by Lamb and Retherford in 1947. In the same year, Kusch and Foley found that the value of the intrinsic magnetic moment of an electron in an atom also differs slightly from that predicted by the Dirac theory. For it to be shown that these discrepancies could be explained as radiative effects in quantum electrodynamics, it was necessary first to recognize that the mass and charge of the bare electrons and positrons that appear in the formalism cannot have their experimentally measured values. Since the electromagnetic field that accompanies an electron, for example, can never be “switched off,” the inertia associated with this field contributes to the observed mass of the electron; the bare mechanical mass itself is unobservable. Similarly, an electromagnetic field is always accompanied by a current of electrons and positrons whose influence on the field contributed to the measured values of charges. The parameters of mass and charge, therefore, had to be renormalized to express the theory in terms of observable quantities. The results for the shift of energy levels (now known as the Lamb shift) and the anomalous magnetic moment of the electron then turned out to be finite andwere,moreover,ingoodagreementwithexperimental results. The use of explicitly relativistic methods of calculation, developed by Tomonaga and Schwinger, was essential in avoiding possible ambiguities in this procedure. FurtherimportantcontributionsweremadebyDyson,who showed that the renormalized theory gave finite results for interaction processes of arbitrary order, corresponding to arbitrary powers of the coupling constant e, and by Feynman,whointroducedadiagrammaticrepresentationofthe mathematical expressions for these processes, which are often of considerable complexity.
The Feynman-diagram technique and Dyson’s perturbation theory are now part of the standard formulation of quantum electrodynamics. This formulation and some of its applications will be outlined in Sections II and III. In this article only the electromagnetic interactions of electrons and positrons (or, more generally, of charged leptons,whichincludemuonsandtauonsandtheirantiparticles) are considered. These particles also participate in the so-called weak interaction (and, of course, in the much weaker gravitational interaction). A unified theory of the electromagneticandweakinteractionshasbeendeveloped in recent years. Many elementary processes, however, are dominated by electromagnetic effects, and these alone form the subject matter of quantum electrodynamics.
II. NONRELATIVISTIC QUANTUM ELECTRODYNAMICS
A. Approximations
Any treatment of the pure radiation field based on Maxwell’s equations in empty space must satisfy the principles of the special theory of relativity, even though it might not be expressed in a form that makes this evident. Quantum electrodynamics has, however, a well-defined nonrelativistic limit in so far as the motion of the charged particles with which the electromagnetic field interacts is concerned.Thenonrelativistictheoryisofanapproximate character, but it involves a much simpler mathematical formalism than that of its more exact relativistic counterpart. Moreover, it can be applied to a wide range of problems in physics and chemistry, particularly in the areas of atomic spectroscopy, intermolecular forces, laser physics, and quantum optics.
Nonrelativistic quantum electrodynamics provides an accurate description of phenomena when the following two conditions are satisfied:
1.	The charged particles move at such slow speeds (inthe inertial frame of a given observer) that their masses can be considered constant and equal to their rest masses. Since the relativistic mass of a particle with speed v and restmassm ism/ ),thisrequiresthatv/c 
Nowthisinequalitygenerallyholdsfortheconstituentparticles of atoms under normal laboratory conditions. For example, the root-mean-square speed υ¯ (relative to the supposedly slowly moving nucleus) of the electron of a hydrogen-like ion in a state with principal quantum number n is Ze2/(2nh), where Ze is the nuclear charge. If Z =1 and n = 1 (the hydrogen atom in its ground state), then v/¯ c equals the fine-structure constant α (approximately  ) and the corresponding fractional increase in mass(overandabovetherestmass)isonlyabout3partsin 105. This ratio is larger for higher values of Z but smaller for higher values of n. The variation of mass with velocity is, therefore, expected to be appreciable only for the inner-shell electrons of the heavier elements.
2.	The number of each type of charged particle (electron, proton, etc.) is conserved; that is, such particles are neithercreatednordestroyedinanyprocess.Thisassumption imposes a restriction on the frequency ν of the radiation with which the particles may interact, since photons of sufficiently high energy are capable of creating particle–antiparticle pairs. This possibility requires an energy of order mc2 (where m is the rest mass of the lightest charged particle, namely the electron) and will therefore be excluded if  c, where νc is defined by hνc =mc2 and is about 1020 Hz. (Here νc is the frequency associated with the Compton wavelength of the electron given by λc =h/mc.) It follows that hard X-rays and high-energy gamma rays are to be omitted from consideration in this section.
B. An Assembly of Photons
The classical electromagnetic field in empty space is equivalent to an infinite number of one-dimensional simple harmonic oscillators. One oscillator is associated with each plane-wave component of the field, specified by its frequency ν, wave vector k (where |k|=2πν/c), and unit polarization vector eˆ. The waves are transverse waves, which implies that the polarization vector is perpendicular to the direction of propagation ˆk (see Fig. 5). Hence, for each propagation direction, there are two independent polarization vectors eˆ(λ)(λ=1,2). A radiation oscillator may therefore be labeled by the pair (k, λ), which specifies the frequency, propagation direction, and polarization for the corresponding mode of the field.
A mathematical description of an assembly of noninteracting photons is obtained when each of the radiation oscillatorsistreatedasaquantummechanicalsystem.This involves little more than the use of the matrix theory of the harmonic oscillator developed in elementary quantum mechanics but extended to cover the case of a set of independent oscillators. The result of this quantization of the electromagnetic field can be briefly summarized. States of the complete system are represented by vectors in a generalized (in fact, infinite-dimensional) vector space and
 
FIGURE 5 A linearly polarized electromagnetic wave of wavelength λ propagating in empty space with speed c in the direction ˆk.The(real)unitpolarizationvectoreˆ andˆktogetherdeterminethe plane of polarization, at any point of which the magnetic induction vector  (broken arrows) is parallel to eˆ and oscillates in simple harmonic motion of frequency ν, where νλ=c. The electric vector  (not shown) also oscillates with frequency ν and in phase with  but is perpendicular to the plane of polarization.
dynamical variables (such as energy and momentum) by linear operators, which act on the vectors to produce other vectors of the same kind. The vacuum state is that for which every oscillator has its lowest energy. It can be assumed, for convenience, that the energy of the vacuum state is zero. The so-called zero-point energy 1/2hν of an oscillator with frequency ν is therefore discarded, but this amountsmerelytoashiftinthedatumpointformeasuring energies. (Nevertheless, changes in the zero-point energy can give rise to measurable forces, for example, between conducting plates. This is called the Casimir effect.)
If a radiation oscillator of mode (k,λ) is excited to its nth stationary state, with energy nhν, then this is taken to correspond physically to the presence of n photons, each with energy hν, for that mode of the field. An occupationnumber state is one with a specified number of photons in each mode. The number nkλ of photons in mode (k, λ) is then called the occupation number for that mode. Only a finite number of occupation numbers can be nonzero and the total numbers of photons is  with the summation extending over occupied modes. Similarly, the total energy E of the photons in an occupation-number state is ). The vacuum state can be thought of as an occupation-numberstateforwhicheveryoccupationnumber is zero.
Theoperatorthatrepresentsthetotalenergyoftheradiation field is called the Hamiltonian operator and is denoted by HRAD. It can be expressed in terms of photon annihilation and creation operators. The annihilation operator for mode (k, λ), when acting on an occupation-number state vector, reduces the number of photons for that mode by one, and when acting on the vacuum-state vector gives the zero vector. Similarly the creation operator increases the number of photons by one. (In the context of the elementary theory of the harmonic oscillator, these operators are usually called lowering and raising operators, respec-
tively.)
A general state of the radiation field at time t is represented by a state vector  of unit length that is a linear combination of the occupation-number state vectors, with coefficients c(..., nkλ,...;t) depending on the occupation numbers and the time. The square of the magnitude of c(..., nkλ,... ;t) is the probability that if a measurement of the occupation numbers is carried out at time t, then these will be found to have precisely the values ..., nkλ,... So long as no measurements are made on the system, the time evolution of the state vector is governed by Schrodinger¨ ’s equation:
ih✏   = HRAD.
The (unit) length of the state vector does not change with time and so the dynamical behavior of the system may be said to correspond to a pure rotation in the generalized vector space. Indeed, the individual probabilities |c|2 do not change with time, since the probability amplitudes c change only through a phase factor exp(–iEt/h✏ ). This is consistent with the fact that for the free field, photons are neither created nor destroyed.
C. The Quantized Electromagnetic Field
Whilethetreatmentoftheradiationfieldasanassemblyof photons may seem to emphasize its corpuscular aspects, thewavepropertiesare,nevertheless,alsocontainedinthe formalism. In particular, Maxwell’s equations in empty space remain valid, although they now appear as operator equations rather than as equations for classical fields. Both the electric field  and the magnetic induction field  become operators that can be expressed as linear combinations of the photon annihilation and creation operators. If these expressions are inserted into the classical formula for the field energy, then the expansion of the Hamiltonian operatorintermsoftheannihilationandcreationoperators is recovered. Thus,
HRAD .
(It is true that an infinite zero-point energy also appears. This energy may, however, be discarded, as were the zeropoint energies of the individual oscillators.) Similarly, the classical expression
1
   ×dV
c
for the field momentum, obtained from Poynting’s theorem, implies, when reinterpreted in terms of annihilation and creation operators, that a momentum h✏ k is to be ascribed to each photon of mode (k, λ). This is in agreement with Einstein’s hypothesis, since h✏|k|=h/λ.
Another consequence of the quantization of the field is the occurrence of uncertainties or fluctuations that have no counterpart in the classical theory. In the vacuum state, for example, the mean value of the electric field is zero but its root-mean-square deviation from the mean, , is nonzero. The fluctuation  arises from the collective zero-point motions of the radiation oscillators and, if calculated for a nonzero volume with linear dimensions of order L and a nonzero time interval with length of order
T, assumes a value whose order of magnitude is given by
   √✏ , if L ≥cT h c

		 ,	if	L ≤cT.
L(cT)
In any other of the occupation-number states, for which the mean values are also zero, the field fluctuations are of greater magnitude than those in the vacuum state. Now the occupation-number states resemble incoherent superpositions of classical plane-wave states, since they are associated with definite wave vectors and polarization vectors butdonothavewell-definedphases(intheclassicalsense), whereasaclassicalplane-wavefieldhasasimpleharmonic time dependence. There exist other states of the quantized field, however, called coherent or quasi-classical states, in which the phase is more well defined but the number of photons, and hence the energy and momentum, is less sharp than for the occupation-number states. To each state of the classical field there corresponds a unique coherent state of the quantized field such that (a) the mean values of the quantized field components are equal to the classical field components and (b) the mean value of the quantized energy is equal to the classical energy. The coherent states are also remarkable in the following respect: the field fluctuations for these states are exactly the same as those for the vacuum state.
The operators representing the components of the electric field  and the magnetic induction field  satisfy certain commutation relations, which may be derived from those for the photon annihilation and creation operators. Just as in ordinary quantum mechanics the commutation
relation
qp − pq = ih✏
between the position operator q and the momentum operator p of a particle leads to the Heisenberg uncertainty relation
q p ∼h✏,
sothecommutationrelationsbetweenthecomponentsof and  lead to uncertainty relations for the electromagnetic field strengths. These uncertainty relations are in agreement with the way in which the field strengths can, at least in principle, be measured by means of macroscopic test bodies. This was shown in detail by Bohr and Rosenfeld in 1933.
D. Interactions of Photons and Atoms
The quantized radiation field has so far been considered as a system by itself. A set of nonrelativistic charged particles, interacting through instantaneous Coulomb forces and also, perhaps, acted on by prescribed external static electric or magnetic fields, can also be considered as a system by itself, as in ordinary quantum mechanics. This system will, for convenience, be referred to as an atom, although it may really be a molecule, an ion, or a collection of atoms, molecules, or ions. It is assumed that there are N charged particles with masses m1,m2,...,mN ; charges e1,e2,..., eN ; position operators q1,q2,...,qN ; and momentum operators p1,p2,...,pN . The Hamiltonian operator for this system is given by
N
	HATOM	α	U,
2mα α=1
where the first term represents the kinetic energy and the second the potential energy. The potential energy U depends on the positions and momenta of the particles, their charges, and the external fields, if any are present.
It is often a good approximation to treat the nuclei as fixed and to regard the coordinates and momenta of the electrons alone as dynamical variables. This is possible becauseofthelargemassoftheprotonsandneutronscompared with that of the electrons (proton mass≈1836× electron mass). The fixed-nuclei approximation involves, among other things, the neglect of the recoil of the atoms which should accompany the absorption or emission of photons. The recoil velocity is, however, normally very small. For example, the speed imparted to a hydrogen atom by a photon with a frequency in the visible spectrum is of the order of 10−8 times the speed of light in vacuo. Such a speed results in only a very slight Doppler shift in the frequency of the emitted radiation. In the fixed-nuclei approximation, the Hamiltonian operator HATOM has, in general, a discrete set of energy levels Er, Es,... corresponding to bound states, as well as a continuous set of energy levels E corresponding to ionized states. Here r,s,... are shorthand notations for sets of quantum numbers sufficient to specify the states completely.
A state vector for the complete system consisting of the atom and the radiation field is obtained by multiplying a state vector for the field directly into a state vector for the atom. For example, there are states for which the photon occupationnumbershavedefinitevaluesandtheatomisin a stationary state with a definite energy. The general state of the complete system is, at any instant, a superposition of such product states.
The Hamiltonian H for the complete system is not simplythesumoftheradiationandatomicHamiltoniansgiven previously. This sum must be supplemented by an interaction term HINT:
H = HRAD + HATOM + HINT.
The inclusion of the interaction term is essential if the operator equations of motion are to reproduce (a) Maxwell’s equations for  and  with the charges and currents as sourcesand(b)theLorentz-forcelawforthechargedparticleswhentheyareactedonbyand,thatis,theexpected equations of motion for the interacting systems. The interaction Hamiltonian HINT contains some operators that refer to the field and some that refer to the particles and, hence, is responsible for the coupling between the two parts of the complete system. In the absence of HINT, the product vectors of the type mentioned above represent stationary states in which the photon occupation numbers are constant and the atom has a fixed energy. Due to the presence of HINT, however, transitions between these states can occur, in which, for example, the atom loses or gains energy and the number of photons is correspondingly increased or decreased. The interaction Hamiltonian may be expressed as the sum of two parts, one proportional to e and the other to e2:
HINT = eH1 + e2 H2,
where H1 is linear and H2 is quadratic in the photon annihilation and creation operators. As a consequence, these two terms give rise to processes in which the number of photons changes by one or two, respectively.
The use of the so-called Coulomb gauge is very convenient in nonrelativistic theory. In this gauge only the transverse electromagnetic field, which is a superposition ofmodeswithtransversepolarizationvectors(eˆ(λ)·ˆk=0), is quantized. The effect of the longitudinal field, responsiblefortheinstantaneousCoulombinteractionbetweenthe charges, is treated as a potential as in ordinary quantum mechanics and is included in the expression for HATOM.
The time evolution of the complete system is governed by Schrodinger¨ ’s equation:
ih✏   H,
∂t where now H is the total Hamiltonian and  represents the state of both the field and the atom at time t. No exact solutions of this equation are known. Fortunately, however, HINT is of order e and, hence, can be regarded as a small perturbation to the unperturbed Hamiltonian HRAD + HATOM. Time-dependent perturbation theory can then be used to calculate approximately the probabilities for transitions between unperturbed states. The total energy is always exactly conserved in transitions between initial and final states. Since the perturbation is small, the unperturbed energy is approximately conserved in such transitions.
E. Applications
Applications of the theory to the emission and absorption of photons by atoms and the scattering of photons by free electrons will now be considered.
1. Spontaneous Emission—Einstein’s A Coefficient
If initially (a) the atom is in an excited state r with energy Er and (b) the radiation field is in the vacuum state, then there is a probability that after a time t a photon of mode (k, λ) has been created and the atom has made a transition to a state s with lower energy Es, where
hν ≈ Er − Es.
Since there are no photons present initially, this process is known as spontaneous emission. It is represented graphically by the Feynman diagram in Fig. 6. Single-photon spontaneous emission involves, in the lowest order of perturbation theory, only that term in the interaction Hamiltonian that is proportional to e. Furthermore, the so-called dipole approximation can be used for optical or lower frequencies and bound states of atoms or small molecules, since then the wavelength of the emitted photon is much larger than the dimensions of the region in which the atomic wave functions differ significantly from zero. The emission probability can sometimes be expressed in terms of a constant transition rate (that is, a probability per unit time for the transition to occur) known as Einstein’s A coefficient. The total transition rate for emission of the photon in any direction and with any polarization is given in dipole approximation by
Ars = (16π3ν3/3hc3)|µrs|2,
where µrs denotes the dipole transition moment, which can be calculated once the wave functions for the atomic states r and s are known. Thus, in dipole approximation, Einstein’s A coefficient is proportional to the cube of the transition frequency and the square of the length of the dipole transition moment.
The reciprocal of Ars is the average lifetime of the upper state r with respect to the lower state s. For example, for optical transitions with a photon wavelength of order 5000 A (1˚ A˚ =10−8 cm) and a dipole transition moment
 
FIGURE6 Feynmandiagramforspontaneousemission.Thelefthand and right-hand portions of the parallel horizontal lines representtheinitialand finalatomicstatesr ands,respectively.(Double lines are used to indicate that the electrons are not free but are bound to the atomic nucleus.) The dotted line represents the emitted photon of mode (k, λ). This is created when the atom undergoes the transition r →s. The vertex labeled e corresponds to the first-ordertermintheinteractionHamiltonian,whichisresponsible for this process in the lowest order of perturbation theory.
 
Electrodynamics, Quantum 
 
FIGURE 7 Feynman diagram for absorption. In the initial state (left of diagram), the atom has energy Es and there is a photon of mode (k, λ) present, whereas in the final state (right of diagram), the atom has higher energy Er and the photon has been annihilated.
of order ea0 (where a0 is the Bohr radius of hydrogen, approximately 0.53 A), the lifetime is of order 10˚ −8 sec.
The transition probability is proportional to the time t so long as t is large compared with the atomic period 1/ν and small compared with the lifetime. Since, with the above assumptions, the period is of order 10−15 sec, there is indeed a range of values of t that satisfy both conditions. The detection of the emitted photons must take place at times t lying in this range, or else the emission rate is not approximately constant.
2. Absorption andhh Stimulated
Emission—Einstein’s B Coefficients
If the atom is initially at the lower level Es, but there is radiation already present, it may make a transition to the hhigher level Er by absorbing a photon with energy approximately equal to Er − Es. The Feynman diagram for absorption is shown in Fig. 7. The transition rate for this process is proportional to the photon occupation number nkλ and hence to the intensity I (erg cm−3 Hz−1) of the incident radiation in the spectral region from which the photon is absorbed. If the atom is bathed in isotropic unpolarized radiation (so that I is independent ofˆk and λ), the total absorption rate is Br s I where Brs is Einstein’s B coefficient for absorption, given in dipole approximation as
Brs = (2π2 /3h2)|µrs |2 .
The upper limit on the time for the validity of this transition rate is now much less than the reciprocal of Br s I. Times less than this upper limit but much greater than the period can be found, provided the intensity of the radiation is not too high.
For an atom initially at the upper level Er with radiation present as before, there is a probability for a transition to the lower level Es accompanied by the emission of a photon with the same characteristics as some of those in the incident beam. This emission may, of course, occur spontaneously, that is, even when all the photon occupation numbers are zero. There is in addition, however, emission that is stimulated or induced by the incident radiation, at a rate proportional to its intensity. For isotropic unpolarized radiation, the stimulated emission rate is Bs r I, where the B coefficient for emission r → s is the same as that for absorption s →r, that is, Bs r = Br s.
3. Thomson Scattering
The nonrelativistic limit of the Compton scattering of photons by free electrons is known as Thomson scattering. This limit applies when both the electron and photon momenta have magnitudes small compared with mc. If p and p denote the initial ahhnal momenta of the electron and
(k, λ) and ( ) denote the wave vectors and polarizations of the incident and scattered photons, then it follows from the laws of conservation of energy and momentum that k ≈k and hence that p ≈ p. Thus, the magnitudes of the momenta are effectively unaltered, although, in general, their directions change. In particular, for the limit considered, there is no shift in the frequency of the scattered photon.
 
FIGURE 8 Feynman diagrams for Thomson scattering. Dotted lines represent photons and solid lines represent free electrons.
The Feynman diagrams that give the leading contributions to Thomson scattering are shown in Fig. 8. Each diagram depicts the incident photon and initial electron arriving from the left, and the scattered photon and recoil electron disappearing to the right. The contribution of Fig. 8a arises from the e2 term in the interaction Hamiltonian; it may be said that here the incident photon is annihilated and the scattered photon simultaneously created. In Figs. 8b and 8c, on the other hand, the annihilation and creation are represented by two different one-photon vertices, each arising from the e term in the interaction Hamiltonian. These diagrams differ in the order in which the creation and annihilation take place. Overall momentum is conserved at every vertex.
It must be emphasized, however, that the contributions of Figs. 8a–8c cannot be physically separated, since only the initial and final states are observed. For this reason, the intermediate states are often referred to as virtual states. Indeed, it may be shown that the contributions of Figs. 8b and 8c effectively cancel, as their sum is of order h✏ k /(mc) times that of Fig. 8a.
In scattering experiments the measured quantity is the cross section (having dimensions cm2), defined as the number of scattered particles per unit time divided by the number of incident particles per unit area per unit time. For Thomson scattering, the differential cross section per unit solid angle  for scattering the photon with polarization λ and direction within d of ˆk is given, from the contribution of Fig. 8a, by
dσ =		2	, r
d
where (a) it is assumed that the polarization vectors are real, (b)  is the angle between the directions of polarization of the incoming and outgoing photons, and (c) r0 = e2/4πmc2 ≈ 2.82×10−13 cm
and is the so-called classical electron radius. (This is the radius that an electron of uniformly distributed charge must have if its electrostatic energy is to equal its rest energy.) It should be noted in particular that, with the approximations indicated, the cross section is independent of frequency and vanishes if the incident and scattered polarization vectors are perpendicular.
If the incident photons are randomly polarized and the polarization of the scattered photons is not observed, then the cross section should be averaged over initial polarization indexes and summed over final polarization indexes. The resulting differential cross section per unit solid angle depends only on the scattering angle θ (where
 
dσ/d .
The total unpolarized cross section, obtained by integrating this over all solid angles, is given by
 .
4. Other Applications
Thefieldofapplicationofnonrelativisticquantumelectrodynamics has expanded considerably in recent years due to the development of lasers and their use as spectroscopic tools for investigating a variety of physical and chemical systems. Lasers are sources of highly coherent and very intense beams of light. In the subject of quantum optics, the quantum statistical properties, such as the degree of coherence, of the light beam itself may be the object of investigation. For example, the quasi-classical states of the radiation field referred to earlier exhibit a higher degree of coherence than that of the occupation-number states, and these in turn are less chaotic than fields in thermal equilibrium, in which the distribution of photons follows Planck’s radiation law.
The high intensity of the light beams that may be achieved by using laser sources can also give rise to nonlinear effects that are unobservable at lower intensities. A typical example of a nonlinear process is third-harmonic generation, that is, the absorption of three photons of frequency ν by an atom and the emission of a single photon of frequency 3ν (the third harmonic of the incident frequency). The rate for this process (after which the atom returnstoitsinitialstateandoverallenergyisconsequently conserved) is proportional to the cube of the intensity of the incident beam. This should be contrasted with a linear process such as single-photon absorption for which the transition rate is proportional to the intensity itself, the factor of proportionality being Einstein’s B coefficient.
III. RELATIVISTIC QUANTUM ELECTRODYNAMICS
A. Relativistic Theory
Relativistic quantum electrodynamics is formed by the union of the special theory of relativity, characterized by the speed of light, and quantum mechanics, characterized by Planck’s constant. In discussions of the relativistic theory it is useful and customary to employ the natural system of units, in which speeds are measured as multiples of c and angular momenta are measured as multiples of h✏ . Since no natural length appears in the theory, lengths continue to be measured in centimeters. The expression for any quantity in (rationalized) natural units is obtained from the corresponding expression in (rationalized) cgs units simply by setting✏ c =1 and h✏ =1✏. For example, the cgs expressions h k,mc2, and e2/(4πhc) for the momentum of a photon, the rest energy of an electron, and thefine-structureconstant,respectively, become k,m, and e2/(4π), respectively, in natural units. It is also easy to convert from natural units to cgs units, by inserting appropriate factors of h✏ and c.
If quantum electrodynamics is to satisfy the principles of the special theory of relativity, its equations must be covariant under Lorentz transformations. Lorentz transformations relate the space–time coordinates x, y, z, and t of events as seen by observers using inertial frames of reference moving with uniform velocity relative to each other. (The coordinates x, y, z, and t are the components of a four-dimensional vector, to be denoted simply by x.) A covariant equation has the same form for two such observers. The fact that physical laws are expressible as covariant equations means that these laws are the same for all observers using inertial reference frames.
The state of a quantum-mechanical system (for example, the electromagnetic field in vacuo) is specified in relativistic theory on a three-dimensional spacelike hyperplane. In a given inertial frame, this consists of either all the points in three-dimensional space at a particular instant of time or all the events on a two-dimensional plane moving for all time perpendicularly to itself with constant speed greater than that of light. Two distinct events on a spacelike hyperplane cannot be connected by signals traveling with speed less than or equal to the speed of light, and so two measurements made in the vicinity of the corresponding space–time points will not interfere. This is known as microscopic causality. The whole of the fourdimensional space–time manifold is filled with a set of parallel spacelike hyperplanes, which may be labeled by an invariant timelike parameter τ, with τ ranging from −∞ to ∞. The evolution of the system is described by specifying the state for each hyperplane τ and is determined dynamically, through Schrodinger¨ ’s equation, on the interval [τ1,τ2], if the state is specified at τ1 and no measurements are made until τ2.
B. Electrons and Positrons
The one-particle relativistic theory of the electron is based on the Dirac equation. This is a differential equation, with matrixcoefficients,foraspinorwavefunctionψ(x)having four components ψµ(x)(µ=0,1,2,3). The requirement that the Dirac equation be covariant determines the behavior of ψ under Lorentz transformations. Since the electron is now described by a four-component spinor rather than by a one-component scalar wave function, it has extra degrees-of-freedom, over and above those allowed by the Schrodingertheory.Thesecorrespondtothespinorintrin-¨ sic angular momentum of magnitude   (in natural units). Hence the spin appears automatically in the Dirac theory of the electron and does not have to be added on in an ad hoc fashion, as it does in nonrelativistic quantum mechanics.
The difficulties of interpretation associated with the negative-energy solutions of the Dirac equation have already been mentioned. These difficulties disappear in the second-quantized version of the theory, in which electrons and positrons are treated on an equal footing and all have positive energy. Moreover, this version provides a calculus for processes involving annihilation and creation of electrons and positrons—in the high-energy regime, the number of these particles is no longer conserved.
The spinor ψ and its related adjoint spinor ψ¯ are first expressed in terms of plane-wave solutions of the freeparticle equation. These solutions correspond to particles with energy E, momentum p, and rest mass e satisfying the relativistic energy–momentum relation
E2 = |p|2 + m2.
The coefficients in the expansions of ψ and ψ¯ may then be interpreted as annihilation and creation operators for electrons and positrons in definite momentum and spin states. The spin states can be chosen to be helicity states of the electrons and positrons, that is, states in which the component of spin in the direction of motion is either  (right-hand helicity) or   (left-hand helicity). It is only the component of spin in the direction of motion that is invariant under Lorentz transformations.
The algebra of the creation and annihilation operators for electrons and positrons differs from that of the creation and annihilation operators for photons. (Technically, it involves anticommutation instead of commutation relations.) The difference arises from the fact that, whereas photons are bosons, electrons and positrons are fermions and are subject to the exclusion principle. The only possible occupation numbers for electrons or positrons are therefore 0 or 1. This is in agreement with Pauli’s spinstatistics theorem, since the spin of an electron or a positronishalfanoddinteger.Itcanbeshownthatquantizing the Dirac field by using commutation relations instead of anticommutation relations leads to a Hamiltonian operator with energy levels that are not bounded below and, hence, one for which no stable vacuum (ground) state exists. (Similarly, quantizing the Maxwell field, which has intrinsic spin 1, by using anticommutation relations instead of commutation relations leads to a breakdown of microscopic causality.)
C. Covariant Quantization of the Electromagnetic Field
The quantization of the electromagnetic field in the Coulomb gauge, though very useful for dealing with bound systems in nonrelativistic approximation, is not a manifestly covariant procedure. In the Coulomb-gauge formalism, only the transverse field is quantized, while the longitudinal field gives rise to an instantaneous interaction between the charges. The division of the field into transverse and longitudinal components, however, is not Lorentz covariant—these components do not transform separately on going from one inertial frame to another. So that the covariance of the theory can be exhibited, it is necessary to use a guage condition on the electromagnetic potentials that is itself covariant. The most convenient such condition is the so-called Lorentz condition. This condition also leads to certain difficulties which are, however, overcome in the formalism developed by Gupta and Bleuler.
The electromagnetic field is, in the first instance, quantized in a covariant way without reference to the Lorentzgaugecondition.Incontrasttothenoncovarianttreatment, there are now, for each wave vector k, four types of photon, corresponding to timelike and longitudinal as well as twotransversepolarizationvectors,whichare,inaddition, four-dimensional rather than three-dimensional vectors. Moreover, the inner (or scalar) product of the infinitedimensional vector space on which the photon creation and annihilation operators act is not positive definite; that is, there exist nonzero vectors in this space the square of whose length is zero or negative. (This is due to the metric of the space–time continuum, which distinguishes timelike from spacelike directions. Thus, the four-dimensional vector x is spacelike, lightlike, or timelike, relative to the origin, according to whether as x2 + y2 + z2 −t2 is positive,zero,ornegative.)Thisconstitutesaseriousdifficulty, sincethequantum-mechanicalstatisticalinterpretationrequires a positive-definite inner product. For the resolution of this problem, the use of the Lorentz-gauge condition, which has yet to be imposed, is of decisive importance.
It may be shown that neither the Lorentz condition nor Maxwell’s equations are satisfied as operator equations in the covariant theory, because they are incompatible with the commutation relations. They are, however, satisfied as equations for expectation values (and hence are satisfied in the classical limit), provided a subsidiary condition is imposed on those state vectors that are to represent physically realizable states. The effect of the subsidiary condition is to make the timelike and longitudinal photons unobservable in real states of the system. These states have either no timelike or longitudinal photons at all or only certain allowed admixtures of them. Moreover, changing the allowed admixtures is merely equivalent to carrying out a gauge transformation that maintains the Lorentz condition. The allowed admixtures are always such that the contributions of timelike and longitudinal photons to, for example, the energy and momentum, cancel out, and only the contributions of the transverse, observable photons remain. Similarly, the statistical interpretation of the theory is consistent, when this is restricted to the calculation of probabilities for physically realizable states.
Despite the fact that timelike and longitudinal photons areunobservableinrealstatesofthesystem,theirpresence is important and cannot be neglected in intermediate or virtual states. For example, the Coulomb interaction may be described in terms of the virtual exchange of timelike andlongitudinalphotonsbychargedparticles.Theappearance of these photons in the formalism is also required, of course, if the theory is to be manifestly Lorentz covariant.
D. Symmetries and Conservation Laws
The coupling between the quantized Maxwell and Dirac fields is represented by a Lorentz-invariant interaction Hamiltonian density INT that links scalar and vector potentials to the charge and current densities. Here INT is linear in the electromagnetic potentials and bilinear in the spinor fields ψ and ψ¯ and is also of order e—there is no e2 term as in nonrelativistic theory. The interaction Hamiltonian density may be derived from a Lagrangian density known as the minimal-coupling Lagrangian density.
It is interesting to note that certain continuous symmetries of the coupled systems are reflected in the structure of the complete Lagrangian density , which is Lorentz invariant and gauge invariant. According to a theorem of Noether,thesesymmetriesmustleadtoconservationlaws. Forexample,theinvarianceofundertimedisplacements implies the conservation of energy; its invariance under space displacements and rotations implies the conservation of linear and angular momentum, respectively; and its invariance under gauge transformations implies the conservation of charge.
The complete system also has three discrete symmetries. It is invariant under (a) charge conjugation C, that is, the interchange of particles and antiparticles (which affects only electrons and positrons, since the photon is its own antiparticle); (b) the parity operation P, that is, space inversion or the interchange of left and right; and (c) time reversal T. This invariance under C, P, and T is not shared by all the laws of nature. The nonconservation of parity in the weak interaction, which is responsible for the dynamics of beta emission, was suggested by Lee and Yang in 1956 and subsequently confirmed experimentally. That the combined transformation of charge conjugation and parity is also not a symmetry follows from the decay of the long-lived neutral K meson into two charged pions, a decay that is forbidden by CP conservation. Invariance under the conbined CPT transformation, established on very general assumptions (Lorentz covariance and locality), then implies that time reversal is also not a symmetry of the physical world. Hence, the separate conservation of C, P, and T is only an approximation which is, however,
 
FIGURE 9 Virtual processes depicted by basic vertex diagrams (to be viewed from left to right). (a) Photon (γ) annihilation and electron–positron (e−e+) pair production. (b) Electron scattering and photon creation. (c) Photon annihilation and positron scattering. Note the convention for the sense of the arrows used on the fermion lines to
distinguish electrons and positrons.
validforphenomenathatareadequatelydescribedbyelectrodynamics alone.
E. The S Matrix and Feynman Diagrams
The S matrix in quantum electrodynamics is used to calculate probability amplitudes for processes in which particles (electrons, positrons, or photons) that are initially free are allowed to interact and scatter. In the so-called interaction picture of the motion, the state vector  for the complete system evolves under the influence of the interaction Hamiltonian INT, alone, and the S operator (or scattering operator) maps the state vector on the hyperplane τ =−∞ (that is, long before the interaction takes place) onto the state vector on the hyperplane τ =∞ (that is, long after the interaction has ceased):
 .
The S operator can be developed as a power series in the coupling constant e. With the help of a theorem due to Wick, the structure of the nth-order contribution, corresponding to the nth power of e in the expansion, may be systematically analyzed and represented by Feynman diagrams. It is usually convenient to use Feynman diagrams in energy–momentum space. These represent all possible virtual processes that can take place for given initial and final momentum and polarization or spin states of the particles. The Feynman rules enable expressions for the probability amplitude or S-matrix element S f i for the process i → f to be written down directly from the diagrams. From this the cross section for the process may be calculated to a given order in e and compared with the experimentally obtained value.
Thelowestorderofperturbationtheroy(n =1)involves only the first power of the interaction Hamiltonia INT, which is linear in the photon annihilation and creation operators and bilinear in the fermion (electron or positron) annihilation and creation operators. This gives rise to processes such as those depicted in the Feynman diagrams of Fig. 9. These diagrams are called basic vertex diagrams. There are in all eight such diagrams, corresponding to processes in which a photon is either annihilated or created and two fermions are annihilated or created or one is annihilated and the other created.
Every Feynman diagram is a combination of some or all of the eight basic vertex diagrams—an nth-order diagram contains n vertices. Energy and momentum (which together form a four-dimensional vector) are conserved at every vertex. (This is in contrast to the nonrelativistic theory, in which momentum but not energy is conserved in virtual processes.) However, the relativistic relation between energy and momentum need not be satisfied for virtual particles. Now this relation cannot be satisfied by all the particles participating in a basic vertex process, which must therefore be a virtual rather than a real process. For example, electron–positron annihilation with the production of a single photon is forbidden by energy–momentum conservation, even though it is allowed by charge conservation. Hence the basic vertex diagrams can appear only as parts of larger Feynman diagrams depicting processes for which overall energy and momentum are conserved and the relativistic energy–momentum relation is satisfied by the (real) particles in the initial and final states.
As an example of a real process, consider the Compton scattering of photons by electrons. This is allowed in the second order of perturbation theory, and the Feynman diagrams, each containing two vertices, are shown in Fig. 10. The corresponding polarized cross section for the laboratory reference system, in which the target electron is initially at rest, is given by the Klein-Nishina formula: dσ
	  =	.
d
Here ν and ν are the frequencies of the incident and scattered photons, respectively, and ε and ε are their (fourdimensional)transversepolarizationvectors,whichinthis
 
FIGURE 10 Feynman diagrams for Compton scattering. The lines are labeled by the four-dimensional energy–momentum vectors of the particles. Energy and momentum are conserved overall and at every vertex. Polarization and spin lables have been suppressed. Diagrams (a) and (b) differ in the order in which the incident photon is annihilated and the scattered photon created.
formula are assumed to be real (so that the photons are linearly polarized). In the low-energy limit (ν  m and
 ), this reduces to the Thomson cross section derived from the nonrelativistic theory. (Note that r0 =α/m). The unpolarized cross section, obtained by averaging over initial and summing over final polarizations, is given by dσ
,
d =−
where θ is the angle of scattering, as in Fig. 3. This reduces to the unpolarized Thomson cross section in the low-energy limit.
F. Radiative Corrections
The first approximation to the S-matrix element for a given process may be improved by adding contributions from higher-order perturbation theory. These contributions, known as radiative corrections, often, thought not always,involveintegralswithultravioletdivergences(that is, the integrals tend to infinity as the upper limits on the momenta of the virtual photons or fermions involved tend to infinity). For example, radiative corrections of second orderine (oroffirstorderinα)relativetothelowest-order term are expected when one of the modifications shown in Fig. 11 is made in a Feynman diagram. Each of the integrals corresponding to the modified diagrams, however, has an ultraviolet divergence.
The divergence difficulties of relativistic quantum electrodynamics may be overcome by first regularizing the theory, that is, by altering it so that all the integrals converge. In the method of dimensional regularization, for example, this is achieved by replacing (in a well-defined sense) divergent four-dimensional expressions by convergent (4−ε)-dimensional expressions, where ε >0. This may be described as reducing the dimensions of energy– momentum space from 4 to 4−ε. The regularized theory is not equivalent to quantum electrodynamics, which is
 
FIGURE 11 Modifications of a fermion line, a photon line, and a basic vertex part leading to second-order radiative corrections. (a) Fermion self-energy arising from emission and reabsorption of virtual photons. (b) Photon self-energy (or vacuum polarization) arising from virtual pair creation and annihilation. (c) Vertex modification arising from virtual photon exchange.
restored only in the limit as ε →0, in which limit the divergences reappear.
The mass and charge of the fermions are then renormalized; that is, the predictions of the regularized theory are expressed in terms of the observed mass and charge of the physical particles rather than the unobservable mass and charge of the bare particles. In this connection, certain relations between fermion self-energy and vertexmodification contributions (see Figs. 11a and 11c), known as Ward’s identities, allow a great simplification to be made. In particular, they imply that charge renormalization arises solely from vacuum polarization effects (see Fig. 11b). It is important to note also that mass and charge renormalization would have to be carried out even if no divergences appeared in the formalism.
Finally, quantum electrondynamics is recovered by removing the regularization. If the method of dimensional regularizationisused,thismeanstakingthelimitasε →0. In this limit, infinities reappear in the relations between the observed and bare masses and charges. These relations, however, are not susceptible to experimental verification, as the bare masses and charges themselves are unobservable. Moreover, as ε →0, the physical predictions of the theory (for example, rediative corrections to scattering cross sections or electromagnetic shifts of energy levels)arefiniteinallordersofperturbationtheoryandare expressed in terms of the observed masses and charges. (For this reason quantum electrodynamics is said to be a renormalizable quantum field theory.) These predictions can therefore be tested against experimental results.
1. The Lamb Shift
The nonrelativistic Lamb shift for atomic hydrogen was first calculated by Bethe in 1947, following the experiments of Lamb and Retherford. Whereas Dirac’s one-
particle relativistic theory predicts that the 2S1/2 and 2P1/2 states of the hydrogen atom have the same energy, Lamb and Retherford showed that the 2S1/2 level is actually
 
FIGURE 12 Feynman diagrams for second-order radiative corrections to atomic energy levels (Lamb shift). (a) Electron selfenergy and (b) vacuum polarization.
higher and found a difference in energy corresponding to a frequency of about 1000 MHz. In Bethe’s treatment, the effect was interpreted as a difference between the electron’s self-energy when free (Fig. 11a) and when bound to the proton (Fig. 12a); a cutoff of order mc was used for the momenta of the virtual photons emitted in each case. The calculation gave no shift for the 2P1/2 level but did giveanupwardshiftofabout1040MHzforthe2S1/2 level and was therefore, in view of the nonrelativistic treatment and the approximations made, in good agreement with the observed value of the separation. This agreement has been enhanced by subsequent refinements in both theory and experiment.
The relativistic treatment of the Lamb shift, which is a bound-state problem, requires a more elaborate formalism (involvingtheso-calledboundinteractionpicture)thanthe S-matrix theory outlined above. In addition to electron self-energy effects, there are vacuum polarization effects (see Fig. 12) and effects due to the finite mass and nonzero size of the nucleus. (The proton is not a pointlike object but has an effective radius of order 10−13 cm.) Vacuum polarization gives a downward shift of about 27 MHz to the 2S1/2 level. The two most precise directly measured values for the 2S1/2 −2P1/2 level splitting in atomic hydrogen are 1057.845(9) MHz, obtained by Lundeen and Pipkin in 1981, and 1057.8514 (19) MHz, obtained by Palchikov, Sokolov, and Yakovlev in 1983. [The figures in parentheses represent uncertainties in the last digit(s) quoted.] In 1994, Hagley and Pipkin deduced the value 1057.839(12) indirectly, by measuring the 2S1/2 −2P3/2 frequency interval and using the theoretical value for the 2P1/2 −2P3/2 fine-structure splitting. A recent theoretical value for the Lamb shift, given by Pachucki et al. in 1997, is 1057.839(4)(4) MHz, where the first error is due to uncertainty in the value 0.862(12)×10−13 cm used for the proton radius and the second error stems from estimates of higher-order binding corrections. The uncertainties, both theoretical and experimental, in the Lamb-shift frequency are of the order of 104 Hz. This should be compared with a frequency of order 109 Hz for the Lamb shift itself and a frequency of order 1015 Hz for an optical transition.
2. The Anomalous Magnetic Moment of the Electron
The comparison of the measured and calculated values of the anomalous magnetic moment of the electron is regarded as an important test of quantum electrodynamics. The anomalous moment arises from small deviations of the electron’s gyromagnetic ratio from 2, which is the value predicted by the Dirac theory. The gyromagnetic ratio ge− is defined throughthe relation between theintrinsic magnetic moment M of the electron and its spin angular momentum S, namely,
M = −ge S.
The directly measured quantity is not the gyromagnetic ration(or g-factor,asitisalsocalled)itselfbuttheelectron anomalyae− ,whichisthedifferencebetweenthisratioand 2, all divided by 2. Thus,
ge− −2 ae .
The electron anomaly is, like the g-factor, a dimensionless constant. Its value is approximately one-tenth of one percent and has been both measured and calculated with great precision. The experimental and theoretical values of ae− agree to seven significant figures ae− = 0.001159652.
Thevalueofge− isobtainedfromthisbysimplearithmetic: ge− = 2.002319304.
In experiments carried out at the University of Washington in Seattle, the accuracy of the measurement has been greatly increased. In these experiments, electrons were held in a configuration of static electric and magnetic fields in a cavity with linear dimensions of order 1 cm. The arrangement is known as a Penning trap. Even single electrons can be held in it for weeks at a time. The electrons in a Penning trap have a discrete set of energy levels and are sometimes considered as part of an atom with a nucleus of macroscopic size, namely the experimental apparatus or, indeed, the earth on which it rests; the atom is called geonium.
The measured value of ae− was reported by Van Dyck, Schwinberg, and Dehmelt in 1987 as aeexp− = 0.0011596521884(43),
whereagainthefiguresinparenthesesrepresenttheprobable uncertainty in the last digits. The electron anomaly, or the g-factor, is the most accurately known of all physical constants. Its measurement does not depend on a knowledge of either the values of other physical constants
 
FIGURE 13 Feynman diagrams for electron scattering by an external field (denoted by X). (a) Zeroth-order contribution yielding a g-factor of 2 or an electron anomaly of 0. (b) Radiative correction of order α yielding a g-factor of 2+(α/π) or an electron anomaly of α/2π.
or the strength of the magnetic field involved in the experiment.
The theoretical value of ae− is obtained by considering thescatteringofelectronsbyanexternal(prescribed)field. Feynman diagrams for the lowest-order contribution to thisprocessandaradiativecorrectionoforderα areshown in Fig. 13. The change in the momentum of the scattered electron ish supplied by the external field. The lowest-order contribution to the electron anomaly is known exactly (its valueα/2π wascalculatedbySchwingerin1948),asisthe contribution of order α2. Further contributions of order α3 and α4 have also been calculated, partly analytically and partly numerically. (The contribution of order α4 arises from 891 different Feynman diagrams.) The theoretical value given by aeth− = 0.001159652140(5.3)(4.1)(27.1)
was obtained by Kinoshita and Lindquist in 1990. Here the first and second errors are numerical and the third (and dominsant) error arises from uncertainties in the value of the fine-structure constant α.
The positron anomaly ae+ was measured by Van Dyck, Schwinberg, and Dehmelt in 1987 by using the geonium experiment. They concluded that any difference between the ratio of the positron g-factor to the electron g-factor and unity must be less than 10−11. This conclusion is strong evidence for the validity of the CPT theorem. Any departure of ge+ /ge− from 1 would signal a breakdown of the combined charge conjugation, parity, and time-reversal transformation as a symmetry of nature.
G. Interaction of Photons and Leptons
Relativistic quantum electrodynamics may readily be extended to include the interaction of photons with certain other charged particles besides electrons and positrons. These are the muon (symbol µ−) and the tauon (symbol τ−) and their antiparticles µ+ and τ+. Muons and tauons have, within experimental accuracy, the same charge (−e) and spin ( ) as electrons, but different masses. While the rest energy (measured in electron volts) of the electron is about 0.511 MeV, that of the muon is about 105.659 MeV and that of the tauon is (with a possible error of about 3 MeV) about 1784 MeV. The fact that the electron, muon, and tauon seem to have identical characteristics (apart from mass) is known as e−µ−τ universality. The muon and the tauon have lifetimes of order 10−6 sec and 10−13 sec, respectively. Electrons, muons, and tauons are all called leptons (as are neutrinos, which are, however, uncharged); they do not, in contrast to hadrons, experience the strong (nuclear) force. On the other hand, they do participate in the weak and gravitational interactions as well as in the electromagnetic interaction.
An example of a scattering process that involves more than one kind of lepton is muon pair production in electron–positron collisions. The Feynman diagram for the lowest-order contribution to this is shown in
Fig. 14. An electron and a positron are annihilated and a virtual photon is created; this in turn is annihilated and a muon and an antimuon are created. For the process to occur, the electron and positron together must have at least the threshold energy equal to twice the rest energy of the muon (about 211 MeV). It should be noted that in Fig. 14 the lepton number, defined as the number of leptons minus the number of antileptons, is conserved at each vertex for both electrons and muons. This is true generally (and for tauons as well) and arises from the form of the interaction Hamiltonian. Each basic vertex involves only one type of lepton or antilepton. There are no vertices involving, for example, the annihilation of an electron and the simultaneous creation of a muon.
In the center-of-mass reference system (in which the electrons and positrons collide head-on with the same energy E),thethresholdenergyisreachedwhentheparticles
 
FIGURE 14 Muon pair production through electron–positron annihilation. The lepton number (in this case 0) is conserved at each vertex for each kind of lepton separately.
have been accelerated to speeds about 0.999988 times the speed of light. For energies much greater than the threshold energy (or speeds even closer to that of light), the unpolarized differential and total cross sections for muon pair production in the center-of-mass system reduce to
d
	d	16E2
and
 ,
where θ is the angle between the incoming electron and the outgoing muon (or between the incoming positron and the outgoing antimuon). The second of these formulas has been verified to within a few percent in experiments using total center-of-mass energies of the order of 55 GeV. (At very high center-of-mass energies, weak-interaction effects must also be taken into account.)
The results of the high-energy experiments can be used to set bounds on possible deviations from exact quantum electrodynamics. The existence of heavy photons, for example, would modify the structure of the theory. (Thus, in the static limit, the Coulomb potential would no longer have a simple inverse-distance dependence). The total cross section for muon pair production would be altered according to
2 σtot →σtot,
where ± are cutoff parameters with the dimensions of energy. For consistency with the experimental results, ± must be at least of the order of 200 GeV. This corresponds to a test of the pointlike nature of photon–lepton interactions down to distances of the order of 1/±, that is, less than 10−16 cm.
SEE ALSO THE FOLLOWING ARTICLES
ATOMIC PHYSICS • ATOMIC SPECTROSCOPY • ELECTRO-
MAGNETICS • MICROOPTICS • OPTICAL DIFFRACTION •
QUANTUM OPTICS • QUANTUM THEORY • RELATIVITY, SPECIAL • UNIFIED FIELD THEORIES
BIBLIOGRAPHY
Cohen-Tannoudji, C., Dupont Roc, J., and Grynberg, G. (1989). “Photons and Atoms: An Introduction to Quantum Electrodynamics,” Wiley, New York.
Craig, D. P., and Thirunamachandran, T. (1998). “Molecular Quantum Electrodynamics: An Introduction to Radiation–Molecule Interactions,” Dover Mincola, N.Y.
Dowling, J. P., ed. (1997). “Electron Theory and Quantum Electrodynamics: 100 Years Later,” Plenum New York. Feynman, R. P. (1985). “QED: The Strange Theory of Light and Matter,” Princeton Univ. Press, Princeton, N.J.
Greiner, W., and Reinhardt, J. (1994). “Quantum Electrodynamics,” 2nd ed. Springer-Verlag, Berlin.
Healy,W.P.(1982).“Non-RelativisticQuantumElectrodynamics,”Academic Press, London.
Kinoshita, T., ed.(1990). “Quantum Electrodynamics,” World Scientific, Singapore.
Milonni,P.W.(1994).“TheQuantumVacuum:AnIntroductiontoQuantum Electrodynamics,” Academic Press, Boston. Pike, E. R., and Sarkar, S. (1995). “The Quantum Theory of Radiation,” Clarendon, Oxford.
Weinberg, S. (1995). “The Quantum Theory of Fields,” Vol. 1, Cambridge Univ. Press, Cambridge.
 
 
Quantum Chemistry
 
Donald J. Kouri
University of Houston
I.	Calculating Atomic and MolecularWave Functions
II.	Electronic Structure and Propertiesof Atoms and Molecules
III.	Quantum Chemical Dynamics
GLOSSARY
Born-Oppenheimer approximation Approximate separation of nuclear and electronic variables in Schro¨dinger equation.
Configuration interaction Variational method using a linear combination of fixed Slater determinants.
Coupled cluster method Nonvariational method using virtual Hartree-Fock spin-orbitals to include configuration interaction effects.
Density functional theory Formally exact method expressing ground state energy in terms of total electron density.
Dividing surface “Surface of no return” that separates product arrangement from all other dynamical configurations.
Eulerian angles Three angles associated with orienting polyatomic systems in space.
Hartree-Fockmethod Variational method based on selfconsistent field approximation, including antisymmetry effects.
Large Bra and Ket vectors Abstract states in quantum mechanics.
Møller-Plessetormanybodyperturbationtheory Perturbation method with respect to a single Hartree-Fock determinant.
Multi-configuration Hartree-Fock method Variational method using a linear combination of Hartree-Fock determinants, in which both spin-orbitals and configuration coefficients are optimized.
Negativeimaginarypotential(NIP) Adhocpotentialintroduced to absorb wave function in dynamical regions of no interest; generally located at dividing surfaces.
Pauli principle Requirement that wave functions be antisymmetric under exchange of identical, half-odd integral spin particles.
Perturbation method Computational method using solutions to a reference problem for a more complicated problem.
Quantum transition state theory Method using NIPs at dividing surfaces to calculate cummulative reaction probability in terms of a “strong interaction Green
function.”
Slater determinant Wave function expression guaranteeing antisymmetry.
Spin Relativistic effect giving rise to intrinsic angular momentum.
Time-independent wave packet theory Time-independent Schro¨dinger equation containing initial wave packet.
 	301
Transition state State of dynamical system at a dividing surface.
Variational method Computational method ensuring an upper bound to the system energy.
Wave function Projection of quantum state onto position eigenstate.
Wave packet Time-dependent wave function.
QUANTUM CHEMISTRY deals with the detailed understanding of atomic and molecular structure, properties, and dynamics based on the mathematical framework of quantum mechanics. This involves determining the quantum mechanical “state vector” of the system, and most commonly in chemistry, this is done in the so-called “coordinate representation,” yielding the “wave function.” The time evolution of the state vector or wave function is governed by the time-dependent Schrodinger equation.¨ A typical strategy expresses the behavior and properties of a bulk system in terms of the smallest possible dynamical system displaying the underlying physical or chemical properties or processes. In the case of chemical reactions, this involves synthesizing the bulk reaction in terms of the smallest possible number of atomic and/or molecular species needed for the basic reaction stoichiometry. For spectroscopy, magnetic, electrical, etc. properties, it typically involves determining such properties for individual atoms and/or molecules.
Under the usual conditions, the most important interactions governing atomic and molecular structure, properties, and dynamics are electromagnetic, and time is treated nonrelativistically. There are, however, some important manifestations of special relativity, such as spin degrees of freedom and the Pauli exclusion principle. It should be clear that quantum chemistry has much in common with atomic and molecular physics and theoretical physics. Here, we focus on the areas of most intense research activity in chemistry.
I. CALCULATING ATOMIC AND MOLECULAR WAVE FUNCTIONS
A. Some Basics of Wave Mechanics
We assume that the reader has some familiarity with quantum mechanics, and here we summarize only a few of the most important aspects, primarily to establish notation. For any atomic or molecular system, there is an associated state vector, , whose time evolution is governed by the abstract Schrodinger equation,¨
	Hˆ  .	(1)
We use the convenient Dirac “ket” notation, , for the state vector (along with the Dirac “bra” notation for the “dual space” vector, , used to compute scalar products in quantum mechanics); Hˆ is the Hamiltonian operator (the generator of the state vector time evolution); and -h-is Planck’s constant h divided by 2π. In quantum chemistry,
Hˆ usually consists of the sum of all contributions to the kinetic energy of the system, Kˆ , and all contributions to the potential energy of the system, Vˆ. The former takes account of energy due to motion, and the second takes account of energy due to position. Like all physical observables in quantum mechanics, Hˆ is a “self-adjoint” or Hermitianoperator,ensuringrealeigenvalues.Particularly useful are state vectors associated with specific values of a complete set of observables. Such sets of observables are composed of the maximum number of dynamical variables whose quantum operators commute (since commuting operators are not subject to a Heisenberg uncertainty condition). Two of the most useful sets of observables are the Cartesian positions of the particles in the system and theircanonicallyconjugatemomenta.Ascanonicallyconjugate variables, the position and corresponding momentumoperatorsofaparticledonotcommute.Consequently, it is customary to use one or the other, and in quantum chemistry,theoverwhelmingimportanceofcoulombicinteractions makes the position variables most convenient. States of well-defined position are eigenvectors of the position operator, xˆ, so that for a particle confined to the x-axis,
	xˆ  ,	(2)
where the eigenvalue x is the point on the axis where the particle is exactly located and  is the (improper) eigenvector for this state. The wave function, χ(x), is a measure of how likely it is that a particle in the state  will be found at the point x. This is called a probability amplitude and is computed as the scalar product of the state   with the state ,
	 .	(3)
If one also represents the Hamiltonian operator in terms of its effect on χ(x), we expect the kinetic energy operator in the coordinate representation to result in changes in where the particle is likely to be found. The most general form is given by
	 .	(4)
The coordinate representation of the kinetic energy operator is
∂2
	 ,	(5)
	2m	−	∂x2
where  ) is the Dirac delta function. For the potential energy, we expect Vˆ to be a function of the particle position operator, xˆ, so in the coordinate representation it is diagonal, with eigenvalues given by the classical potential energy function, V(x). Then the coordinate representation of the time-dependent Schrodinger equation [in one¨ dimension (1D)] is
 ∂
For typical chemical systems, Eq. (6) applies to each Cartesian coordinate for each electron and nucleus in the system, and there are also potential energy terms for the interparticle coulombic interactions. The general form
is
e 
	−  	a, ,t)
a,rl},t)
	ih	.	(7)
∂t
Here, (a,a ) label nuclei, ( ) label electrons,  denotes the set of all vectors from a common origin to the nuclei and electrons,  is the three-dimensional Laplacian for nucleus a (having charge Za), and ∇l2 is the three-dimensional Laplacian for electronl. The enormous difficulty associated with solving Eq. (7) basically stems from the coulombic repulsions and attractions which prevent a separation of variables. In recent years, quantum chemists have become increasingly interested in solving the time-dependent Schrodinger equation directly. How-¨ ever, it remains true that the overwhelming majority of computations have focussed on taking advantage of the fact that (in the absence of external, time-varying perturbations) Hˆ is independent of any explicit time dependence. This makes possible solution by separation of variables,
	 ,	(8)
where
	ih- 	 	E ,	(9)
∂t
	H	= E	.	(10)
Note that we shall always use Dirac notation when writing abstract state vectors and denote abstract operators with a caret. Wave functions and coordinate representation operators will be indicated by ordinary Greek and Roman letters, and we shall suppress the explicit coordinate dependence, except when it is required for understanding. The separation constant, E, is interpreted as the total energy of the system, and Eq. (10) is the “workhorse” of quantum chemistry. However, it is perhaps useful to point out that while the above is totally general for systems in which the preparation of the system is irrelevant (e.g., systems not involving sources), it is not for other problems. For example, in reactive scattering experiments one may desire to determine highly resolved information (e.g., state-to-state cross sections at specific energies), and one must know the detailed initial conditions in order to make a comparison between experiment and theory. Although seldom discussed, the special nature of Eq. (10) can be seen by deriving it in a more general manner.
We do this by noting that time and energy are conjugate variables in the sense of Fourier analysis. A more general way to derive a time-independent wave function equation is to Fourier transform Eq. (7), written more compactly as
	H 	(11)
∂t
If we specify an experiment lasting from ti to t f , a natural definition of a time-independent wave function is
	1	t f	iEt/-h
		dte	χ.	(12)
ti
The equation determining	is obtained, in general, by applying H to	, using Eq. (11), and integrating by parts to yield
(E  eiEt f /-hχ(t f ) − eiEti /- 
Now t f is the end time of the experiment, and for scattering, the products, whatever they are, will have passed through the detector and exited the apparatus. Therefore, χ(t f ) is essentially zero inside the apparatus. However, to obtainEq.(10),onemustalsoassumethatχ(ti)isalsozero everywhere within the apparatus, but this contradicts the fact that one must measure what it is in order to analyze the experimental data. Therefore, the time-independent Schrodingerequationthatcorrespondstoexperimentmust¨ be
	ih--	iEti /-h
	(E  e	χ(ti).	(14)
It is convenient to define ti to be zero. Thus, the timeindependent Schrodinger equation retains a memory of¨ the experimental details. This should not be surprising since it is well known in quantum statistical mechanics that the time-independent von Neumann equation contains the initial density matrix. Of course, the ultimate goal is to determine dynamical information characteristic of the chemical species involved, independent of the experimental details. This means that the ultimate quantities calculated will have had all reference to the experiment removed. Individual definite energy, state-to-state cross sections from Eqs. (7), (10), or (14) will be the same. However, there can be computational advantages to solvingequationscontainingspecificexperimentalconditions.
B. General Aspects of Nuclear and Electronic Dynamics: Born-Oppenheimer Approximation
Except for the hydrogen atom and its isotopic variants, there are no closed form analytical solutions to the Schrodinger equation for atoms and molecules. The sim-¨ plest molecules are H+2 and H2 (and isotopic variants), and they provide convenient examples for sketching the difficulties encountered. For H+2 , Eq. (10) is
 
and the coulombic attraction terms prevent separation of the  dependence. However, the mass of the electron is about 1837 times smaller than that of a proton, so at any given kinetic energy, electrons travel some 43 times more slowly. This suggests one can neglect changes in the nuclear wave function on the time scale for electron dynamics. Mathematically, this is manifested by the approximate separation of variables in Eq. (15), and one should be able to solve the electron dynamics at fixed | R2 − , with the wave function written in a product form. In fact, one may do this in a much more careful way. The potential depends only on the three distances separating the two protons and the electron from each nucleus. It is independent of the three coordinates of the molecular center of mass and the three (Eulerian) angles orienting the three particle triangle. Therefore, one rigorously separates out these six coordinates. The remaining dynamics is then characterized by the total angular momentum quantum number J, the component of angular momentum quantum number M with respect to a z-axis fixed at the system center of mass with arbitrary orientation, and the component of angular momentum quantum number  with respect to a “body-fixed” z-axis that rotates to maintain a definite orientation with respect to the three particle triangle. The wave function becomes a vector of functions,	J , satisfying equations of the form
J
	HJ	J ,	(16)
 =−J
where the Hamiltonian matrix contains the radial kinetic energy and centrifugal energy for the relative nuclear motion, the centrifugal energy for rotation of the electron about the interproton axis, and terms that are nondiagonal in the  index (referred to as “coriolis coupling,” describing the tumbling in space of the three particle triangle). It is common to neglect the coriolis coupling so that one solves a single uncoupled equation for each	J :
	HJ	J  	J .	(17)
This equation is still nonseparable, and the BornOppenheimer approximation consists of assuming a product solution
		J (R,ξ,η)	 J	(R,ξ,η)	(18)
and neglecting ∂φ∂R and ∂ ∂2Rφ2 terms. Here, ξ,η denote the remainingelectroncoordinates.Thenoneobtainsanequation of the form
φHaJ (ξ,η, R)φ
2
	=(R,ξ,η),	(19)
R
where HaJ(R) is a radial kinetic energy operator for the relative dynamics of the two protons (nuclei); it also contains the centrifugal potential (if any) associated with the internuclear rotation. We solve for the eigenvalues and eigenfunctions of the electronic Hamiltonian He(ξ,η, R):
	He .	(20)
Note that the electronic eigenenergies depend on R through the electron-proton attraction terms of the potential operator in He,. Its dependence on  takes account of the electronic rotation about the internuclear vector. Also,thequantumnumberenters He as2,soeachenergy level n is twofold degenerate. The potential energy fornuclearmotionassociatedwiththeBorn-Oppenheimer state ζJ (R)φn(R,ξ,η) is
e2
	Un(R) = n(R) +  .	(21)
R
The electronic energy n(R) and the associated wave function φn(R,ξ,η) can be thought of as “adiabatic” energies and states. They essentially assume that the electron adjusts adiabatically to the nuclear motion. Inclusion of the nuclear derivatives,  and , leads to states that are viewed as “diabatic.” More rigorous treatments exist in which these nuclear kinetic energy terms are eliminated by a mathematical transformation defining the adiabatic and diabatic states.
Thelaststepintheprocedure(attheBorn-Oppenheimer level) is to solve the Schrodinger equation for the nuclear¨ vibrational motion,
	 ,	(22)
and for scattering dynamics,
 
Corrections to take account of the nonadiabatic effects of nuclear-electronic coupling require inclusion not only of
2
the R R n terms, but also the coriolis coupling in the  quantum number, as well as inclusion of more than just a single product form for	J (R,ξ,η). Thus, Eq. (18) is replaced by
		J (R,ξ,η) (R,ξ,η),	(24)
n
which is substituted into Eq. (16) to generate coupled equations for the ζnJ(R). The φn are members of the complete set of eigenfunctions of the Hamiltonian He, in Eq. (20). The study of electronic nonadiabatic coupling is currently of great interest in quantum chemistry.
Finally, before going on, we display in Fig. 1 some examples of the potential energy functions, Un(R), governing the relative nuclear dynamics. The electronic states canbeunderstoodinpartbyusingtheirbehaviorintwoextreme limits. The “united atom” limit (R →0) results in a totalnuclearcharge(Z1 + Z2)e,soforH+2 ,itgivesacharge of+2e.ThelowestH+2 electronicstatethencorrelateswith2 the ground state of He+. When the nuclear repulsion, eR is added to obtain U(R), it results in a coulombic singularity at R =0. At large R, H+2 yields a neutral H-atom and H+, so the electronic energy tends to the ground state of the hydrogen atom. Since eR2 → 0 in this limit, we see that U →−0.5a.u. Similar considerations apply to excited states. For H+2 , the first excited united atom state is the 2pz level of He+, and the large R limit is again a single ground stateH-atomplusaproton.Ofcourse,theprotonsareidentical and one cannot distinguish to which one the electron is bound. This is reflected in the fact that the ground state,  ), wave function has the form
	 ,	(25)
where φ1s(i) is the 1s-hydrogen orbital centered on nucleus i = A or B. The positive sign reflects the fact that the lowest electronic wave function should have the longest possible deBroglie wavelength and must be normalizable. This latter condition implies that φ1,0 vanishes for the electron infinitely far from both nuclei, and the former condition implies that it have no other “nodal surfaces.” The first excited electronic state must likewise have the nodal surface at infinity (for normalizability), but it must also have an additional nodal surface (to give a shorter deBroglie wavelength). This can be ensured by writing
	 ,	(26)
since at any value of R this is zero when the electron is anywhere in the plane bisecting the internuclear distance. In the united atom limit, this plane contains the united nucleus, and φ1s(A) provides the positive lobe and −φ1s(B) provides the negative lobe of the 2pz wave function. Similar ideas apply in general.
In the case of the H2 molecule, there is an additional electron, which introduces additional complexity. This occurs because of an effect of the special theory of relativity, namely,electronspinandtherequirementsofFermi-Dirac statistics and the Pauli exclusion principle. The relativistic requirement that time must be treated on an equal footing with the spatial coordinates was shown by Dirac to lead to an additional matrix structure for relativistically covariant quantummechanics.Itwasalsofoundthateveninthenonrelativistic limit, this matrix structure (though somewhat simplified)didnotgoaway.Inthislimit,Paulishowedthat the matrix operators associated with the remaining relativistic effects obey the commutation relations of a quantum mechanical angular momentum operator, with eigenvalueforthesquareofthespinbeings ,and sz . As a result, it was found necessary to multiply the usual nonrelativistic, single electron solutions of the
Schrodinger equation by either of two spin states,¨	 and
 .Byconvention,theα-statecorrespondstosz  and the β-state corresponds to sz . The energy (Hamiltonian) is independent of the spin angular momentum if one neglects electromagnetic interactions associated with the electron’s magnetic moments arising due to its orbital and spin angular momentum. (Classically, any current or charge circulation produces a magnetic field.) In an analogous fashion, nuclei that are fermions also possess intrinsic (spin) angular momentum. For example, protons and neutrons are fermions, having half-integral spin. Consequently, associated with the nuclear part of an atomic or molecular wave function one must include nuclear spin states.
The second complication arising if a system contains morethanoneofagiventypeoffermion(e.g.,twoprotons inH+2 ;twoprotonsandtwoelectronsinH2;threeelectrons in Li; etc.) is that the wave function (or state vector) must change sign if any two identical particles are exchanged. So long as the system only contains two of any identical fermion particles, the effects of antisymmetry can be accounted for by forming a product of an appropriately symmetrized and antisymmetrized spatial and spin wave functions.
In the case of H2, one approach is to use single electron molecular orbitals patterned after the electronic states of H+2 . Then a symmetric spatial wave function consists of each electron occupying a φ1,0-like state, with the total spatial wave function being a product φ1,0(1)φ1,0(2), with the index in parentheses labeling electron 1 or 2. Obviously, this wave function is symmetric under exchange of the electrons. The spin part of the wave function must be antisymmetric,
	 ,	(27)
or in the usual determinantal form,
	 .	(28)
Ingeneral,interchangingthepairofelectronsinterchanges the columns of the determinant, which ensures a change of sign. This state corresponds to one electron with sz 2
and one with sz 2. The total Sz is zero, as is also the magnitude Sˆ2. The complete molecular orbital description of ground state H2 is then
	 .	(29)
This is a simple example of the “linear combination of atomic-molecular orbital” (LCAO-MO) description of the electronic structure of H2. It is of interest to multiply out the spatial part of this LCAO-MO wave function:
 s
	+φ1s(B,1)φ1s(A,2)].	(30)
This illustrates a very important aspect of the LCAO-MO approach, since the terms φ1s(i,1)φ1s(i,2), i = A, B represent both electrons bound to the same nuleus, A or B. These are called “ionic terms” since, e.g., the state φ1s(A,1)φ1s(A,2) implies that B has lost an electron which is now bound to A.
Another approach is to assign an electron to a spinorbital so that, e.g., having electron 1 on nucleus A with spin α is represented by φ1s(A,1)α(1). Similarly, electron 2 on nucleus B with spin β is described by φ1s(B,2)β(2). We can construct an antisymmetrized total electron wave function as the “Slater determinant”
 
Expanding this yields
 
	−φ1s(B,1)β(1)φ1s(A,2)α(2)].	(32)
Clearly, this wave function contains no ionic terms, but rather assigns one electron to nucleus A and one electron to nucleus B. This is an example of a “valence bond” electronic wave function. In general, both ionic and covalent type terms contribute to the accurate description of electronic states in molecules. In a general LCAO-MO treatment, one would use a sum of a number of atomic electronic configurations to form molecular orbitals, and bydoingso,arbitrarilyaccurateresultscould(inprinciple) be obtained. Similarly, one could take a sum of many distinct valence bond wave functions so that many electronic configurations contribute. Again (in principle), arbitrarily accurate results can be obtained. Both LCAO-MO and valence bond approaches are used by quantum chemists.
When more than two identical Fermions are present in an atom or molecule (e.g., Li or LiH), one no longer can construct a properly antisymmetrized wave function as a product of a symmetrized total spatial and an antisymmetrized total spin wave function. This essentially results from the fact that there are only two possible single electron spin states, α and β. If one tries to form a spin determinant for three (or more) electrons, one always finds two rows of the determinant are equal and it vanishes identically.Theconsequenceisthatonemustformdeterminants using one-electron products of a spin and spatial function. Any particular spatial function can be multiplied by either an α or β spin state so that, at most, each spatial orbital can be occupied by no more than two electrons. The spatial function can be either an LCAO-MO or a valence bond function.
χS=1,Sz=1 = α(A)α(B),	(34)
χS=1,Sz=−1 = β(A)β(B),	(35)
One last important aspect of molecular wave functions is the inclusion of the effect of identical nuclei. Nuclei with half-odd integral spin are Fermions, and the total wave function (nuclear plus electronic) must be antisymmetric under exchange of any two identical nuclei. If they have integer spin, they are Bosons, and the total wave function must be symmetric under exchange of two such nuclei. In the case of H2, we note that exchanging protons A and B affects the nuclear wave function through the polar and azimuthal angles of the internuclear vector. The symmetry is determined by whether J is even or odd, with odd (even) J yielding a nuclear rotational wave function that is odd (even) under nuclear exchange. However, it is also clear that the LCAO-MO φ1,0 [see Eq. (25)] is even if A and B are exchanged, but φ2,0 [see Eq. (26)] will change sign under this interchange. If both electrons in H2 occupy either the φ1,0 or φ2,0 spatial orbitals, then the total electronic wave function is even under proton exchange. If one occupies φ1,0 and the other occupies φ2,0, then the electronic wave function is odd under the exchange. Then the even (odd) J-rotational states times the even (odd) total electronic wave function requires an antisymmetric nuclear spin wave function, while the odd (even) J-rotational states times even (odd) total electronic states require a symmetric nuclear spin state. We note that the odd nuclear spin state has the form χS=0,Sz=0(A, B)  and the symmetric spin states are
Clearly, there are three states possible for S =1(−1 ≤
Sz ≤1) so it is the triplet spin state. The proper enumeration of the possible spin states with even- and odd-J nuclear rotational states is crucial in quantum statistical mechanics.
If there are three or more nuclei in the molecule and someorallareidentical,appropriategeneralizationsofthe above are necessary. In addition, there can be additional symmetry operations (for the nuclei in their equilibrium positions), and in general, it is computationally advantageous to take this into account both in the molecular electronic wave function and in the nuclear wave function. The use of group theory plays a major role in atomic and molecular spectroscopy.
The final topic in this discussion is the nature of the nuclear vibrational Schrodinger equation [Eq. (22)]. If the¨ potentialUn(R)possessesawellsufficientlydeeptosupport bound eigenstates, then one seeks to compute the ζnJν and Jν. One commonly used technique is to expand Un(R) in a Taylor series about the potential minimum at Re:
	Un(R) = Un  Re)2,	(37)
since dRd Un|Re ≡0. In addition, the centrifugal potential is approximated by its value at R = Re. This gives the energy Jν as a sum of the harmonic oscillator energy
- ) and the rigid rotor energy J , where µ is the reduced mass of the two nuclei and ωe is the usual harmonic oscillator angular frequency. A more accurate description can be obtained by including more terms in the Taylor expansion of both Un and the centrifugal potential. This leads to a power series in the quantum numbers ν and J, with cross terms that arise from vibrational-rotational coupling, higher powers of (  due to anharmonic effects, etc.
Again,analogousgeneralizationsexistforsystemswith more than two nuclei. For systems with large numbers of nuclei, it is not convenient nor particularly useful computationally to separate the center-of-mass motion or the three Eulerian angles. This is essentially because of the enormous number of possible relative coordinates and rotating frames for such systems.
C. Computational Tools for Bound States
The two primary tools for computing energy levels and wave functions in quantum chemistry are the variational and perturbation theoretic methods. A key aspect of the wave functions for bound systems is the fact that since the probability of observing system components at infinite separations from one another must be zero, the wave function must vanish on the system boundaries. Further, because the probability density for observing the system in any configuration equals the modulus of the wave functionsquared,andthetotalprobabilityoffindingthesystem somewheremustequal1,boundstatewavefunctionsmust be “quadratically integrable” or L2-functions. In general, the value of the observable total energy of a system in state 	is given by
	E ,	(38)
where dτ is the differential volume element and the integral is over all space. The Rayleigh-Ritz variational principle states that the functional variation of E with respect toeither	or	∗ vanishes,andthattheextremumsolution to the resulting Euler-Lagrange equations is a minimum. Rearranging Eq. (38), we calculate
 dτδ	∗(E − H)	
	 ,	(39)
andweimposetheconditionδE ≡0.Sincecomplex	and 	∗ are linearly independent, so also are their variations and consequently the coefficients of both δ	and δ	∗ must separately vanish. This yields the usual Schrodinger¨ equation, (E − H)  0, or its complex conjugate, and establishes that a complete minimization of E yields the exact energy. Alternatively, we can expand	in Eq. (38) using the complete set of eigenfunctions of H, {φn},
satisfying	
Hφn = Enφn,	(40)
so that
		 .	(41)
n
Then subtracting the lowest (ground state) energy, E0, from both sides of Eq. (38), and substituting Eq. (41), we obtain
	E  cn .	(42)
The right-hand side of the above equation is greater than or equal to zero, so we conclude that
	E ≥ E0,	(43)
which proves that Eq. (38) yields an upper bound to the ground state energy of the system. In practice, one typically expands	in some appropriate basis functions (satisfying the same boundary conditions as the exact	):
		 .	(44)
j
Then E is computed, along with  ∂E (noting that since H is self-adjoint, it is not necessary to also examinej ∂∂aEj ), yielding
E , (45) j 	j 
with
	Hjj ,	(46)
and
	S .	(47)
The matrix Sjj  is called the “overlap” matrix; if the basis functions are orthonormal, Sjj , where the Kronnecker delta   is zero unless j . In matrix notation, Eq. (45) is referred to as the generalized eigenvalue problem of linear algebra:
	ES · a = H · a.	(48)
In addition, normalization of	implies that
	 .	(49)
j
Major research activities in quantum chemistry center around developing efficient ways to compute the Hjj  and to solve for the E’s and a’s.
In perturbation theory, the strategy is to use or construct a solvable quantum problem which is as close as possible to the unsolvable system of actual interest. If H0 is the “reference system” Hamiltonian and H is the true system Hamiltonian, then the perturbation, λV, is defined as
	λV = H − H0,	(50)
where λ is an arbitrary parameter such that when λ=1, onehasthetruesystem.Letthecompletesetofeigenstates of H0 be denoted by {ψ0j ; j =0,...}, such that
	H .	(51)
It is assumed that the true eigenstates, satisfying
	(H0 + λV)ψk = Ekψk,	(52)
can be expanded in a power series in λ, as can Ek also:
n
	k ,	(53)
n=0
	Ek  .	(54)
n=0
We substitute Eqs. (53)–(54) into Eq. (52) and require the coefficients of each separate power of λ to vanish identically:
n
	H0ψkn + Vψkn−1 =  Ekl ψkn−l.	(55)
l=0
Thus,
	H ,	(56)
	H ,	(57)
	H ,	(58)
etc. The first equation shows that the zeroth order solution is given by the reference problem. The second equation leads to
	 .	(59)
Inserting the resolution of the identity in the unperturbed basis, this becomes
	Vjk ,	(60)
	E	E
	j=0	k −	j	
where we must require that
	E Vkk	(61)
in order for ψk1 to exist. Then, Eq. (60) becomes
0
k Vjk, (62) j	E j
and the first order correction to the energy is given by Eq. (61). If there are degeneracies, then Eq. (62) will still contain singularities for all j such that E . When this occurs, the procedure is modified by replacing the degenerate ψ0j by linear combinations:
	 	bkjψ0j	(63)
j=degeneratewithk
and choosing the {bkj} so that the submatrix  is diagonal. This (along with normalization of the new reference states) determines a new modified subset of degenerate, unperturbed states which are uncoupled by the perturbation. If the new states are labeled by ψ˜ 0k, then
 , and the first order correction to
the energy for the degenerate states is
	E  V˜ kk,	(64)
and
0
	.	(65)
E − E j
Here, {k} denotes the modified degenerate states.
The second order correction is obtained by solving Eq. (59),
	 .	(66)
Again expressing the unperturbed Green function in the unperturbed basis (including the superposed degenerate states ψ˜ 0k), we obtain
We require that
	E 	(68)
and
0
,	(69) j  E j
and we understand that no degeneracy terms occur where E0j canequal Ek0.Thesecondordercorrectiontotheenergy can be computed knowing the first order correction to the wave function. In fact, knowing ψk1 enables one to determine the energy up to third order, Ek3, according to
	E .	(70)
In general, knowing the wave function through order n determines the energy up through order 2n +1.
II. ELECTRONIC STRUCTURE AND PROPERTIES OF ATOMS AND MOLECULES
A. Variational Methods
The most widely used approaches to calculating energies and wave functions for electrons in atoms and molecules have their roots in attempts to approximate the relevant Schrodinger equation (within the Born-Oppenheimer¨ approximation) in terms of some sort of “independent electron” model. The crudest is simply to neglect all electron-electron repulsions and construct a product wave function using hydrogenic-like orbitals (with proper nuclear charge). Each orbital is assigned to two electrons until all electrons are accounted for. This includes the effect of the Pauli exclusion principle and leads to the simplest “aufbau principle” for building up atomic and molecular structure.MorerealisticresultsareobtainedbytheHartree self-consistent field approach. Again, the wave function is taken to be a single product of one-electron orbitals, each associated with at most two electrons, but the orbitals are now considered unknowns. They are determined by successively projecting the action of the Hamiltonian on the product wave function onto all but one of the various orbitals,toobtainasetofeffectiveone-electronorbitalequations of the form
 ,..., Z,
(71)
where we illustrate the expression for a neutral atom with nuclear charge Ze. Here, Vieff is given by
	Vieff  .	(72)
We see that Eq. (71) is a set of nonlinear, integrodifferential equations that must be solved iteratively. This is done by guessing initial functions for the φi,i =1, ..., Z that appear in the effective potentials. Then the resulting equations are uncoupled, linear partial differential equations for the i and φi. Once they are solved, new Vieff are calculated and used to generate updated equations,Eq.(71),andtheprocedureisrepeateduntilthei,φi do not change to within a given tolerance. The approximate total energy is computed as the expectation value of the full Hamiltonian using the final product wave function determined by the self-consistent procedure.
A more sophisticated approach is the multiconfigurationself-consistentfieldHartree-Fock(MCSCFHF) approximation, which expresses the electronic wave function as a sum of “Slater determinants,” constructed from one-electron spin-orbitals. This yields a properly antisymmetrized wave function,
		 Cl l.	(73)
l
The individual “configuration” Slater determinants,  l, are constructed from spin-orbitals, φj, given by
	 	or	 ,	(74)
where χλ is a spatial basis function. The χλ generally fall into two classes:
 Slater-type orbitals (STOs)
	χλ = NnlmζYlm(θ,φ)rn−1 exp(−ζr),	(75)
where Nnlmζ is the normalization constant and ζ determines the radial “size” of the STO (physically, it is associated with an “effective nuclear charge”).
 Cartesian Gaussian-type orbitals (GTOs)
	χλ = Nabcαxa ybzc exp(−αr2),	(76)
where Nabcα is the normalization constant and α determines the radial size of the orbital. Note, e.g., that (a,b,c)=(1,0,0), (0,1,0), or (0,0,1) are px, py, pz orbitals; (a,b,c)=(2,0,0), (0,2,0), (0,0,2), (1,1,0), (0,1,1), (1,0,1) are sufficient to describe five d-orbitals and an s-orbital [since the sum of (2,0,0), (0,2,0), and (0,0,2) yields the function r2 exp(−αr2)].
In early work in quantum chemistry, STOs were the most commonly used basis, but as digital computers have becomemorepowerful,withincreasedmemory,theGTOs have dominated computations. The STOs have the attractive feature of behaving properly at the nucleus, but the matrix elements of the Hamiltonian between STO spin-orbitals are computationally costly. The GTOs permit these matrix elements to be evaluated routinely (even in polyatomic systems), but they do not behave correctly at the nucleus. However, it is possible to replace the χλ in Eq. (76) by a sum of Gaussians with fixed coefficients and different α-values, determined so as to mimic the cusp behavior at the nucleus. These are referred to as “contracted GTOs” (CGTOs). It is also sometimes efficient to use CGTOs that have been determined variationally from atomic structure calculations. These are useful for treating “core” electrons that retain a significant atomic character within the molecule.
In order to understand the level of sophistication of a given calculation, it is necessary to understand some basic terminology. A minimal basis is one in which the number of STOs or GTOs is equal to the number of core and valence orbitals in each atom. A double zeta basis is one in which there are twice as many STOs or GTOs as there are core and valence atomic orbitals. This gives greater flexibility to the LCAO-MOs that ultimately appear in each of the Slater determinants (configurations). Typically, one of the pair has a smaller exponent (α or ζ) and one has a largerexponent.Atriplezetabasishasthreetimesasmany STOs or GTOs as the number of core and valence atomic orbitals.Evenlargerbasissetsarepossible.Onesuchbasis is denoted by (10s,6p/5s,4p), indicating that 10 s-type primitive GTOs were contracted to yield 5 distinct s-type CGTOs and 6 primitive p-type GTOs were contracted to provide 4 distinct p-type CGTOs. Another Gaussian-type basis is denoted STO-3G, where three Gaussians each are used in a least squares fit of STOs, which have been optimized to describe various atomic electronic states. Yet others are denoted as 4-31G and 5-31G bases. In this case, the core orbital space is treated with CGTOs containing four or five Gaussians. The valence orbital space is treated at a double zeta level, with the first CGTO constructed from three primitive GTOs and the second containing one primitive GTO.
The framework of the Hartree-Fock approach is common to many of the most widely used electronic structure computational methods. Here we summarize some of these and indicate how they are related. In the MCSCF version,thevalueof E =	|H|	 isdetermined variationally with respect to the CI coefficients, Cl, in Eq. (73) and simultaneously with respect to the Cλj coefficients in the individual spin-orbitals. In addition, the Cλj areconstrainedtosatisfytheortho-normalizationrelations
	 .	(77)
λ,λ 
The fact that the exact H contains at most two-electron interactionsimpliesthatitsmatrixelements,whilequadratic in the Cl, are quartic in the spin-orbital coefficients, Cλj. This makes a full MCSCF calculation very costly and limits the size basis set that is practical. The CI method involves first determining the LCAO-MO coefficients in a single determinant SCF (sometimes called an “unrestricted Hartree-Fock” or UHF approximation) or small MCSCF calculation. Then the Cλj are fixed and a CI calculation is carried out in which only the Cl are varied.
B. Nonvariational Methods
There are several nonvariational methods that make use (usually)oftheresultsofanUHFcalculation.Onemethod is called M-Plesset perturbation theory (MPPT) or, equivalently, many body perturbation theory (MBPT). In the UHF calculation, there are no Cl coefficients and the Cλj and j are obtained by solving the so-called Roothan matrix Hartree-Fock equations,
	 λ λ	λj	j	λ λCλj,	(78)
where
F  j
(79)
Here, h is the one-electron part of the full Hamiltonian, g is an electron-electron repulsion potential energy, and
	 i,	(80)
i
	 CδiCκi,	(81)
i
where the single primed sum is over all occupied spinorbitals and the doubly primed sum is over all occupied spin-orbitals having the same spin as spin-orbital j. Since the operator depends on the unknown {Cλj}, the equations again must be solved iteratively. One specifies an initialguessfortheoccupied{Cλj};computestheRoothan Hartree-Fock matrix, F  j , j =1,..., Z; and then solves the resulting linearized eigenvalue equations [Eq. (78)] for the and the new {Cλj}. Then new are computed and the procedure is repeated until the results converge. We note that the dimensionality of the matrix F  j is M × M, where M equals the total number of atomic basis orbitals used in the LCAO-MO expansion. It therefore has M eigenvalues j and associated eigenvectors, Cλj,m,m =1,..., M. In general, 1≤ j ≤ Z, and M will be larger than Z. Consequently, only the lowest energy of each spin-orbital set, {φj,m}, 1≤ j ≤ Z, will be occupied. The unoccupied ones are referred to as virtual spinorbitals.
The unperturbed Hamiltonian for the MPPT/MBPT method is taken to be the sum of the F j matrices:
Z
	H F j,	(82)
j=1
and the perturbation is the difference between the exact H and H0 in Eq. (82).
The other nonvariational approach using the UHF as its starting point is the coupled cluster (CC) method. In this approach, CI-like effects are included in a different fashion. One writes the total wave function as
		= exp(T) ,	(83)
where   is usually an UHF Slater determinant and the operator T generates the so-called single, double, etc. “excitations.” The singles are determinantal wave functions in which one of the occupied spin-orbitals is replaced by a virtual spin-orbital, doubles have two occupied spinorbitals replaced by virtual spin-orbitals, etc. The form of T is
	T   tijmnm+n+ij + ···,	(84)
	i,m	i,j,m,n
where i, j,... remove occupied spin-orbitals and m+, n+,... create occupied virtual spin-orbitals φm,φn,.... The tim,tijmn,... play the role of the usual CI coefficients, Cl. However, they are not determined variationally. Rather, one uses the fact that  =exp(−T)	to write the Schrodinger equation as¨
	  E .	(85)
Thisisprojectedontothevarioussingle,double,etc.Slater
determinants,  to yield, e.g.,
	 ,	(86)
	 ,	(87)
etc.Thezeroesontheright-handsidesofEqs.(86)and(87) result from the fact that all of the single, double, etc. Slater determinants are automatically orthogonal to the UHF state, . This is a consequence of the occupied and virtual spin-orbitals for any j being eigenvectors of a Hermitian matrix.
It is useful to comment here on the strengths and weaknesses of variational and nonvariational approaches. In fact, the two approaches are complementary, in that variational methods provide rigorous upper bounds for the total energy, but these energies are not “size extensive.” That is, a calculation on two CH3 radicals at very large separation will not, in general, give an energy that is twice that of a single CH3 radical. The MPPT/MBPT method is size extensive, but does not guarrantee that the total energy lies below the approximate energy. This suggests that the method of choice depends on the objective of a givenapplication;e.g.,extendedsystemsarebettertreated nonvariationally.Forfollowingcertainchemicalreactions, electronrearrangementrequirestheinclusionofmorethan one configuration. In that case, the crucial role of the UHF determinant in MPPT/MBPT suggests that one would be better off using MCSCF or CI.
C. Density Functional Theory
Another major approach to atomic and molecular electronic structure is density functional theory (DFT). Closely related are the Thomas-Fermi and X−alpha (Xα) methods; since they have been supplanted by DFT, we shall concentrate on it. The fundamental basis of DFT is thefactthatonecanprovethatthegroundstateenergy, E0, ofa Z-electronsystem(atomormolecule)isexactlydetermined by a functional, E0(ρ), of the total electron density,  ), of the system. Note that this does not provide the explicit dependence of E0 on ρ, but rather guarantees that if one can determine ρ, this, in principle, determines the exact ground state energy. The resulting equations to be solved are
 
	 i,	(88)
where UX ) is an effective one-particle potential that accounts exactly (in principle) for all electron-electron correlation and exchange effects, and the integral term involving ρ is the coulombic interaction at the pointr due to the total electron density. Note that UXα also must remove the “self-interaction” of the electron occupying orbital φi with its own contribution to  ). The DFT equations, like the Hartree approximation equations, must be solved iteratively, since it is easily verified that
	 ,	(89)
j
where n j is the number of electrons occupying orbital φj. Thus, one begins with an initial guess of the φj and computes ρ. If one also has an estimate of UXα, then Eq. (88) is a linear eigenvalue problem for calculating a revised estimate of the φj and its single particle energy, i. Once Eq. (88) is solved, a new  ) is calculated from Eq. (89) and the procedure is repeated until one reaches selfconsistency. The total energy of the system is computed as
E  n j
j
  .
(90)
The greatest difficulty in the theory is obtaining an accurateapproximationforUXα,andthisisaveryactiveareaof research. A popular choice is the so-called “local density approximation” (LDA), for which
	UX .	(91)
Theoretical work indicates that α =2/3 is the optimum value to use.
All of the above discussion has been couched in purely theoreticalterms.Whenalloftherelevantmatrixelements of the Hamiltonian are computed from first principles, the calculation is referred to as “ab initio.” However, a great deal of quantum chemical applications use various ways to estimate the Hamiltonian matrix elements. These can range from ignoring the effects of nonorthogonality of the atomic orbitals centered on nonbonded atoms to approximating matrix elements using experimental data. The resulting approaches are referred to as semi-empirical methods,andthereexisthighlydevelopedcomputercodes anddatabanksforcarryingoutsuchcomputations.Details can be found in some of the bibliographic references at the end of this article.
D. Other Properties
Finally,wecommentonthecalculationofpropertiesother than the electronic energy. These are usually expressed in terms of the response of the system to some appropriate external perturbation, λV. These properties are typically evaluated by doing a Taylor expansion of the total energy of the perturbed system about λ=0,
	E 	(92)
where
E 
 
	l	 
j,µ  
 , (94)
etc. The value of (dEdλ)λ=0 depends not only on the nature of the perturbation, but also on the method used to obtain 	(λ=0). Thus, for the MCSCF method, derivatives of	with respect to the Cl and Cµj vanish identically since the MCSCF functional is stationary with respect to such variations. If the atomic orbitals, χµ, do not depend explicitly on the external field, then (∂χ ∂λµ)λ=0 ≡0, and the first order effect is due solely to the average of V. In, e.g., the CI method,  0, but 0 since the Cµj are not varied
l to minimize the CI energy functional.
III. QUANTUM CHEMICAL DYNAMICS
A. Early Transition State Theory
Over the past 30 or so years, the field of rigorous quantum chemical dynamics has been created. Prior to this, the dominant method used to calculate rates was the transition state approach. The role of quantum mechanics was mainly to determine the Born-Oppenheimer potential surface for nuclear dynamics and the eigenenergies of various bound degrees of freedom of the full system at the transition state (for use in calculating the transition state partition function). The definition of the transition state is most easily given for systems in which the collision process has to pass through a so-called “bottleneck” (e.g., assumed in many cases to be the saddlepoint in the Born-Oppenheimer nuclear potential surface, separating reactants and products). Generally, it is assumed that in all collisions in which the system reaches the transition state configuration, having positive kinetic energy (positive velocity in the direction of the product region), the reactive probability equals 1. The transition state is sometimes couched in terms of a “dividing surface” normal to which a positive velocity inexorably leads to reaction. An additional quantum modification is to introduce an additional “transition factor” which can account for effects such as tunneling (for collision energies below the saddlepoint barrier height, which otherwise have a zero reaction probability) as well as corrections to the assumption that all positive kinetic energy trajectories reaching the transition state cross to products with unit probability.
B. Rigorous State-to-State Quantum Reactive Dynamics
Although such transition state-based methods continue to play a major role in ab initio predictions of reaction rates, there now exist several rigorous quantum treatments of atom-diatomanddiatom-diatomreactivecollisions,yielding detailed quantum state resolved probabilities, cross sections,andrates.Mostoftheseemployarotating,centerof-mass coordinate frame (rigorously separating out the three coordinates of the center of mass and the three Euler angles characterizing the overall rotation of the three or four atom system). In reactive scattering, the major complicationistheresultofthefactthatthenaturalcoordinates fordescribingtheatomicandmolecularspeciesineacharrangement are different. This is easily seen by considering an atom-diatom collision system like D + HF. Depending on the collision energy, there can be as many as four arrangements:
 D + HF
 H + DF  F + HD
 F + H + D
In the first, the three natural coordinates remaining after separating off the center-of-mass and Euler angles of rotationaretheinternuclear HF distance,r1;thedistanceof D fromthe HF centerofmass, R1;andtheangle,γ1,between these two distance coordinates. Analogous but distinct sets of three natural coordinates apply to the second and thirdrearrangements.Forthelastarrangement(termedthe “breakup”arrangement),thenaturalcoordinatesarecalled hyperspherical coordinates and typically consist of a hyperradius ρ (whose square equals the sum of the squares of the two distance coordinates for any of the other three arrangements, i) and two angles. One of these can be the same as the γi in any of the other coordinate sets, and the second angle is typically defined as α ≡arctan(ri/Ri). The boundary conditions are very different in each of the limits Ri →∞, i =1,2,3 or ρ →∞ (the latter requiring that both ri, Ri →∞ simultaneously). We note that the breakup process has only been treated quantatively within a collinear model of chemical reaction; a major topic of research is the development of methods for treating breakup in full dimensionality. Henceforth, we restrict our discussion to collisions well below the breakup energy threshold. Computational methods that have been applied include algebraic variational methods and direct numerical solution of the discretized partial differential form of the Schrodinger equation. For scattering, the most widely¨ used variational principles are based on the generalized Newton and the Kohn functionals, and they are stationary rather than extremal. They are typically employed using basis set expansions, with the stationary condition leading to linear systems of inhomogeneous algebraic equations. Either the basis functions explicitly include terms to satisfy the various asymptotic boundary conditions or the variational functional itself explicitly includes them through the appearance of “causal” or “anticausal” Green functions.
A major advance in dealing with the problem of coordinates in reactive scattering was the introduction of a practicalmethodforeliminatingtheneedtosolvesimultaneously for the dynamics in all three arrangements. This is done by introducing ad hoc, localized negative imaginary potentials (NIPs) designed to absorb the wave function in regions that are not of direct interest. This permits one to solve the Schrodinger equation only in the region leading¨ from reactants to the one transition state of interest. Both a time-dependent and time-independent version of the approach exist. It is also possible to resolve state-to-state reactive scattering amplitudes at any energy contained sufficiently in the t =0 wave packet. The approach yields results in quantitative agreement with those obtained by the more traditional methods. We note that in the traditionalnumericalintegrationapproach,oneisusuallyfaced with solving the equations subject to so-called “two-point boundary conditions.” One condition is that the solution be regular at the origin, and the others are that the solution have incident waves only in the initial arrangement and that there be only outgoing scattered waves in all possible product arrangements. Since the amplitudes for scattering into the various possible final states are unknown (and are what one is trying to compute), one only knows the form of the scattering boundary conditions and not their numerical values. Consequently, it is necessary to generate enough linearly independent solutions of the differential equations to form linear combinations that possess the correct asymptotic behavior. The general procedure is to expand the total wave function in internal basis states, giving rise to coupled ordinary differential equations for the expansioncoefficients.Ifthereare N basisfunctionsinthe expansion, there result N coupled second order differential equations, having in general 2N linearly independent solutions. At most, only N of these can be regular at the origin, leading to the necessity of solving the coupled differential equations N separate times for these N sets of linearly independent regular solutions. The expansion in the N basis functions yields an N × N Hamiltonian matrix operator, and propagating each N component regular solution vector involves doing N2 multiplications at each step of the propagation. Since this is done N times, there is a total of N3 multiplications at each step, for an overall scaling of MN3, where M is the number of steps needed to escape the scattering interaction. This must be redone at each separate energy E for which one desires scattering information. By comparison, solving the time-dependent
Schrodinger equation formally, one gets¨
	χ(t) = e−iHt/-hχ(0).	(95)
ApopularwaytoevaluateEq.(95)istotaket shortenough that one can approximate exp(−iHt/-h-) as the product exp(−iVt/2-h-)exp(−iH0t/-h-)exp(−iVt/2-h-) (called the “symmetric split operator” approximation). Then the exponential operators are evaluated in the representation in which they are diagonal (the coordinate representation for the potential and the momentum representation and internal eigenstates for the reference Hamiltonian H0). The majorcomputationaleffortisthatoftransformingbetween these two representations. For the scattering distance and its canonical momentum, this is typically done by Fast Fourier Transform, which scales as M log2M, where M is the number of grid points in the discrete Fourier transform. The other basis dependence is at most N2 (and can be as low as N3/2 in the rotating frame approach). The computational effort then scales more slowly with N than the time-independent method discussed above, but more rapidly with M. Also, one must do this at each time step untilthescatteringiscompleted.Toavoidhavingtofollow the continued time evolution of the portion of χ(t) that has already escaped the range of the interaction causing the scattering, one may analyze it for the scattering information and then absorb it beyond the analysis region with an NIP. Finally, the time-dependent method automatically yields scattering information at all energies suffiently contained in χ(0), and χ(t) automatically satisfies the proper scattering boundary conditions.
A particularly powerful and promising wave packet approachmakesuseofthefactthatwhilehavingaterm−i A, where A is a positive semi-definite function, added to the Hamiltonian absorbs the wave packet with a time history given by −i Aχ(t), if one records this time evolution information and changes the sign, +i Aχ(t) then constitutes a source that feeds the wave back into the region where A is nonzero. This makes it possible to decouple the dynamics in all regions that can be defined using appropriate dividing surfaces from transition state theory. We write the set of uncoupled regional time-dependent Schrodinger¨ equations as
	ih-- ∂χ r = (H − i Ar)χr,	(96)
∂t
	ih-- r,	(97)
	ih- 	=	χ , p = 1,..., K.	(98)
Here, χr(t = 0) is the initial packet; H is the full Hamiltonian, and Ar, Ap, p =1,..., K are the functions that determine in what regions of configuration space sinks and sources are located. The absorber −i Ar is located just beyond the dividing surface associated with the initial (reactant) arrangement (just inside the so-called “strong interaction” region, 2). The −i Ap are located just beyond the dividing surface associated with arrangement p, p =1,..., K (includingtheinitialarrangement).Then it is easily seen that the dynamics of χr occurs only in the reactant arrangement, up to just within the reactant dividingsurface.Thedynamicsofχ2(t)occurssolelywithinthe strong interaction region, until it is completely absorbed by the various −i Ap located just outside the respective p arrangement dividing surface. The dynamics of the χp wave packet occurs solely in the region outside the pth dividing surface. We note that if we add all the equations, the result is
ih-  ,
(99)
so that the exact solution of the time-dependent Schro-¨ dinger equation is
K
	 .	(100)
Notice that while we must solve for χr(t) and χ2(t), they are nonzero for a shorter length of time than the total overall collision, and they are nonzero only in limited regions of configuration space. Therefore, computing them is much less work than solving for χ(t) directly and requires less storage. In addition, once we have recorded the time evolution of the −i Apχ2, p =1,..., K, we only need to solve for the final arrangements of immediate interest, and these are done completely separately (they are totally uncoupled between two regions p ). We can alsodothecalculationswhenevercomputingresourcesare most available and least costly. We also can use whatever coordinates are optimum in each separate region p. We pointoutthatatime-independentversionofEqs.(96)–(98) has been developed which appears very robust. Essen-
tially, it results from a half Fourier time-to-energy transform of Eq. (95), to yield [in analogy with Eq. (14)]
i
	(E  ,	(101)
or in causal solution form,
i
	.	(102)
Note that ξ+(E) is not the usual definite energy, causal solution of the Schrodinger equation (known as the¨ Lippmann-Schwinger scattering solution). However, in certainwell-definedregionsofconfigurationspace[namely, on the “target side” of the initial wave packet, χ(0)], it is proportional to the Lippmann-Schwinger solution,
	+(E), satisfying
		k+(E) = φk(E) +	 − 1 +	Vφk(E).	(103)
	E	H	i
Here,φk(E)isthesolutionoftheunperturbedSchrodinger¨ equation,
where, as usual,	H0φk(E) = Eφk(E),	(104)
	H = H0 + V,	(105)
with V being the interaction responsible for causing the scattering. If we express χ(0) in terms of the complete set {φk(E)},
	 ,	(106)
	C ,	(107)
	 .	(108)
One then finds that on the target side of χ(0), in configuration space,
+	mC(k)	+	.	(109) h2k
In general, if there are internal degrees of freedom and different possible chemical arrangements, one obtains
 
	ξrnr (E) =	-h-2knr	rknr (E),	(110)
whereCr(knr )characterizestheinitialpacketlocatedinarrangementr,withinitialinternalquantumnumbers-h2kn2r nr and relative kinetic energy  2m , and	rk+nr (E) is the complete Lippmann-Schwinger solution, including all possible final arrangements. The state   can be similarly split into
r localized pieces satisfying uncoupled time-independent dynamical equations analogous to Eqs. (96)–(98).
A particularly convenient observation is that, just like the homogeneous Schrodinger equation, a variational ex-¨ pression for the S matrix at energy E can be derived, based on Eqs. (101), (102), and (110). The result for a general scattering amplitude, connecting state r,nr at total energy E with final state p,n p at energy E is the robust expression
 
The modulus squared of this S matrix element is the probability of the indicated state-to-state process, and χ(pn p |t =0) is a wave packet located in the product region of configuration space, outside the collision region. Clearly, this is equal to a known factor times χ(pn p . It should be clear that knowledge of the full Green function, 1/(E − H  ), provides all one needs to know to calculate the state resolved S matrix element at the energy E.
It is worthwhile to examine how one can implement Eq. (111) computationally. A particularly effective way to do this is to expand 1/(E − H ) in an appropriate polynomial basis. A popular one is the Chebychev polynomials, denoted Tn. However, they require an argument bounded by ±1, while the exact spectrum of H is unbounded. However, in practice, one introduces a finite dimensional matrix representation of H, and this can be normalized so that it possesses no eigenvalues larger in magnitude than 1. This leads to an expansion of the form
1  	gn+(Enorm)Tn(Hnorm),	(112)
	E − H + i	n
where −1≤ Enorm ≤+1; a similar bound holds for the eigenvalues of Hnorm; and gn+(Enorm) is a simple, analytically known function that explicitly builds in the causal behavior of G+(E). Computation of the S matrix then requires evaluating
 t = 0)
	 (Enorm)Tn(Hnorm)χ(rnr |t = 0).	(113)
n
Note that all of the dependence on the energy E is contained in the analytical coefficients, gn+. Defining “Krylov vectors”
	ηn ≡ Tn(Hnorm)χ(rnr |t = 0),	(114)
we note that they are totally independent of E, and
	t  g+(Enorm)ηn.	(115)
n
Therefore, once the {ηn} are calculated that have nonzero overlap with χ(pn p |t =0), one has all the information needed to compute the S matrix elements at any other energy E contained in the initial packet. The Tn satisfy a simple recursion relation, so that
η0 = χ(rnr |t = 0),	(116)
η1 = Hnormη0,	(117)
	ηn = 2Hnormηn−1 − ηn−2, n ≥ 2.	(118)
Ifoneincludesanyabsorbingpotentials,thentherecursion is modified by an additional damping factor. Clearly,
n
Spn pknrnrknr
	pC	p
	 (Enorm)	.	(119)
n
We also remark that one can easily derive a similar Chebychev expansion of exp(−iHt/-h-)χ(0). Then the gn+ are replaced by analytical functions of time, but exactly the same ηn appear as in the energy dependent Green function expansion. The bottom line is that results are obtained with virtually no additional effort for any energy sufficiently contained in the initial packet. Note also that if one uses the same expansion for G+(E) in Eq. (103) for the scattered wave portion of the Lippmann-Schwinger solution, one obtains η˜n(E)≡ Tn(Hnorm)Vφk(E), which must be recalculated at every new energy!
C. Rigorous Quantum Transition State Theory
The above discussion shows, as one might have expected, that knowledge of G+(E) is tantamount to having solved, subject to causal boundary conditions, the Schrodinger¨ equation for any possible initial and final states and arrangements. This suggests that G+(E) cannot only yield state-to-stateprobabilityamplitudes,butalsothesumover all possible initial states in arrangement r and all possible final states in product arrangement p, denoted as Npr(E). Thisquantityisknownasthe“cummulativereactionprobability,” and it is central to an arbitrarily accurate, rigorous quantum transition state theory. This should also not be surprizing in light of the fact that by use of absorbing potentials located at various dividing surfaces, one can isolate the dynamics occurring in the strong interaction region. One then expects that the total strong interaction Green function for Eq. (97),
G 	(120) E   A j
should be able to provide Npr(E) without having to carry out any dynamics outside of region 2. This has indeed been proved to be true, and it is found that
Npr(E) = trace ApG2 Ar 
	= tracePpr(E),	(121)
where arrangement r can be any possible initial arrangement, p can be any possible final arrangement, and one computes the trace of the matrix product. The matrix Ppr(E) is Hermitian, and its eigenvalues are interpreted as probabilities of reaction to all possible final p states from all possible initial r states. The matrix elements can be computed using any convenient, sufficiently complete basis and need not have any relation to asymptotic states in any of the arrangements. This provides a rigorous quantum transition state theory.
SEE ALSO THE FOLLOWING ARTICLES
ATOMIC AND MOLECULAR COLLISIONS • COLLISIONINDUCED SPECTROSCOPY • ELECTRON SPIN RESONANCE
• INFRARED SPECTROSCOPY • KINETICS (CHEMISTRY) • LIGAND FIELD CONCEPT • MICROWAVE MOLECULAR
SPECTROSCOPY • QUANTUM MECHANICS • QUANTUM
THEORY
BIBLIOGRAPHY
Bader, R. (1970). “An Introduction to the Electronic Structure of Atoms and Molecules,” Clarke, Irwin, and C., Toronto.
Daudel, R., Pullman, A., Salem, L., and Veillard, A., eds. (1980, 1981, 1982). “Quantum Theory of Chemical Reactions,” Vols. I–III, Reidel, Dordrecht.
Dirac, P. A. M. (1958). “Quantum Mechanics,” Oxford Univ. Press, London.
Schatz, G. C., and Ratner, M. A. (1993). “Quantum Mechanics in Chemistry,” Prentiss Hall, Englewood Cliffs, NJ.
Simons, J., and Nichols, J. (1997). “Quantum Mechanics in Chemistry,” Oxford Univ. Press, New York.
Wyatt, R. E., and Zhang, J. Z. H., eds. (1996). “Dynamics of Molecules and Chemical Reactions,” Dekker, New York.
 
 
Quantum Chromodynamics
(QCD)
Taizo Muta
 
Hiroshima University
I. Why is QCD Needed? A Historical Survey II. Principles of QCD
III.	General Framework of QCD. PerturbativeRegime
IV.	Physical Applications
GLOSSARY
Baryon Type of hadron. The baryon family includes the proton, neutron, and other particles whose eventual decayproductsincludetheproton.Baryonsarecomposed of three-quark combinations.
Boson A particle that obeys Bose–Einstein statistics and has zero or integral spin. Unlike fermions, bosons are not conserved in number. They can be generated or destroyedsingly,ratherthaninparticle–antiparticlepairs.
Fermion A particle that obeys Fermi–Dirac statistics; a half-integer-spin particle.
Feynman diagrams Schematic representations of mathematical expressions for predicting the interaction of particles, in which lines represent the path of a particle and vertices represent particle interactions.
Gluon A massless particle that carries the strong force from one quark to another. Gluons can also interact amongthemselvesandformparticlesconsistingofonly gluons bound together (glueballs).
Hadron Any particle of the largest family of elementary particles; they interact with each other through strong interactions, usually produce additional hadrons in a collision at high energy, and are roughly spherical.
Lepton Member of the family of weakly interacting particles, which includes the electron, muon, tau, and their associated neutrinos and antiparticles. Leptons are acted upon not by the strong force, but by the electroweak and gravitational forces.
Singularity A point in space-time where the space-time curvature becomes infinite.
 	319
THE STRONGinteractionwasdiscovered in early1930s as nuclear forces which bind the nucleons together to form nucleus. Since then it has been a major research subject to explore the theory of strong interactions. In 1947 the first meson, the pion, was discovered experimentally as the mediator of nuclear forces. Through the 1960s the number of “elementary particles” including nucleons and mesons increased rapidly. Those elementary particles associated to strong interactions were called hadrons. In 1964 Gell-Mann and Zweig proposed that hadrons are composed of quarks. It was then natural to look for the dynamics obeyed by quark systems as the origin of strong interactions.
I. WHY IS QCD NEEDED?
A HISTORICAL SURVEY
In order to obtain experimental information on quark dynamics it seems to be the most sensible to probe the inside of hadrons by applying a beam of structureless particles (i.e., leptons). For the study of the hadronic structure we needmuchhigherenergiesandlargermomentumtransfers to obtain higher resolution. The first series of such experiments to probe the structure of the proton was initiated in the 1960s at SLAC (Stanford Linear Accelerator Center) and the process was called deep inelastic electron–proton scattering. In 1969 Bjorken reported the scaling property of the structure functions in deep inelastic electron– nucleonscatterings.ThisscalingiscalledBjorkenscaling, for which it is claimed that structure functions in the deep inelastic region depend only on the ratio q2/ν rather than on two independent variables q2 and ν, where q2 and ν are the 4-momentum transfer squared and energy transfer of electrons, respectively.
Bjorken scaling implies that the constituents of hadrons look almost free and pointlike deep inside the nucleon when observed with high spatial resolution. These free, pointlike constituents were named partons. If one accepts the parton idea, the dynamics governing the parton system should have the property that the interaction between partons becomes weaker at shorter distances. The partons were later identified with quarks since experimentally it wassuggestedthattheirquantumnumberssuchascharges and spins were practically the same as those of quarks.
Right after the proposal of the parton model all the known quantum field theories were surveyed as possible candidates for quark dynamics. Almost all of them were shown not to enjoy the above-mentioned property that the interaction between quarks gets weaker at short distances. The exception was the non-Abelian gauge field theory, which was originally introduced by Yang and Mills. ’t Hooft, Gross, Wilczek, and Politzer found that the non-Abelian gauge field theory satisfied the desired property, which is now called asymptotic freedom. Soon after it was shown that non-Abelian gauge field theory was the only theory which exhibited the asymptotic freedomamongtheknowntheoriesinfour-dimensionalspacetime. Therefore the dynamics governing quark systems is to be found among non-Abelian gauge field theories. The non-Abeliangaugefieldtheoriesaregeneratedbysymmetries described by a noncommutative algebra. This means that quark systems are required to have an extra symmetry associated with the non-Abelian gauge field. In the meantime three facts suggested that quarks must have a new quantum number called color and exhibit the color symmetry. We discuss these observations below.
A. The Problem of Constructing the Baryon Wave Functions
As an example, we consider the pion–nucleon resonance ++,whichisofspin3/2andismadeofthreeu-quarks.If weconsiderthe J3 =3/2statewith J3 thethirdcomponent of the total angular momentum for the ++ system, we find that all three u-quarks must have spins aligned up since relative orbital angular momentum are required to vanish for the lowest state in three-quark systems. Thus ++ state with J3 =3/2 is given by
	 	,	(1)
where the arrow represents the spin aligned up. But this assignment is not acceptable because it contradicts the Pauli exclusion principle, according to which fermions cannot occupy the same state.
A possible way out of this difficulty may be to consider higher orbital angular momenta for the quarks. This, however, spoils the success in the prediction of baryon magnetic moments based on the S-wave three quarks. Hence we prefer to keep quarks in S-states. Then we are forced to assume the exixtence of hidden degrees of freedom for quarks, color, in order to distinguish three quarks which are otherwise identical. We need at least three different colors to discriminate these three quarks. It is then easy to construct the totally antisymmetric state for ++ in place of Eq. (1),
 , (2)
where indices	εijk is the totally antisymmetric tensor (the repeated indices are summed). The same argument applies to other brayon states and the difficulty is now circummvented with the introduction of the extra color degree of freedom for quarks. Since we do not observe the color degrees of freedom directly, we may assume that hadronic phonomena are unaltered under the exchange of colors. The symmetry group corresponding to the color degrees of freedom may be chosen from the Lie groups and we adopt SU(3) for the color symmetry. A single quark state is then assigned to the fundamental triplet, 3, of SU(3). The state (2) is then a singlet, 1, of SU(3).
B. Nonobservation of Isolated Quarks
Sincewehavenoexperimentalevidenceofhadronswhich carrycolorquantumnumbersinanexplicitmanner,inconstructing the hadronic state out of quarks we have to pick out a singlet representation in the decomposition of the product of three triplets into irreducible representations,
i.e.,
3 ⊗ 3 ⊗ 3 = 1 ⊕ 8 ⊕ 8 ⊕ 10,
for the baryon state, and
3 ⊗ 3∗ = 1 ⊕ 8,
for the meson state. In analogy with Eq. (2), the meson color singlet state is taken to be
	 .	(3)
The fact that color is not directly observable can be stated in a different way: physical phenomena are invariant under the color transformation. Hence the color SU(3) has to be an exact symmetry. According to this principle, all hadronsarerequiredtobeinthesingletofthecolorSU(3). Other states with explicit color degrees of freedom are color nonsinglets and should not be explicitly observed. It is worth noting that among the many low-lying configurations of quarks, only qq¯ and qqq states can belong to the color singlet. Thus, the postulate of the nonobservability ofcoloredstatesisessentiallythesameasthatofthequark confinement, which requires that quarks be confined to the inside of hadrons and are not observed as isolated states. It should be noted that this postulate is just a kinematical constraint to eliminate colored states. There is, however, a hope that quark confinement may be a natural dynamical consequence of the strong interaction.
C. Discrepancy between Prediction and Experiment on Decay Rates for π0→2γ and Total Cross Sections of e+e−→Hadrons
The total decay rate of π0 →2γ can be calculated through the lowest order Feynman diagrams, and is obtained as
		  , (4)
2 π
where Nc is the number of color degrees of freedom, Qu and Qd are the u- and d-quark charges in units of the proton charge e, mπ0 is the neutral pion mass, α = e2/4π, and Fπ is the pion decay constant for π →µν decays (Fπ =91 MeV). Substituting Nc =3, Qu =2/3 and Qd =−1/3 we have (π0 →2γ)=7.6 eV, which is in perfect agreement with the experimental data (exp)=7.48±0.33 eV. Note that the theoretical prediction with Nc =1 (no color degree of freedom), (π0 →2γ)=0.84 eV, is far from explaining the data.
For e+ +e− annihilations at very high energies the total cross section σ(e+e− →hadrons) is given by
Nf
	σ(e+e−	hadrons)Nc	Q2, (5)
	→	3s	i=1	i
where s is the center-of-mass total energy squared of the e+e− system, Qi isthechargeoftheithquark,and Nf isthe number of flavors of quarks which may contribute to the process.ComparisionofEq.(5)withthedatastronglysupport Nc =3. If there is no color degree of freedom, the prediction of Eq. (5) is much smaller than experimental data.
These facts strongly support the idea that quarks should have an extra quantum number, color. In 1970s the idea of the extra quantum number, color, for quarks was established and the theory of quark dynamics was found to be a non-Abelian gauge theory with SU(3) symmetry that was named quantum chromodynamics (QCD).
The non-Abelian gauge field in QCD mediates color interactions between quarks. It is called the gluon. Gluons carry color charges and hence interact with each other even in the absence of quarks. This property of gluons is an essential ingredient for having asymptotic freedom. When one considers massless gluons, serious infrared divergences exist in QCD and may be the origin of quark confinement. The QCD has the property of the asymptotic freedom at short distances, while it has the possibility of quark confinement at long distances.
According to the property of asymptotic freedom of QCD, one may safely use perturbation theory to discuss short-distance processes. This approach in QCD is usually referred to as perturbative QCD. Perturbative QCD has been applied to many physical processes with the help of operator product expansion (OPE) and renormalization group equations, such as electron–nucleon scattering, e+e− annihilation, heavy quarkonia (J/ψ’s and ϒ’s) decays, photon–photon scattering as a subprocess of e+e− →e+e−X (X represents unobserved hadrons), production of jets from quarks and gluons, the Drell– Yan process NN →l+l−X, inclusive e+e− annihilation e+e− →hadrons+ X, large-pT hadron reactions, and multijets in e+e− annihilations. These applications, together with the later analysis of further experimental data, gave strong support to QCD.
II. PRINCIPLES OF QCD
QCD is a gauge field theory, which is based on the gauge principle. The gauge principle is the requirement that the theory be invariant under the local gauge transformation.
The symmetry group in QCD is the color SU(3) group, whichisanoncommutative(non-Abelian)group.Agauge theory which is invariant under the non-Abelian gauge group is also called Yang–Mills theory.
We consider the fermion ψ(x) with mass m (the quark field, to be more specific) which belongs to the Ndimensional fundamental representation of the group G. Thus the field ψ(x) has N components: ψi(x), i = 1,2,..., N.ThegroupGinQCDisthecolorSU(3)group and so N =3. The Lagrangian for the free fermion field ψ(x) is given by
	 .	(6)
The Lagrangian is invariant under the transformation
	 j, U = exp(−iT aθa),	(7)
whereθa (a =1,...,8)arethetransformationparameters and T a are the SU(3) generators, which are subject to the commutation relations
	[T a, T b] = i f abcT c,	(8)
where the summation on the repeated indices should be understood as usual and f abc are the structure constants of the SU(3) group. For θa depending on x, the Lagrangian (6)isnolongerinvariantunderthetransformation(7).The Lagranian may be made invariant under the non-Ablian local gauge transformation (7) if the derivative in Eq. (6) is replaced by the covariant derivative,
	Dµ = ∂µ − igT a Aaµ,	(9)
where Aaµ are the gauge fields and g is a constant representing the coupling strength between ψ and Aaµ. In component form Eq. (9) reads
	(Dµ)ij = δij∂µ − igTija Aaµ,	(10)
where Tija is the representation of T a in the fundamental representation. We now replace the Lagrangian (6) by
 i
µ
Dµ(11)
ThenewLagrangian(11)isinvariantunderthenon-Ablian local gauge transformation (7) provided Aaµ(x) obeys the transformation rule
T a Aµa = UT a Aaµ  
We now show that the Lagranian (11) is invariant under the local gauge transformation. Note that   igT a A 
 T aU A 
Because Aaµ satisfies the transformation rule (12), we have  .	(14)
Thus ψ¯ Dµψ is invariant under the non-Abelian local gauge transformation (12) and hence the Lagrangian (11) is also invariant.
The Lagrangian (11) describes the fermion ψ(x) in interaction with the gauge fields Aaµ(x). It is still to be supplemented by a kinetic term consisting purely of the gauge fields Aaµ(x). Inspired by the example of electrodynamics, we may try the form
 . (15)
However, such a term is not SU(3) gauge invariant. It is not difficult to prove that Fµνa Faµν is invariant with
	Fµνa  gf abc AbµAcν.	(16)
Finally we arrive at the general form of the Lagrangian which is invariant under the non-Abelian local gauge transformations (7) and (12),
	  Fµνa Faµν µDµ	(17)
4
ItshouldbenotedthatintheaboveLagrangianthereexists only one arbitrary parameter g owing to gauge invariance. This universal constant g is called the gauge coupling constant. We derived the above Lagrangian based on the gaugeprinciple.OfcourseitshouldstillbeLorentzinvariant and invariant under space and time reversal. Unfortunately, the Lagrangian (17) is not unique, in that we may add to it other terms of higher power of Fµνa and ψ within the requirement of local gauge invariance, Lorentz invariance, and invariance under space inversion and time reversal. The additional requirement of renormalizability may eliminate all the irrelevant terms and fix the Lagrangian (17) in a unique way.
After fixing the Lagrangian we are ready to move on to the quantization of the theory under consideration. The quantization can be conveniently performed in the Feynmanfunctional-integralformalism.Forsimplicityweconsider a system consisting only of a neutral scalar field φ(x) withmassm.TheGreenfunctionisgivenbythefunctional integral
 , (18)
where S is the classical action,
	S .	(19)
Here L is the classical Lagrangian density:
	 ,	(20)
with V(φ) the part of the Lagrangian representing the selfcoupling of the field φ. The Green function (18) may be reexpressed in another form if we introduce an external source function J(x) and an artificial source term φ(x)J(x) in the functional integral,
Z . (21)
Here Z(J)isafunctionalof J(x).Wedefinethefunctional differentiation by
	− y)] −	[J(x)]
.
	δJ(y)	ε→0	ε
(22)
According to the above definition, we have δn Z[J]
 .
(23) Hence we obtain
 .
The functional integral Z(J) thus generates all the Green functions. In this sense Z(J) is called the generating functional for Green functions.
A straightforward application of Eq. (21) to the case of gauge fields suggests that the generating functional for gauge fields Aaµ is given by
Z  AaµJaµ 
where L is given by Eq. (11) and [A] is the shorthand notation for
	 .	(26)
µ,a
In Eq. (25), L and [A] are gauge invariant. The action
S is also gauge invariant. In the following we set A µ Aµ a in order to emphasize its dependence on θa. Starting with a fixed Aaµ, we obtain a set of Aµ(θ)a by applying to Aaµ all the transformations U(θ) belonging to group G. According to the above invariance, the action S is constant for all A(µθ)a in this subset and the functional integral Z[0] on this subset of A(µθ)a diverges, as the region of the integral is infinite. Hence it is sensible to integrate only once on such A(µθ)a that belongs to the subset and to factor out a divergent constant. After this mamipulation is done with the following restriction on Aaµ,
	GµAaµ = Ba,	(27)
we have an expression for Z[J],
Z[J] = GµAaµ(x) − Ba 
a,x
	  AaµJaµ.	(28)
Since Ba(x) is arbitrary, we may average Z[J] over Ba(x) in the sense of the functional integral, i.e., we integrate Z[J] on Ba(x) with a suitable weight, which we choose to be
	 ,	(29)
where α is an arbitrary constant. Hence we obtain
Z  MG
 GµAaµ  AaµJaµ.
(30)
In this way we succeeded in exponentiating the constraint. The resulting exponent is the so-called gauge-fixing term with gauge parameter α. The following are examples of explicit expressions for the matrix MG:
1.	Coulomb gauge Gµ =(0,∇): (MG(x, y))ab = (δab∇2 − gf abcAc ·∇)δ4(x − y). (31)
2.	Lorentz (covariant) gauge Gµ =∂µ:
  gf abc 
3.	Axial gauge Gµ = nµ (here nµ is a spacelike constant 4-vector):
(MG(x, y))ab = (δabn ·∂ − gf abcn · Ac)δ4(x − y). (33)
4.	Temporal gauge Gµ =(1,0,0,0):
  gf abc A . (34)
With the generating functional Z[J] given by Eq. (30) the quantization program for gauge fields is completed.
The functional-integral quantization has been successfullyperformedforscalarandgaugefieldsinEqs.(21)and (30). The case of fermion fields needs special care and the quantization is performed by the use of the Grassmann number, which is a set of anticommuting numbers ψj (j =1,..., N),
	{ψi,ψj} = 0.	(35)
Thus the generating functional including fermion fields is
Z[J,η,  MG
 
	+ AaµJaµ ,	(36)
where η and η¯ are anticommuting source functions for fermion fields ψ¯ and ψ, with ψ¯ =ψ†γ0. According to the anticommuting property of fermion fields and source functions, we have to pay special attention to the sign associated with η(x) when we define fermion Green functions. For example, the fermion two-point Green function should be defined in the following way:
 
(−
.
	J=η¯=η=0	(37)
This rule of doing the functional differentiation with −η(x) should always be kept in mind in defining fermion Green functions.
The following formula for the integral over a Grassman algebra will be useful in the following, where A(x, y) is a certain complex function:
 .
III. GENERAL FRAMEWORK OF QCD. PERTURBATIVE REGIME
A. Perturbation Theory
In order to develop the perturbation theory it is most convenient to use the covariant gauge. In this case, however, det MG given by Eq. (32) depends on Aaµ and also on the gauge coupling constant g and hence a simple perturbative expansion of Eq. (36) is not allowed. For this purpose we need to exponentiate det MG and regard it as a part of the effective Lagrangian. Up to an irrelevant factor, det MG is represented by, according to Eq. (38),
 
	 ,	(39)
where MG is given by Eq. (32) and χa(x) is a complex fictitious field obeying the Grassmann algebra and belonging to the adjoint representation of the gauge group G=SU(3). The field χa(x) is called the Faddeev–Popov ghost, as it has the strange property that it is fermonic as well as bosonic. The exponent of the integrand in Eq. (39) can be rewritten by doing an integration by parts such that
 
	 ,	(40)
where Dµab is the covariant derivative in the adjoint representation [note that (T a)bc =−i f abc],
	Dµab = δab∂µ − gf abc Acµ.	(41)
We insert Eq. (39) together with Eq. (40) into Eq. (36) to obtain the generating functional
Z[J,ξ,ξ 
 
	 ,	(42)
where ξa and ξa∗ are source functions (Grassmann numbers) for the ghosts, and AJ,χ∗ξ, and ξ∗χ are shorthand notations for
AJ = AaµJaµ, χ∗ξ = χa∗ξa, ξ∗χ = ξa∗χa. (43)
HereLisaneffectivequantumLagrangianwhichincludes the effect of det MG,
	L = LG + LGF + LFP + LF,	(44)
  Fµνa Faµν,
	Fµνa  gf abc AbµAcν,	(45)
	 ,	(46)
b
	,	(47)
	µ	ij
	Dµ.	(48)
The indices on the Lagrangians (45)–(48) stand for “gauge,” “gauge fixing,” “Faddeev–Popov,” and “fermion” terms, respectively. The Lagrangian (44) forms the basis of quantum chromodynamics.
In the following we will develop the perturbation theory of quantum chromodynamics and derive the Feynman rules for it. For this purpose we split up the Lagrangian (44) into a free part L0 and an interaction part L1,
	L = L0 + L1	(49)
with
	 ,	(50)
 
	 ,	(51)
	 ,	(52)
	 	(53)
As Eq. (52) is of the form of the Lagrangian for massless charged scalar fields, we recognize that the Faddeev– Popov ghost is bosonic although it is fermionic owing to its nature as a Grassmann number. The remaining part of the Lagrangian L after subtracting L0 is the interaction Lagrangian L1,
L1 = L1(Aa,χa,χa∗,ψ,ψ¯)
g abcbµ cν   f	A A
g2 abe cde a b cµ dν f f AµAν A A
− gf abc(∂µχa∗)χbAcµ + gψ¯T aγµψ Aaµ. (54)
Then Eq. (42) can be rewritten in the following form:
Z[J,ξ,ξ∗,η,η¯]
 
	× Z0[J,ξ,ξ∗,η,η¯],	(55)
where Z0 is a generating functional for free fields,
Z ,	(56)
Z 
Z0FP 
Z 
In order to obtain Z[J,...] perturbatively we first calculate Z0[J,...] for the gluon, Faddeev–Popov ghost, and quark, respectively. To do this we reexpress the free Lagrangian by doing an integration by parts,
  AaµK abµν Abν,
Kµνab  , (60)
	b	ab	ab
	, K	= δ ,	(61)
	LF = −ψψ, ¯	= −iγµ∂µ + m. (62)
If we denote the inverses of Kµνab, K ab, and  by Dµνab , Dab, and S, respectively, we have
 zKµλac  abgµνδ4 (x − y),
(63)
 zK ac(x − z)Dcb(z − y) = δabδ4(x − y), (64)
 
These functions Dµνab , Dab, and S are propagators of the gluon, Feddeev–Popov ghost and quark, respectively. Solving the conditions (63)–(65) for Fourier coefficients, we find
Dµνab (x) = δab ,
(66)
Dab(x) = δab x,	(67)
	S x.	(68)
We can now perform the functional integrations of Aaµ, χ, χ∗, ψ, and ψ¯ in Eqs. (57)–(59), respectively. We obtain, apart from irrelevant constant multiples,
Z yJaµ ,
(69)
Z0FP ,
Z 
We insert Eqs. (69)–(71) into Eq. (56) and use Eq. (55) to generate the perturbation series,
Z
(72)
We can calculate Green functions order by order with the use of Eq. (72). For example, we can calculate two-point Greenfunctions(propagator),three-pointGreenfunctions (vertex), etc. Accordingly we have the Feynman rules for the Lagrangian of QCD shown in Tables I and II.
	TABLE I	QCD Feynman Rules
Now that we have settled the Lagrangian for QCD and established the Feynman rules for it, we are free to make perturbative calculations of cross sections for an arbitrary quark–gluon process. In general, however, the loop contributions to quark–gluon processes generate divergences. The divergences are properly taken care of by the renormalization program which we will describe in the following.
Renormalization is a technique for subtracting the divergences appearing in the loop calculations. Before substracting these divergences the divergent integrals should 
TABLE II	Additional Rules for Transition Matrix Elements
 
Mass-shell condition	p2 = m2 for external lines
 
be made tentatively finite by introducing a suitable convergence device. This procedure is generically called regularization. Regularization is a purely mathematical procedure which has no physical consequences; accordingly, it is not a unique procedure. We have a variety of the regularization schems, such as (1) the cutoff method, (2) thePauli–Villarsregulatormethod,(3)analyticregularization, (4) lattice regularization, and (5) dimensional regularization. Since in dimensional regularization the regularized theory is kept Lorentz invariant, gauge invariant, and unitary, in this sense dimensional regularization is the most suitable for gauge theories. We will present this method in this article.
In order to explain the dimensional regularization scheme, we take a specific example of a divergent integral, the quark self-energy part ij(p). Its relation to the quark propagator S˜ij(p) is given by
	S˜ij .	(73)
Following the Feynman rules for QCD, we can obtain an expression for the quark self-energy part to order g2
(see Fig. 1),
	2	4	γ
	(p)   g CF	(2π)4i k2(m2 − (p − )2)
TheaboveexpressionisobtainedinFeynmangaugeα =1, and CF =(N2 − 1)/2N, N =3. The four-dimensional integral in Eq. (74) is linearly divergent, as can be easily seen by simple power counting in k, i.e.,
k
 
	p	p  k	p
FIGURE 1
	lim K.	(75)
K→∞
The divergence comes from the high-momentum region |k|→∞. This divergent integral may be made convergent by reducing the number of multiple integrals. For example, Eq. (74) would be finite if the space-time were two dimensional.Thisfactisthebasicideaofdimensionalregularization. Where we keep the space-time dimension D lowerthanfourandreplacethedivergentfour-dimensional integral by a convergent D-dimensional one. By making momentum integrations explicitly, we obtain an analytic expression as a function of the dimension D. We make the analytic continuation in D in this expression. Then the original divergence will show up as a pole at D =4 in the above analytic expression.
We summarize the convensions for dimensional regularization here:
1.	The D-dimensional space-time has the metric gµν = (+,−,...,−).
2.	Tr[I]=4 in the space of the gamma matrices.
3.	The integral measure is .
4.	γ5 is an object which satisfies {γ5,γµ}=0.
It is worth noting here that the gauge coupling constant g is no longer dimensionless for arbitrary space-time dimensions, dim[g]=2 − D/2. Thus we introduce a mass scale µ by hand and rewrite the gauge coupling constant g in the following way:
	g = g0µ2−D/2,	(76)
where g0 is the dimensionless gauge coupling constant. We can finally obtain the expression for the quark selfenergy part in D-dimensional space-time for the covariant gauge with α arbitrary,
 B
  O(ε),
(77)
where we defined a new parameter ε by ε =(4 − D)/2. We can find that there is a ploe in Eq. (77) which is relevant to the condition when the arbitrary dimension D is four.
In the renormalization program divergences in Green functions are subtracted by redefining the fields, the coupling constant g, and the mass parameter m in the original Lagrangian. It is important to note here that the way of elimintingdivergencesinperturbationtheoryisnotunique becausethereexistsanambiguityindefiningthedivergent piece of the Green function. This ambiguity eventually leadstoambiguityinthefinitepieceoftheGreenfunction. In order to remove this ambiguity, we have to specify how we define the divergent piece which will be subtracted out in the renormalization process. The prescription for subtracting divergences in Green functions is called the renormalizaion scheme. The scheme in which we eliminate only the pole term 1/ε in the dimensionally regularized expression of the Green functions is called minimal subtraction (MS). We see in Eq. (77) that the pole term is usually accompanied by the natural constant γ and ln4π in the combination 1/ε −γ + ln 4π, thus the scheme to eliminate the whole of 1/ε −γ + ln4π is called modified
 
minimal subtraction (MS).
The basic Lagrangian for QCD is given in Eq. (44). It is more convenient to rewrite the FP ghost term in the form
	 .	(78)
Hence the QCD Lagrangian is taken as
  Fµνa Faµν  
	µ	ij
Dµ
The above Lagrangian may be decomposed into a free and an interaction part, L0 and L1, such that
L = L0 + L1,	(80)
 
i
, (81)
 AbµAcν
g2 abe cde a b cµ dν f f AµAν A A
−igf abc . (82)
To eliminate the divergences in loop corrections to the
Greenfunctions,weredfinethefields Aaµ,χ1a,χ2a,andψ by
Aaµ = Z Araµ, χ1a,2 = Z˜31/2χ1a,2r, ψ r,
(83)
and the parameters g, α, and m by
g = Zggr, α = Z3αr, m = Zmmr, (84)
where the constants Z3, Z˜3, Z2, Zm, and Zg are called renormalization constants. Inserting Eqs. (83) and (84) into Eq. (79), we obtain
	L = Lr0 + Lr1 + LC,	(85)
where Lr0 and Lr1 are precisely equal to L0 and L1 if the quantities Aaµ,  , and m are replaced by the renormalized ones, Araµ,  r, gr, αr, and mr. Then LC is given by
 
i r
i	r
 gr f abc ArbµArcν
 gr f abe f cde AraµArbν ArcµArdν
 igr f abc r Arcµ
j	a
	r Arµ.	(86)
If we define four new renormalization constants by
Z1 ≡ Zg Z33/2, Z Zg Z˜3 Z31/2,
(87)
Z1F ≡ Zg Z2 Z31/2.
We can rewrite Eq. (86) in the form
 Arbν
 r
i r
i	r
 gr f abc ArbµArcν
 gr f abe f cde AraµArbν ArcµArdν
−(Z˜1 − 1)igr f abc r Arcµ
j	a
	A .	(88)
	r	rµ
The term LC is called the counter-term Lagrangian, and is used to subtract the divergences. The renormalization constants Z3, Z˜3, Z2, Zm, and Zg should be determined by adjusting the counter terms so as to cancel overall divergences appearing in higher order Feynman amplitudes.
B. Renormalization Group Method
According to the renormalization program, we substract all the divergences from the Green functions systematically order by order in perturbation theory. In the subtractionprocedurethereexistsanarbitrarinessofhowtodefine adivergentpieceinaGreenfunction,i.e.,howmuchofthe finite piece is to be subtracted together with the infinity. This arbitrariness results in a variety of renormalization schemes.Ontheotherhand,insubtractingthedivergences we inevitably introduce an arbitrary mass scale µ, which is called the renormalization scale. The renormalization scale µ is entirely arbitrary and remains in the finite part of the Green functions, thus leaving an arbitrariness for the renormalized Green functions after the subtraction of divergences.
Due to this arbitrariness we have many possible expressions for one physical quantity depending on the choice of the renormalization scheme and scale. These different expressions are connected by a finite renormalization. Since they describe a unique physical phenomenon and they have to be equivalent. In other words, physical quantities such as S-matrix elements are invariant under a finite renormalization.
The renormalized coupling constants gr and mr depend on the renormalization scale µ at which the subtraction procedure is defined. Writing this dependence explicitly, we have
gr(µ) = Zg(µ)−1g,
(89)
mr(µ) = Zm(µ)−1/2m.
The renormalized coupling constants gr(µ) and gr  which are obtained through two different subtraction procedures characterized by the renormalization scales µ and µ, respectively, are related to each other by
	gr ,	(90)
where the finite renormalization zg ) is given by
	zg .	(91)
In the same way we have
	mr (µ,µ)mr(µ),	(92)
where zg ) is defined by
	zm(µ,µ) .	(93)
Equation (90) defines a set of finite renormalization  for varying renormalization scales µ and µ. The finite renormalization (90) can be regarded as a transformation. This set of transformations possesses group properties. This group is Abelian. A similar property is possessed by , which is also an Abelian group. We have yet another kind of finite renormalization which applies to Green functions. For simplicity, let us consider here the truncated connected Green function for n gluon legs G˜ tcn (p, g,m), which is defined by
 (p, g,m)
 (x1,..., xn),
(94)
where Gcn(x1,..., xn) is the connected Green function given by
Gcn(x1,..., xn) = (, (95)
J=0
and W[J, g,m] is the generating functional for the connected Green functions, which is related to the generating functional Z[J, g,m] for the Green functions Gn through the relation
	Z[J, g,m] = eiW[J,g,m].	(96)
Since
	W[J, g,m] = Wr[Jr, gr,mr],	(97)
and J = Z3−1/2 Jr (note here the redefinition of J corresponding to the field redefinition Aaµ = Z Araµ), we find that the renormalized connected Green function Grnc (x1,..., xn) is related to Gcn(x1,..., xn) by
	Grnc  .	(98)
Defining the renormalized truncated connected Green function G˜ rntc (p, gr,mr,µ) through the equation
(2π)4δ4(p1 + ··· + pn)G˜ r2(p1)··· G˜ r2(pn)
× G˜ rntc (p, gr,mr,µ)
	xn)	c
Grn(x1,..., xn),
(99)
we obtain
G˜ rntc (p, gr,mr,µ) (p, g,m). (100)
We introduce the renormalized Feynman amplitude
Fn(p, gr(µ),mr(µ),µ)withrenormalizationscaleµsuch
that
Fn(p, gr(µ),mr(µ),µ)
	= −iG˜ rntc (p, gr(µ),mr(µ),µ).	(101)
The finite renormalization for Fn is then given by
Fn(p, gr 
= zn(µ (p, gr(µ),mr(µ),µ), (102)
where the renormalization factor zn ) is defined by
	zn .	(103)
Thus the change of the renormalization scale µ generates a finite multiplicative renormalization of the Feynman amplitudes which gives rise to an Abelian group
 .
We have obtained three sets of finite renormalizations  which constitute Abeliangroupsgeneratedbythescalechangeµ .The group thus obtained is called the renormalization group.
The transformations (90), (92), and (102) may be regarded as functional equations for gr(µ), mr(µ), and Fn(p, gr(µ),mr(µ),µ) characteristic of the renormalization group. If we restrict ourselves to an infinitesimal change of the renormalization scale µ, these functional equations reduce to differential equations which correspond to the Lie differential equations in the Lie group.
These differential equations are called renormalization group equations.
Now we derive the renormalization group equation in
 
the MS (or MS) scheme. We first derive the differential equations corresponding to the functional equations (90) and (92). We keep µ fixed in Eqs. (90) and (92) and differentiate both sides of these functional equations with respect to µ. It is, however, more convenient in the later practical calculations to start with Eq. (89) to obtain the same differential equations. We employ dimensional regularization. Then g and gr acquire mass dimension. We isolate these mass dimensions explicitly,
g  
(104)
ε grgRµ,
where ε =(4− D)/2 and g0 and gR are dimensionless coupling constants. Here the mass scale µ0 is fixed scale, while the mass scale µ for the renormalized coupling constant gr is a variable parameter. The mass scale µ is in fact identified with the renormalization scale in the MS (or
 
MS) scheme. Using Eq. (104), we rewrite Eq. (89) in the following form:
	gR g0.	(105)
The bare parameter g and m are regarded as fixed constants, hence we have
	dg	dm
	0,0.	(106)
	dµ =	dµ =
According to Eq. (105), we obtain, from (106), the differential equations for the renormalized parameters gR and mR,
dgR
µ= β	(107) dµ
dmR
µ= −mRγm,	(108) dµ
where we have rewritten mr as mR, i.e., mR =mr, just to balance the notation, and β and γm are given by
µ dZg
	β = −εgR −  gR,	(109)
Zg dµ
	 m	Zm1/2	dµ .	(110)
The quantities β and γm defined here are finite functions of µ since the divergences in Zg and Zm as ε →0 cancel out in expressions (109) and (110).
We now turn our attention to the differential equation corresponding to the functional equation (102). We note that the unrenormalized n-point Green function  tc
Gn (p, g,m) defined in Eq. (94) is independent of the renormalization scale µ as far as the bare parameters g and m are fixed, i.e.,
d	˜ tc(p, g,m)|g,m = 0.	(111) Gn
dµ
In terms of the renormalized n-point Green function definedbyEq.(100),wereexpressEq.(111)inthefollowing way:
	d	−n/2Fn(p, gR(µ, g,m),
(µ, g,m) dµ
	×mR(µ, g,m)		.	(112)
Applying the chain rule in differentiation to Eq. (112), we obtain
Fn + Z3−n/2
g,m
	Fn	= 0. (113)
g,m
Rewriting Eq. (113), we have
 Fn = 0, (114)
where β, γm, and γ are defined respectively by
	β = µ,	(115)
g,m
γm = −    ,	(116) µ
mR
µ ∂Z
	γ = −.	(117)
g,m
It should be mention that in the MS scheme β, γm, and γ depend only on gR:
β = β(gR),	(118)
γm = γm(gR),	(119)
γ = γ(gR).	(120)
Equation (114) together with Eqs. (118)–(120) constitute the renormalization group equation for the Green function Fn in the MS scheme. Equation (114) is called the ’t Hooft–Weinberg equation. The functions β(gR), γm(gR), and γ(gR) are called the renormalization group functions. In particular β(gR) goes by the name of the β-function or the Gell-Mann–Low function, and γ(gR) is called the anomalous dimension of the gluon field Aaµ.
Now we can easily generalize Eq. (114) to the truncated connected Green function FnG,nF with nG gluon and nF quark legs, and take the renormalized gauge constant αR into account. The generalized renormalization group equation reads
∂
	(gR,αR)	(gR,αR)mR  
	∂µ	∂gR	∂mR
+δ(gR,αR)  nGγG(gR,αR)
	−nFγF(gR,αR)FnG,nF = 0,	(121)
where gR = grµ−ε, g0 = gµ−0 ε, ε =(4−D)/2, mR =mr, and αR =αr. The renormalization group functions β, γm, δ, γG, and γF are defined by
	β(gR,αR) = µ,	(122)
g,m,α
µ ∂mR
γm(gR,αR) = − 	,	(123) m
δ(gR,αR)(gR,αR), (124)
µ
γG(gR,αR),	(125)
g,m,α
µ 
γF(gR,αR).	(126)
g,m,α
Here γG and γF are called the anomalous dimensions of the gluon and quark fields, respectively.
The renormalization group functions can be calculated order by order in quantum chromodynamics. The calculation of the β-function has been performed up to four loops in the MS scheme. Here we present the expression for the β-function up to three loops:
β(g) = −β0g3 − β1g5 − β2g7 + O(g9), (127)
where the βi are given by
 ,	(128)  ,	(129)
 
Now we introduce the running coupling constant g¯, which is the renormalized running coupling constant defined at the arbitrary renormalization scale µ, i.e.,
dg¯
µ  = β(g¯),	(131) dµ
If we reexpress the scale µ by a new scale t through the relation µ=et, the above equation becomes
dg¯
	β(g¯),	(132)
dt =
where the running coupling constant g¯ can be regarded as function of t, so that it should be expressed as g¯(t). The integrated form of Eq. (132) is given by
	t  .	(133)
We choose the momentum scale to be
	et  /µ,	(134)
where q is the typical momentum under consideration, which is taken to be spacelike, and µ0 is the fixed momentum scale. We insert Eq. (127) into Eq. (133) to obtain
t , (135)
where g = g¯(0). If we choose g sufficiently small, λ is also kept small since g¯ < g. Hence to this approximation we may safely truncate the perturbative series for the β-function. Keeping only the one-loop order, we have from Eq. (135)
	t  .	(136)
Hence the running coupling constant g¯ is given by
	g2	1
	 ,	(137)
where the new momentum scale  is defined by
	 .	(138)
The momentum scale  is often referred to as the QCD scale parameter and is the only adjustable parameter in QCD except for the quark masses. In fact, the free parameter g present in the original Lagrangian is replaced by the scale parameter  through Eq. (138). The scale parameter  should be determined by comparing the QCD predictions with experimental data.
From Eq. (137), we can see that asymptotic freedom occurs if β0 > 0. Equation (128) shows that the condition for the asymptotic freedom reads
Nf < 33/2.
Hence quantum chromodynamics enjoys the property of asymptotic freedom in so far as the number of quark flavors is less than 16. It should be noted that, for Nf =0, i.e., for a world made up only of gluons, the coefficient β0 is positive definite. It is the presence of quarks that can spoil asymptotic freedom. The fundamental origin of asymptotic freedom may be traced back to the existence of the three-gluon coupling term in the Lagrangian. As this term is peculiar to the Yang–Mills theory, we realize that asymptotic freedom is inherent in the nature of a Yang–Mills theory.
The formula (137) may be improved by taking into account the two-loop term, i.e., the term with the coefficient β1 in Eq. (135). Performing the integration, we obtain
t 
We rewrite (139) in the following form:
 , (140)
with the scale parameter  defined by
 = µe . (141)
Note that Eq. (141) reduces to Eq. (138) if we set β1 =0. Equation (140) may be solved for g¯2 iteratively provided that  ,
g¯  The second term in the parentheses in the above equation represents the next to leading order, which corresponds to the two-loop effect.
We find that the renormalized coupling constant tends to be small as the relevant momentum scale grows. According to this property of asymptotic freedom, we realize that our perturbative calculation is justified for the largemomentum scale. Thus, in QCD, perturbation theory is perfectly legitimate in the large-momentum region.
C. Operator-Product Expansion
Theproductoffieldsatthesamespace-timepointiscalled the composite field or composite operator. Strictly speaking, the composite operator field is not well defined if one takes a product of fields in a naive way. To make the argument simpler we shall confine ourselves to the case of the neutral scalar field φ(x).
Even for free fields we can see show that the composite operator is not well defined. Let us consider the timeordered product of two fields T[φ(x)φ(y)]. Its vacuum expectation value is the propagator of the free field φ(x) (times −i),
)
= −i
ε
As we let y → x in Eq. (143), we see that the momentum integral on the right-hand side diverges. Furthermore, not only for the vacuum expectation value (143), but also for general Green functions   onemayshowthatthedivergenceoccurs
as ˆ(yx→)φˆ(xy.)] Thusfor freethefields is not well decomposite	operatorfined. To seelimy→x
T[φ
the situation more clearly, we perform the momentum integration in Eq. (143) explicitly:
 
 , (144) iε
where K1(z) is the modified Bessel function of the second kind. The right-hand side of Eq. (144) is obviously divergent for x = y. In the case of free fields we may find a meaningful definition of the composition field φ(x)2 by subtractingthesingularityofitsvacuumexpectationvalue from the naive product of the field operators,
	:  ˆ	2 =
Thecompositeoperator:φˆ(x)2:definedinthiswayisnothingbutthenormalproductoffreefields.Fortheinteracting fields, this simple manipulation cannot be generalized in a straightforward manner.
For interacting fields we also have a simple argument showing that the composite operator φ(x)2 is ill defined. We take the vacuum expectation value of the composite operator φˆ(x)2 and find that
n
Here we have inserted between the two φˆ(x)’s the complete set of eigenstates   of the four-momentum op-
erator Pˆ µ,
	Pˆ ,	(147)
where n is a quantum number other than momentum p, labeling the eigenstates, and we have also used the translation invariance of the theory, φˆ(x) = ei Pˆ·xφˆ(0)e−iPˆ·x. (148)
The complete set of states  as a subset and hence
	 p, .	(149)
n
Here the matrix element in Eq. (149) depends only on p2 by covariance. In particular, the right-hand side of Eq. (149) is independent of pµ since p2 =m2 for the oneparticle state, where m is the mass of field φ(x). Therefore we have by combining Eq. (146) with Eq. (149),
d3p
 , p	,
|(2π)42p0
(150)
the right-hand side of which is divergent, and N =  p, . Thus the composite operator φˆ(x)2 in general gives rise to divergent matrix elements and is not a mathematically well-defined object.
The operator-product expansion proposed by Wilson mayservetogiveameaningfuldefinitionofthecomposite operator. By the operator-product expansion we mean that theproductofoperators,say Aˆ(x)and Bˆ(x),isexpandedin aseriesofwell-definedlocaloperators Oˆ i(x)withsingular c-number coefficients Ci(x) (i =0,1,2,3,...),
Aˆ(x)Bˆ(y) = , (151)
where Aˆ(x) and Bˆ(x) may be the field φˆ(x) or any other local operators. The local operator Oˆ i(x) is regular in the sense that the singularity of the product Aˆ(x)Bˆ(x) for y = x is fully contained in the coefficient functions Ci(x − y). In Eq. (151) we arranged each term in the order of decreasing singularity. Hence C0(x − y) is the most singular as y → x, the next most singular one is Ci(x −y), and so on. The operator Oˆ 0(x) is usually an identity operator. Thus the operator-product expansion serves as a means of defining the composite operator.
Now we shall derive the operator-product expansion of Eq. (151). We exemplify it in free field theories. One of the simplest examples of the operator-product expansion in free field theories is the Wick theorem applied to the time-ordered product of two free neutral scalar fields: T 
where :φ(x)φ(y): represents the normal product. Also, for free fermions we have
T 
As remarked before, the normal product of free fields may be used to define a composite operator, as it is regular even in the limit x → y. Defining the electromagnetic current jµ(x) by the normal product for the quark fields,
	jµ(x) =:ψ¯(x)γµψ(x):,	(154)
we derive the expansion of the product of two currents by applying the Wick theorem,
T[jµ(x)jν(0)]
 (155) Note here that for the free quark field ψ(x)
i x,
(156)
where S(x) is the free quark propagator. As is easily seen in the above equation, S(x) is singular for x →0. Since on the right-hand of Eq. (155) we have two S(x)’s in the first term, one S(x) in the second and third, and none in the fourth, we realize that each term on the right-hand side of Eq. (155) is arranged in the order of decreasing singularity for x ∼0. Equation (155) is clearly an example of the operator-product expansion (151).
The free quark propagator S(x) is related to the free neutral scalar propagator (x) defined previously in Eq. (143), i.e.,
	S .	(157)
The explicit form of (x) is given by Eq. (144). The leading singularity of (x) may be extracted from Eq. (144) and is found to be independent of the quark mass,
 less singular terms. (158)
The singularity lies on the light cone x2 →0 and so is called a light-cone singularity. It is important to note here that the more singular the behavior of (x) near the light cone, the larger the power of q2 in the Fourier transform sim (q) of (x). The following formula is a typical example of this property in the one-dimensional Fourier transformation: 2
qα−1. (159)
Hence it is enough for us to examine the most singular part of the c-number coefficients in Eq. (155) in order to see the dominant contribution of the current product to the matrix element of the physical reaction.
We extract the most singular part of Eq. (155) near the light cone by using Eqs. (157) and (158),
	2	2xµxν
T
 OVρ(x,0)
	xλ	ρ
+  2π2(x2 − iε)2 εµλνρOA(x,0)
	+ Oµν(x,0),	(160)
where OVρ(x,0), OAρ(x,0), and Oµν(x,0) are regular bilocal operators defined by
OVµ(x, y) = :ψ¯(x)γµψ(y) − ψ¯(y)γµψ(x):,	(161)
OAµ(x, y) = :ψ¯(x)γµγ5ψ(y) − ψ¯(y)γµγ5ψ(x):, (162)
Oµν(x, y) = :ψ¯(x)γµψ(x)ψ¯(y)γνψ(y):, (163) and σµλνρ is given by σµλνρ = gµλgνρ + gµρgνλ − gµνgλρ. (164)
It is important to note here that the operator-product expansion (160) provides us with a clear separation of the short-distance effects from the long-distance effects. In fact the singular c-number coefficients in the expansion characterize the short-distance behavior of the product of currents, while the regular bilocal operators include full information on the long-distance properties of the theory and are unimportant in the short-distance region.
We may transform Eq. (160) into a formula for the current commutator [jµ(x), jν(0)]. For this purpose we first note that
T[jµ(x)jν(0)] − T[jµ(x)jν(0)]† = ε(x0)[jµ(x), jν(0)],
(165)
where we took into account that current jµ is Hermitian, and ε(x0) is the sign function,
x0
	ε(x  ) = .	(166)
We then use the fundamental relation
	 ,	(167)
x2 − iε x2
where P denotes the principal part. Differentiating Eq. (167) n − 1 times with respect to x2, we have
 + iπ − δ − (x ), (168) (x2 − iε)nn (n − 1)!
where
dn
	(n)	22
δ (x ) =  δ(x ).	(169) d(x2)n
From Eq. (168) we immediately obtain
 1 − +1 = 2πi (−−1)n−1 δ(n−1)(x2). (x2 − iε)n (x2 iε)n (n 1)!
(170)
Using Eqs. (160), (165), and (170), we finally obtain the desired formula,
	i	2
(x )
 
	i	ρ
OA(x,0)
+ Oµν(x,0) − Oνµ(0, x). (171)
Now we apply the operator-product expansion to physical processes. Let us start with the application of Eq. (171) to the e+e− annihilation cross section. Using the standard method, the total cross section of e+e− annihilation can be expressed as
	e4	µν
	 l wµν,	(172)
where
	lµν  gµν,	(173)
wµν  
Here p1 (p2) is the momentum of the electron (positron), and q = p1 + p2. We insert Eq. (171) in Eq. (191). Since
OV , OA, and Oµν are of the form of a normal product, we realize that only the first term on the right-hand side of Eq. (171) contributes to wµν. Hence we have
	i	∂ ∂	∂ ∂
	wµν 	I3, (175)
where nonleading contributions are neglected and In is given by
	In  .	(176)
After some calculation, In is found to be
	iπ2	n−1
	Inε(q0)θ(q2),	(177)
where θ(q2) is the step function. We then obtain
	wµν .	(178)
SubstitutingEq.(178)intoEq.(186),weimmediatelyfind for the e+e− annihilation total cross section
4πα2
	σ =  .	(179)
3s
Intheaboveargumentwestartedfromtheelectromagnetic current given by Eq. (154) and so the quark was assumed to have unit charge, Q =1. If we had started form the electromagneic current of the form
	Nf	Nc
	jµ ,	(180)
with Nf quark flavors and Nc colors, we would have
obtained
	Qi2.	(181)
3s i=1
The above result is just the same as what is obtained from the parton model. Thus the free quark operator-product expansion(171)atshortdistancesisessentiallyequivalent to the parton model. This is in a sense quite reasonable becausethefirsttermoftheright-handsideof(171)comes from the first term of Eq. (155), which corresponds to the Feynman diagram depicted in Fig. 2. Taking the imaginary part of the Feynman amplitude corresponding to Fig. 2, we obtainthelowestordercontributionoftheelectromagnetic interaction to the e+e− annihilation total cross section. Hence we have the parton model prediction of the cross section.
IV. PHYSICAL APPLICATIONS
Equipped with the operator-product expansion and renormalization group method we are ready to apply perturbative quantum chromodynamics to physical processes dominated by short-distance effects. As typical examples
 
we deal with the total cross section of e+e− annihilations, deep inelastic structure functions, and hadron jet distributions in e+e− annihilations.
A. e+e− Annihilations
One of the simplest examples of the application of perturbativeQCDisfoundindeterminingtotalcrosssectionsfor e+e− annihilationprocesses.Letusconsidertheprocessin which a positron e+ and an electron e− annihilate through the electromagnetic interaction, producing a number of hadrons. Here, for simplicity, we do not take into account the weak interaction effect which may become significant in the energy region of the weak neutral boson Z0. The process of e+e− annihilation is written as
	e+ + e− → X,	(182)
where X represents the final hadron system. The corresponding Feynman amplitude is given by
 e 0,
(183)
where p1(p2)andλ1(λ2)arethemomentumandspincomponent of the electron (positron), respectively, with q the total momentum, q = p1 + p2; uλ(p) [ν¯λ(p)] is the Dirac spinor of the electron (positron) and jµ(x) is the quark part of the electromagnetic current.
Thetotalcrosssectionfortheannihilationprocess(182) can be written down as
  q) ,
(184)
where the electron mass is neglected and
	s = q2 = (q1 + q2)2.	(185)
Inserting Eq. (183) in Eq. (184), we ontain
	e4	µν
	σ =	 3 l wµν,	(186)
2s
where
	lµν  gµν,	(187)
wµν  (pX  j .
X
(188)
It is easily shown that wµν can be rewritten as
	wµν .	(189)
For the process e+ +e− → X to be physical, the total energy q0 of the initial state should be positive, and then we can show
	 .	(190)
With Eq. (190), Eq. (189) can be written in the form
	wµν .	(191)
Thus the total cross section for e+e− annihilation is expressed in terms of the current commutator. In the centerof-masssystem,wehaveq =(q0,0,0,0).Bearinginmind high-energyannihilations,weletq0 →∞andwefindthat only the region x0 ∼0 makes a major contribution to the integral (191) according to the Riemann–Lebesgue theorem. On the other hand, the integral (191) has a support only when x2 ≥0 due to the causality requirement, so that x0 ∼0 implies x ∼0. Hence we conclude that the total cross section for high-energy e+e− annihilations is governed by the current commutator at short distances.
For later convenience we further rewrite Eq. (186). The general tensor structure of wµν may be easily deduced following the requirements of Lorentz invariance and current conservation. We find that wµν is expressed in terms of only one invariant amplitude w(q2),
	wµν ,	(192)
where the extra factor 1/(6π) is attached for later convenience. Substituting Eq. (192) into Eq. (186), we have
	σ w(s).	(193)
3s
where α =e2/(4π). On the other hand, it is easy to show that the total cross section for the process
	e+ + e− → µ+ + µ−	(194)
in the lowest order of the electromagnetic interaction is equal to
4πα2
	σµν =  ,	(195)
3s
where the electron and muon masses are neglected. It is customary to define so-called the R ratio
R ,	(196) σµµ
to discuss the high-energy e+e− annihilation process. The R ratioiscloselyrelatedtothecurrentcommutatoratshort distances.Toshow,thisweuseEqs.(191),(192)and(196) to reexpress the R ratio as
R	  	jµ .	(197) q
We consider the e+e− annihilation at very high center-of-
masses are negligible compared with q2. Then R is mass energies (large q2) so that all the relevant quark
a function only of the center-of-mass energy squared, s =q2, the renormalized coupling constant g, and the renormalization scale µ,
	R = R(s/µ2, g).	(198)
Here the dependence of R on s and µ is given by the ratio s/µ2 for dimensional reasons.
The operator jµ in Eq. (197) is the electromagnetic current, which is conserved, and hence its anomalous dimension vanishes. Accordingly, the renormalization group equation for the R ratio reads
	 .	(199)
The general solution of Eq. (199) is easily found to be
	R ,	(200)
where the running coupling constant g¯(s) is defined in terms of the β-function such that
	 , g¯(µ2) = g,	(201)
∂t with t =(1/2)ln(s/µ2).
The meaning of Eq. (200) is obvious: the explicit s dependence of the R ratio computed by using the coupling g can be completely absorbed into the s dependence of the running coupling constant g¯(s). In asymptotically free field theories, the running coupling constant g¯(s) for large s is found to be small; thus the validity of the perturbative calculation of R is guaranteed.
The R ratio expressed in terms of the coupling constant g renormalized at scale µ contains, in general, large logs, ln(s/µ2), for large s in each term of the perturbative expansion and hence the effectiveness of the perturbative calculation is spoiled. According to Eq. (200), however, the calculation is drasticaly improved if we employ the coupling constant renormalized at the scale of the relevant energy .
Let us look into the details of the above statement. The
R ratio R(s/µ2, g) is given by the perturbative calculation in the form
R  Qi2[1+a(s/µ2)g2 +b(s/µ2)g4 +···],
i
(202)
where the index i runs over colors and flavors of quarks. The coefficients a, b,... in general include large logs, ln(s/µ2). Equation (200) indicates that, if g is replaced by g¯(s), these large logs in the coefficient disappear, i.e.,
R  Qi2[1 + a(1)g¯(s)2 + b(1)g¯(s)4 + ···].
(203)
The expression (203) is much better than Eq. (202) in two respects: its expansion coefficients are smaller than those in Eq. (202) and the expansion parameter g¯(s) is smaller than g for large s  ) according to the property of asymptotic freedom.
We shall show how to calculate a(1) in Eq. (203) in perturbative QCD. The strategy for computing a(1) is first to calculate the R ratio to order g2 by using the coupling constant g renormalized at the scale µ and then set µ2 =s to obtain a(1).
The Feynman diagrams contributing to the total cross section of the e +e − annihilation are shown in Fig. 3. The total cross section σ receives separate contributions from thefinalstatesqq¯,qqG¯ ,qqq¯ q¯,qqGG¯ ,...,withq,q¯,and G denoting the quark, antiquark, and gluon, respectively. The contribution up to order g2 may be represented as in
Fig. 4 and is split into three parts: the Born cross section σB (Fig. 4a), the virtual (one-loop) gluon contribution σV (Fig. 4b, c), and the real-gluon-emission cross section σR (Fig. 4d). Denoting the full cross section to order g2 by σ, we have
 R
	= σB + σ˜V + σR,	(204)
where B with Z2 thefieldrenormalization constant associated with the quark extrnal lines. The factor Z22 inEq.(204)isnecessarysincethefieldrenormalization constant Z21/2 for each quark external line should 
 
	 k	  2
(d)
FIGURE 4
beincludedintheexpressionoftherenormalizedS-matrix elements as a renormalized truncated Green function.
TheBorncrosssectionσB canbeobtainedbyneglecting electron and quark messes,
	 Qi2.	(205)
3s
i
The one-loop contribution σV to the e+e− →qq¯ cross section of Figs. 4b and 4c is calculated in the following way.Weconsiderthee+e− annihilationsatveryhighenergies so that quark masses are practically negligible. In the following calculations all the quarks are regarded as massless. The contribution of Figs. 4b and 4c can be written in such a way that
1 σV =  
8s
	×(k1 + k2 − p1 − p2)FV,	(206)
where FV is given by
FVTr[k/1µk/2γν] + c.c.,
q
i
(207)
with c.c. representing the complex conjugate of the first term and µ the one-loop vertex part corresponding to
Fig. 5,
	21	λ
µ	g CF	µ  γ . (208)
k/ + k/2
Note also that we use the Feynman gauge in the present calculation, and we calculate Z2 on the mass shell of quarks where quarks are massless. Here naturally we meet with the infrared divergence (mass singularity) arising from the vanishing quark mass. We shall regularize the mass singularity by means of dimensional regularization. For p2 =0thequarkself-energypart(p)intheFeynman gauge reads
	1	d Dk	1
 |p2=0	F	−	0	−	(2 π)Di k4
	 ,	(209)
where ε and ε are equal to the parameter (4− D)/2 and servetoregularizetheultravioletandinfrareddivergences,
 
respectively. From Eq. (209) we obtain the renormalization constant Z2 to one-loop order,
	Z .	(210)
The integration in Eq. (208) is performed similarly and results in
µ  
	 ,	(211)
where µ is the mass scale introduced to make the coupling g dimensionless and
	q = p1 + p2.	(212)
As expected, the ultraviolet divergences present in Eq. (211) cancel out in σ˜V on account of Eq. (210). Inserting Eq. (211) into Eq. (207) and taking account of Eqs. (205) and Eq. (210), we find
	σ˜V = AVσB,	(213)
where AV is given by
AV  
 , (214)
where αs is the QCD coupling constant defined by αs = g2/(4π).
The calculation of σR goes as follows. The cross section σR corresponding to Fig. 4d is written in the form
 
where
FR,
q
(216)
Sµν  .	(217) k/1 + k/3	k/2 + k/3
In Eq. (215) we worked in D dimensions ratther than in four dimensions because we anticipate possible infrared divergences. We introduce tensors Gµν, Lµν, and Iµν, Gµν ,	(218)
Lµν = Tr ,
(219)
Iµν Gµν.	(220)
The cross section σR is then expressed in the form
 CFLµν Iµν. (221)
As can be seen in Eq. (220), Iµν depends only on qµ and satisfies the following condition corresponding to the conservation of the electromagnetic current:
	qµIµν = 0.	(222)
Hence the general form of Iµν is given by
	Iµν = I(q2) ,	(223)
with I(q2)=−gµν Iµν/(D − 1). By means of Eq. (223) we obtain
	Lµν Iµν =	 −−	q gµν Iµν.	(224)
	D	1
On the other hand, we find after some calculation
	gµνGµν ,	(225)
(1 − x1)(1 − x2)
where ε =(4 − D)/2 and xi = 2ki · q/q2 (i = 1,2,3). (226)
The three-body phase volume for gµν Iµν in D dimensions may be rewritten in terms of the variables xi so that
gµν Iµν  xi)−ε dxiδ
	 gµνGµν.	(227)
Combining Eqs. (221), (224), (225), and (227), we arrive at
σR  
	 .	(228)
where µ comes from the mass dimension of the coupling constant g in D dimensions and
2
K.
2)
(229)
The constant K can be calculated analytically to order ε0,
i.e.,
KB
(230)
We wish to express Eq. (228) in the form of
	σR = ARσB,	(231)
with AR to be determined. For this purpose we needto find the expression for the Born cross section σB in D dimensions. We repeat the calculation of σB in D-dimensional space-time and obtain
 
Comparing Eq. (228) with (232), we find for AR of Eq. (231)
AR 
SubstitutingEqs.(213)and(231)intoEq.(204),wefinally obtain
 
In this result we clearly see that the infrared divergences present in AV and AR just cancel out leaving a finite oneloop effect. We thus finally obtain a(s/µ2), which was defined in Eq. (202).
It should be noted here that up to this order, a(s/µ2) is independent of large logs, ln(s/µ2), and so
	a(s/µ2) = a(1).	(235)
Under this circumstance we may, according to Eq. (200), simply replace αs in Eq. (234) by α¯ s, the running coupling constant,
	 ,	(236)
and obtain
	R .	(237)
i
Owing to asymptotic freedom, the running coupling constant of QCD decreases logarithmically as the relevant mass scale grows. Accordingly, Eq. (237) tells us that the R ratio in QCD approaches the parton-model prediction as s →∞.
B. qq¯ Jets in e+e− Annihilations
We shall show in the present section that hadronic jet phenomena are dominated by short-distance effects, so that perturbative QCD may be safely applied to the discussion of jet processes. For this purpose we present the proof of the cancellation of the infrared divergences in the jet cross sections since the infrared divergences reflect the long-distance nature of QCD.
Here we confine ourselves to hadronic jets arising from the quark–antiquark pair production in e+e− annihilations. In order that the hadronic jets flow from the quark– antiquark pair, the quark and antiquark are required not to lose too much energy in their direction by the emission of gluons and quark pairs. In other words it is necessary to show that most of the annihilation energy is deposited along the direction of the quark and antiquark. The first step of the argument is to give a precise definition of the jet cross section and then to prove that the dangerous infrared (soft and collinear) divergences are controllable in size. The jet generated by the above QCD mechanism is often called the Sterman–Weinberg jet or the QCD jet.
We have calculated in Section IV.A the total cross section of e+e− annihilations to which the QCD diagrams shown in Fig. 3 contribute. The contribution up to order g2 was represented in Fig. 4. Here we discuss the jet contibution up to the same order as above. The diagrams contibuting to jets are the same as in Fig. 4 though the kinematical region in the final state is restricted. We define the two-jet event in such a way that most of the available energy √s, i.e., (1 − )√s with  1, is deposited on two cones of small half-angle δ (see Fig. 6). We consider the angular distribution of the final quarks, i.e., the differential cross section dσ/d in the solid angle specified by polar and azimuthal angles θ and φ, respectively. The Born contribution (dσ/d )B corresponding to Fig. 4a is given by
 Qi2(1 + cos2 θ).	(238) d B	4s	i
The virtual (one-loop) contribution (dσ/d )V corresponding to Figs. 4b and 4c is directly obtained in parallel with the previous argument in deriving Eq. (213),
	,	(239)
B
where AV is given by Eq. (214).
 
FIGURE 6
Now comes the real-gluon-emission contribution (dσ/d )R corresponding to Fig. 4d, which occupies the majorpartoftheargumentintherestofthepresentsubsection. The differential cross section (dσ/d )R is defined in a similar way as in Eq. (215) by
d (2π)DδD
	R	i0
 FR, (240)
where FR is given by Eq. (216) and the integral region R is specified by the following conditions: The emitted gluon is either soft (i.e., x ) or collinear to one of the quarks(i.e.,θ13,θ23 <2δ),where x3 isdefinedbyEq.(226) and θ13(θ23) is the angle between the gluon and the quark (antiquark) as shown in Fig. 7. It should be noted here that the restriction of the phase space to R in Eq. (240) correspondstotakingthedegeneratestateofthequarkand gluon,andtheinfrareddivergences(softandcollinear)are known to cancel out in the following sum:
dσ
  =	. (241) d d B d V d R
It is convenient to define new variables ζ1 and ζ2 through  ,	(242)
	 ,	(243)
where use has been made of the relation
 
Since θ13, θ23 ≤2δ in R, we have
	ζ1,ζ2 ≤ sin2 δ.	(245)
Only two variables are independent among the five variables x1, x2, x3, ζ1, and ζ2 and so we choose ζ1 and x3 as independent variables. Then the region R is specified by
 δ, 0 ≤ x3 ≤ ,
(246)
where the lower bound of ζ1 comes from the condition ζ2 < sin2 δ. In Fig. 8 the kinematical region R given by Eq. (246) is shown in the ζ1–x3 plane. Neglecting terms of order δ2, we express (dσ/d )R in the form of an angular distribution with respect to the quark direction,
 
FIGURE 7
2
s
  KR, (247)
where
KR  ρ, (248)
	.	(249)
(1 − x1)(1 − x2)
Note that the slight deviation from the above angular distribution is expected if a precise calculation is made. Probably the easiest way of calculating KR in Eq. (248) is the following: We first note that
	KR = K − KR¯,	(250)
where K is the quantity corresponding to KR integrated over the whole phase space and is already given in Eq. (230) and KR¯ is obtained by integrating the integrand of Eq. (248) over the region R¯ which is obtained by eliminating R from the whole phase space as shown in Fig. 8. Since there is no infrared singularity in the region R¯, we may put ε =0 in KR¯ and then the calculation turns out to be straightforward. Changing the variables to ζ1 and x3, we obtain
KR  
where ζmax and ζmin are respectively the maximum and minimum values of ζ1 given in Eq. (246), and ρ defined in Eq. (249) is rewritten in terms of ζ1 and x3 as
= (1 − x3)2 + (1 − x3(2 − x3)ζ1)2
ρ.	(252) x32(1 − x3)ζ1(1 − ζ1)
After some calculation we find
KR .
(253)
 
Hence we have
KR
.
(254)
Exactly in the same way as in Eq. (232) we calculate the Born contribution to dσ/d in D dimensions, which results in
 ε
	B	i
	 .	(255)
Using Eqs. (247), (254), and (255) we finally obtain
 (256)
Combining Eqs. (238), (239), and (256), we see that the infrared divergences just cancel out, and find d d
According to Eq. (257), we realize that the order-αs correction to the two jets from the quark pair is controllable in size within the framework of perturbation theory and the hadronic pair jets appproximately in the direction of the quark and antiquark. Thus the angular distribution of the hadronic pair jets reflects the spin-1/2 nature of the constituents.
A similar argument as above may be made for hadronic jets originating from gluon sources. It has been shown that the same infrared cancellation as in the quark jets takes place in the gluon jets. Hence the hadronic jet from the gluon should also be observed experimentally. In fact, clear signals of three jets from the quark, antiquark, and gluon have been observed in e+e− annihilation processes.
SEE ALSO THE FOLLOWING ARTICLES
GREEN’S FUNCTIONS • GROUP THEORY, APPLIED • PER-
TURBATION THEORY • QUANTUM MECHANICS
BIBLIOGRAPHY
Bromley, D. A., and Schafer, A. (1994).¨	“Quantum Chromodynamics,” Springer-Verlag, Berlin.
Close, F. (1997). “The Cosmic Onion: Quarks and the Nature of the Universe,” Springer-Verlag, Berlin.
Fernandez, F. M. (2001). “Introduction to Perturbation Theory in Quantum Mechanics,” CRS Press, Boca Raton, FL.
Forshaw, J. R., and Ross, D. A. (1997). “Quantum Chromodynamics and the Pomeron,” Cambridge University Press, Cambridge. Henyey, F. (1994). “Quantum Chromodynamics,” Springer-Verlag,
Berlin.
Manohar, A. V., and Wise, M. B. (2000). “Heavy Quark Physics,” Cambridge University Press, Cambridge.
Reinhardt, H., and Alkofer, R. (1995). “Chiral Quark Dynamics,” Springer-Verlag, Berlin.
 
 
Quantum Hall Effect
 
J. K. Jain
Pennsylvania State University
I.	Quantum Hall Effect
II.	Integral Quantum Hall Effect
III.	Fractional Quantum Hall Effect
IV.	More Phenomena
GLOSSARY
Composite fermion (CF) The bound state of an electron and an even number (2p) of quantum mechanical vortices.
Filling factor (ν) The ratio of the number of electrons to the number of flux quanta (a flux quantum is defined as φ0 =hc/e) penetrating the sample. It is nominally equal to the number of filled Landau levels.
Hall effect Generation of a voltage transverse to the direction of current flow in the presence of a magnetic field. The ratio of the transverse voltage to the current is called the Hall resistance, RH .
Landau level (LL) The quantized kinetic energy of an electron in the presence of a magnetic field. The separation between Landau levels is called the cyclotron energy(hωc).TheLandaulevelsofcompositefermions are called CF-Landau levels.
Quantum fluid A fluid whose behavior is governed by quantum mechanical phases.
Quantum Hall effect (QHE) Occurrence of plateaus in the Hall resistance of a two-dimensional electron system on which it is quantized at RH =h/fe2, f being either an integer (the integral QHE) or a fraction (the fractional QHE). The plateau with RH =h/fe2 is centered at filling factor ν = f .
Two-dimensional electron system (2DES) A system of electrons confined to two dimensions. Such a system is obtained typically at the interface of two semiconductors. von Klitzing constant (RK) RK ≡h/e2.
I. QUANTUM HALL EFFECT
 	345
The study of magnetotransport in systems where electrons are confined to move in two dimensions has given us one of the most fascinating phenomena discovered in physics: the quantum Hall effect. Its theoretical investigation has helped uncover new structures and concepts, and there is a consensus that a sound understanding of the basic physics of this new quantum fluid has been achieved. This article makes an attempt to summarize in a simple, coherent, and least redundant manner the generally accepted knowledge at the present, to which a large number of workers have contributed. I apologize to those whose work could not be adequately represented due to length constraints or my ignorance; the books edited by R. E. Prange and S. M. Girvin (1990), S. Das Sarma and A. Pinczuk (1996), and O. Heinonen (1998) ought to be consulted for a comprehensive bibliography as well as a more detailed historical account.
 
FIGURE 1 Schematics of magnetotransport measurements. I,
VL, and VH are the current, longitudinal voltage, and the Hall voltage, respectively. The longitudinal and Hall resistances are defined as RL ≡VL/I and RH ≡VH/I.
In 1879, E. H. Hall discovered that the passage of current in the presence of a magnetic field induces a voltage perpendicular to the direction of the current flow, an effect known as the Hall effect (see Fig. 1). A new resistance, known as the Hall resistance, is defined as
VH
	RH =  .	(1)
I
The phenomenon can be understood in simple classical terms, based on the Lorentz force law of electrodynamics, which tells us that the Hall resistance is given by
B
RH =  ,	(2) ρec
where B is the external field, and ρ is density of current carriers. The proportionality of the Hall resistance to B is used routinely to measure the density of the mobile charges.
The modern field of quantum Hall effect (QHE) began almost exactly 100 years later, when K. von Klitzing in 1980, and D. C. Tsui, H. L. Stormer, and A. C. Gossard found in 1982 that in two-dimensional electron systems, the Hall resistance exhibits plateaus on which its value is quantized (Fig. 2), determined only by universal constants of nature:
h
	RH =  fe2 , 	(3)
where f can be either an integer (the integral quantum Hall effect, or IQHE) or a fraction (the fractional quantum Hall effect, or FQHE). Concomitant with the quantization of RH is an exponential suppression of the longitudinal resistance RL with temperature, indicating a total lack of dissipation in the limit of zero temperature.
The absolute accuracy of the quantization of RH has been established to 2.4 parts in 108 (for one standard deviation uncertainty), and the relative accuracy to 3.5 parts in 1010 at National Institute of Standards and Technology (Jeffery et al., 1998) and the Swiss Federal Office of Metrology (Jeckelman et al., 1995). The quantization is believed to be exact. The ratio h/e2 has been adopted as the fundamental unit of resistance, called the von Klitzing constant (RK ), with its value given by RK =25812.807572(95) Ohms. The combination h/e2 also occurs in the definition of the fine structure constant α =e2/h−c ≈1/137. Because the speed of light is known extremely precisely, the Hall effect measurements in dirty solid-state systems also provide one of the most accurate values for α.
The appearance of a universal quantization, independent of the sample type, geometry, and various materials parameters (like the band mass of the electron or the dielectric constant of the semiconductor), caught the community by surprise. One might expect such physics in, say, a simple atomic system, but it was entirely unexpected in a complex, macroscopic, and disordered solid-state system. Simple behaviors in complex systems have always enthralled physicists, and the discovery of QHE predictably stimulated intense activity in search of the fundamental principles responsible for it.
II. INTEGRAL QUANTUM HALL EFFECT
The IQHE, namely, the quantization of the Hall resistance at RH =h/ne2 where n is an integer, was discovered by vonKlitzingin1980.Thatthephenomenonhasaquantum mechanical origin (hence the Q in QHE) was obvious by the appearance of the Planck’s constant in the formula for the Hall resistance. Our understanding of the IQHE, discussed later, shows that it is a single particle effect, that is, it can be understood in an independent electron model. It is a dramatic consequence of the well-known quantization of the electron kinetic energy into Landau levels (LLs).
 
FIGURE 2 Overview of the quantum Hall effect. The Hall resistance RH and the longitudinal resistance RL are plotted as a function of the magnetic field B. (Adapted from Stormer and Tsui, 1996.)
A. Landau Levels
The Hamiltonian for a single electron moving in two dimensions in a perpendicular magnetic field is given by
	H  	,	(4)
	2mb	c
where, A is given by ∇ ×A = B = Bz ˆ and mb is the band mass of the electron. The solution of this problem shows that the electron kinetic energy is quantized into Landau levels, as shown in Fig. 3B,C. The eigenenergies are given by En =−hωc(n +1/2), where ωc =eB/mbc is the cyclotron frequency, and n =0,1,... is the Landau level index. The degeneracy of each Landau level for a single spin is given by B/φ0 per unit area, where φ0 =hc/e is called the flux quantum.
Nowconsidermanyindependentelectrons,withdensity ρ per unit area. The ground state is obtained by filling up the lowest energy single particle orbitals, with the condition that no orbital is occupied by more than one electron, as required by the Pauli principle. The number of filled Landau bands,
	 	(5)
B
is called the filling factor (defined so that a Landau level filled with both spins has a filling factor of 2). The plateau with RH =h/ne2 is centered at ν =n.
The many-particle ground state is infinitely degenerate in general, because all arrangements of electrons in the topmost partially filled Landau level produce the same energy. The exception is at an integral filling factor, ν = n. The ground state here is unique (Fig. 3B), with a gap to excitations. This fact is responsible for the IQHE plateau with RH =h/ne2.TheIQHEisaconsequenceofthequantization of the electron energy into Landau levels.
B. Disorder and QHE Plateaus
Even though the physics of the IQHE lies in the opening of a gap at integral filling factors, it turns out that a finite amount of disorder is also needed for the establishment of the plateaus. It is easy to see that no plateaus may result in the absence of disorder. Consider the motion of electrons in crossed electric and magnetic fields in a system without disorder. Taking advantage of the translational invariance of the problem, we can boost to a frame of reference moving with velocity v =cE/B in which there is no electric field,andhencenocurrent.Thisallowsacalculationofthe current in the laboratory frame of reference, which yields the classical value of the Hall resistance, Eq. (2), with no plateaus.
The Landau levels are broadened by disorder as depicted schematically in Fig. 4, with extended states at the
 
FIGURE 3 Evolution of two-dimensional electron system as the transverse magnetic field B is increased. For independent electrons, the Fermi sea (A) (filled to Fermi energy EF) at B=0, splits into Landau levels (B). The lowest Landau level (C) is split by interactions into energy levels of composite fermions. The composite fermions are shown as electrons with attached vortices, with each vortex represented by an arrow. These fill a CF-Fermi sea (D) at n =1/2 (filled to Fermi energy E∗F) and occupy CF-LLs (E) at other filling factors. A jump out of such a level (F) creates a CF exciton. At still higher fields, the scenario (D–F) repeats itself, but now with composite fermions carrying four or more flux quanta. The particle spin has been neglected for simplicity of illustration. (Adapted from Jain, 2000.)
 
FIGURE4 Schematicsofthesingleparticledensityofstatesasa function of energy in the presence of disorder. The Landau levels are broadened, with extended states at the centers and localized states elsewhere.
centers and localized states elsewhere. A somewhat oversimplified description of the physics of plateaus is as follows.Atintegralfillingν =n,theclassicalformulaEq.(2) for the Hall resistance can be recast to give RH =h/ne2. Now imagine changing the filling factor away from ν =n by adding some electrons or holes to the system. So long as the additional particles go into orbitals that are localized, they do not contribute to transport; as a result, the Hall resistance retains its value RH =h/ne2.
A more general and precise explanation for the Hall plateau follows from an argument due to R. B. Laughlin (1981), which showed that the Hall resistance is quantized at RH =h/ne2 whenever the Fermi level lies in the localized states, with n counting the number of extended bands below the Fermi level. Consider a Hall bar with periodic boundary conditions, which has the topology of the Corbinodisk,showninFig.5.Imaginethatideal,disorderfree regions have been attached at the inner and the outer boundaries of the Corbino sample. An azimuthal current I flows when a voltage VH is applied across the sample. The current I is related to the variation in the energy of the system as a function of a test flux φ through the center by I =c(dU/dφ), which is approximated by I =c(U/φ0), where U is the change in energy during the process of changing the test flux adiabatically by φ0 =hc/e. Because a flux quantum through the center can be gauged away, the single particle energy levels at φ =0 and φ =φ0 are identical. The energy U changes because the occupations of the single particle energy levels are different at φ =φ0 than at φ =0. The determination of U requires monitoring the evolution of single particle orbitals as the test flux φ is varied from 0 to φ0. Each of the extended states, defined as states that go around the sample thereby encircling the test flux, moves to the next one during this process. The localized states, which do not enclose the test flux, remain unaffected. Let us now consider the situation when all of the extended states of the lowest n LLs are occupied, i.e., the Fermi level lies in localized states. As the extended states evolve under the variation of φ they carry their electrons with them, because there is nowhere else for the electrons to go. At the end of the adiabatic process, each extended state has moved into the next one, carrying its electron with it, with the net effect that precisely n electrons have been transported from the inner to the outer edge of the Corbino disk. We therefore have
U =neVH which gives us the quantized Hall resistance RH = V/I =h/ne2.
A closely related approach for understanding the IQHE is based on the Landauer-Buttiker theory of resistance¨ (Buttiker, 1988). This approach is especially useful for¨ dealing with deviations from exact quantization. Consider a sample with translational invariance in the x direction, so px,themomentuminthexdirection,isagoodquantum number. The potential in the y direction is a combination of the confinement potential at the edges, and the potential
 
FIGURE 5 Schematic depiction of the single particle states in the Corbino geometry, with a test flux f piercing through the hole.
due to the applied Hall voltage. Let us now consider a full Landau level, that is, a state in which all single particle energy levels with momenta p− < px < p+ are occupied, where p− and p+ are the momenta at the edges of the sample. The current in the x direction is obtained by adding the individual currents:
dpx
	Ivx.	(6)
2πh
Withvx px, it follows that I =(e/h)(µ+ −µ−)=(e2/h)VH , where µ+ and µ− are the chemical potentials at the edges. The current is independent of the LL index, so the total current for n filled Landau levels is I =(ne2/h)VH . Now consider a sample with disorder, but connected to the current source via ideal, disorder-free leads. So long as the electrons at the chemical potential, which are at one edge of the sample, are not back-scattered, the current is not degraded and the Hall resistance remains quantized at RH =h/ne2,independentofdisorder.Theback-scattering is strongly suppressed because the states carrying currents in opposite directions are localized on opposite edges, and therefore are exponentially weakly coupled.
III. FRACTIONAL QUANTUM HALL EFFECT
A.	Phenomenology
In 1982, Tsui, Stormer, and Gossard observed a plateau quantized at RH =h/13e2. In the subsequent years, as the result of a tremendous improvement in the quality of samples, a host of new fractions were observed. Today, the number of observed fractions below unity ( f <1) stands at approximately 50 and increasing. The plateau at
RH =h/ fe2 is seen in the vicinity of filling factor ν ≈ f . The longitudinal resistance RL exhibits activated behavior, as in IQHE, indicating the existence of a gap in the excitation spectrum. The observed fractions appear in sequences of the form
n
	f  .	(7)
Some of the fractions observed to date are:
Thefirstseveralmembersofeachsequencearewellestablished, in that quantized plateaus have been observed. The lastfewareseenonlythroughresistanceminima,butthere is little doubt that the corresponding Hall plateaus will develop upon further improvement in sample quality. FQHE at f also implies FQHE at 1− f due to particle-hole symmetry in the lowest Landau level. In addition to these fractions, FQHE has also been observed with f =5/2, the only exception to the “odd-denominator rule” in a single layer system.
B.	Model Hamiltonian
BecauseonlytheintegralQHEispossibleforindependent electrons, interactions are clearly responsible for producing gaps at fractional filling factors. One therefore must look for the solutions of the more complete problem of interacting electrons, defined by the Schrodinger equation¨
H = E with
1
H
	j	rj − rk|
	 gµB · S.	(8)
j
The first term on the right-hand side is the kinetic energy, the second term is the Coulomb interaction energy, the third term is a one-body potential incorporating the effects of the uniform positive background and disorder, and the last term is the Zeeman energy. The parameter  is the dielectric constant of the background material.
Insofar as the conceptual foundation of the FQHE is concerned, it is convenient to neglect disorder, and consider the limit of large B, so both the cyclotron and the Zeeman energies are large compared to the interaction energy. The electrons are then fully polarized and confined to the lowest LL, making the kinetic and Zeeman energies irrelevant constants. We thus end up with the idealized model of fully polarized electrons in the lowest LL with the Hamiltonian (suppressing the interaction with the background)
	e2	1
	HLLL =  |	−	|.	(9)
	 j<k rj	rk
This is the simplest and the cleanest model containing the essentialphysicsoftheFQHE.Thestronglycoupled,nonperturbative nature of the problem can already be seen by noting that there is no small parameter in the problem: HLLL contains only one energy scale, set by the Coulomb interaction. All states are degenerate in the absence of interaction, and the FQHE results as soon as the interaction isturnedon,nomatterhowsmallitsstrength(or,howlarge ). Standard perturbative treatments are not useful here.
The FQHE is a true many body phenomenon, in which strongly interacting electrons behave in a correlated manner to produce rich and nontrivial, yet amazingly simple behavior. The solution of this Schrodinger equation¨ should clarify the physics responsible such behavior. By analogy to the IQHE, the plateau at RH =h/fe2 with fractional f originates due to the opening of a gap at ν = f . (For such a gapped state, when the filling factor is moved away from ν = f , some “defects” are created, but they are pinned by disorder, thus giving rise to a plateau at RH =h/fe2.) The goal of theory is therefore to explain the origin of gaps in a partially filled Landau level, specifically why they appear only at certain sequences of odd-denominator fractions. A satisfactory explanation of the odd-denominator rule must necessarily elucidate why there is no FQHE at even-denominator fractions (with the exception of f =5/2). Even though the problem looks intractable at first, the trail of experimental clues has led to a simple, yet extremely accurate solution to the problem that is also in good agreement with experimental observations.
C. Laughlin’s Theory
The first observed fraction was f =1/3. Soon thereafter, in 1983, Laughlin noted that the single particle wave function in lowest Landau level has the form zs exp[−|z|2/4l2], where z = x −iy denotes the position=√ of the electron as a complex number, and l hc/eB is the magnetic length. The wave function of a system containing many electrons must therefore have the form
FS ] where FS is an antisymmetric polynomial of z j. Choosing a Jastrow form for the polynomial, he wrote the following wave function
	1/m =	j	k	2	i	,	(10)
4l
which provides an excellent representation of the ground state at ν =1/m, as confirmed by comparison with exact results known for small systems. This wave function served as a paradigm for the subsequent theoretical developments. It is easy to see that it has good correlations built in it in the presence of repulsive interactions. In a typical wave function satisfying the Pauli principle, the probability of two electrons approaching one another vanishes as r2,r being the distance between them. In 1/m, it vanishes much faster, asr2m, which shows that electrons avoid each other efficiently.
The exponent in the Jastrow factor, m, must be an odd integer, due to the fundamental requirement of the antisymmetry of the wave function. For m /m gives the wave function of the fully occupied lowest LL (ν =1), and for m =5 it gives the wave function at ν =1/5, which is relevant to FQHE at f =1/5 observed later on. However, the exponent is not allowed to take noninteger or even-integer values, and the observations of numerous fractions other than 1/m subsequent to Laughlin’s theory pointed to the existence of a more general structure.
D. Composite Fermions
A more general theory was put forth by the author in 1989. The fundamental building block of this theory is called the composite fermion, which is the bound state of an electron and an even number of quantum mechanical vortices. According to this theory, strongly interacting electrons in the lowest LL capture vortices to turn into weakly interacting composite fermions. The ensuing investigations revealed that the FQHE was only one manifestation of composite fermions, which describe a superstructure encompassing other phenomena as well. Experimenters observed their Fermi sea, their Shubnikov-de Haas oscillations, and their semiclassical cyclotron orbits; they also measured the particles’charge,spin,statistics,mass,andmagneticmoment (Stormer and Tsui, 1996).
The composite fermion (CF) theory proposes the following wave functions at any arbitrary filling factor ν:
N
	  zk)2p,	(11)
whereν∗ aretheknownwavefunctionsofnoninteracting electrons at an effective filling factor ν∗, related to ν as
	 .	(12)
This equation gives wave functions for ground as well as low-energy excited states of interacting electrons at arbitrary ν, derived from the corresponding states of noninteracting electrons at   describe a strongly correlated state of electrons, because the probability of electrons approaching one another in ν vanishes rapidly as r4p+2. In the limit of very strong B, the functions  are to be projected into the lowest electronic LL.
The wave functions  in Eq. (11), which are accurate representations of the actual eigenstates (see below), lend themselves to a simple interpretation. They contain a Jastrow factor (zj − zk)2p which attaches 2p vortices to each electron. The bound state of an electron and 2p vortices behaves as a particle, called the composite fermion. The electronic wave function  can therefore also be interpreted as wave functions of composite fermions.
The capture of vortices has a profound consequence for the dynamics of the particles. As composite fermions move about, the vortices carried by them generate phases which partly cancel the Aharonov-Bohm phases due to the external magnetic field, and the composite fermions in effect experience a much weaker magnetic field. Because a closed path around a vortex produces, by definition, a phase of 2π, a vortex is effectively equivalent to a flux quantum, which also produces the same Aharonov Bohm phaseforaclosedpatharoundit.(Forthisreason,thecomposite fermion is often envisioned as an electron bound to 2p flux quanta.) Therefore, each vortex cancels one flux quantum of the external magnetic field, giving the effective magnetic field:
	B∗ = B − 2pρφ0.	(13)
In effect, each electron absorbs 2p flux quanta of the external field to become a composite fermion (Fig. 6). (It must be understood here that an external magnetometer will measure B and not B∗. There is no real “Meissner effect” in the FQHE. However, B∗ is the real magnetic field for composite fermions; this is the field that would be obtained if the composite fermions themselves are used to measure the field.) Treating composite fermions as independent, their filling factor is ν∗ =ρφ0/|B∗|, and Eq. (13) can be transcribed into the relation in Eq. (12). The − sign in Eq. (12) corresponds to the situation when B∗ points opposite to B.
Laughlin’s theory of inverse-odd-integer states falls naturally within the CF theory. The wave function 1/(2p (z j − zk)2p is identical to Laughlin’s wave function, which can be seen by noting that the wave function of the fully occupied lowest LL is given by

4l j<k	i
1/(2p+1) is interpreted as one filled Landau level of composite fermions.
 
FIGURE 6 Capturing two flux quanta converts each electron into a composite fermion moving in a reduced effective magnetic field. (Adapted from Jain, 2000.)
Theunusualcharacterofcompositefermionoughttobe emphasized. It is a collective particle, with the definition of one composite fermion involving all particles in the system. A composite fermion may live only inside the CF liquid. It is an inherently quantum mechanical object, a “quantum particle,” because it is the product of the union of an electron and quantum mechanical phases (vortices). The fluids of composite fermions are quantum fluids not onlybecausecompositefermionsthemselvesarequantum particles, but also because they involve a quantization of the composite fermion orbits into CF Landau levels. The composite fermion also has a topological character due to its integrally quantized vorticity (=2p). It is indeed surprising that the composite fermions behave as ordinary particles to a large degree.
In 1991, A. Lopez and E. Fradkin implemented the physics of composite fermions in a Chern-Simons field theoretical framework. It has been further developed by a number of groups over the years. The Hamiltonian formulation of R. Shankar and G. Murthy (1997) obtains many essential features at the Hartree-Fock level.
To summarize: The strongly interacting electrons in the lowest Landau level transforms into weakly interacting composite fermions in a reduced magnetic field B ∗. The lowest electronic Landau level thus splits into energy levels of composite fermions (Fig. 3).
E. FQHE
Plotting the FQHE data as a function of B∗ brings out its striking similarity to the IQHE data plotted as a function of B, as seen in Fig. 7. The difference between the two is no more significant than that between the IQHE traces in different samples demonstrating that the strongly correlated liquid of interacting electrons at B behaves as a weakly interacting system of fermions at B∗. A similar correspondence is obtained for negative values of B∗, and also at lower electron filling factors, where composite fermions have four or more vortices bound to them.
There is also a correspondence between the Hall plateaus at B and B∗, but the Hall resistances are not the same at ν∗ and ν. For example, at ν =1/2, where B∗ =0, the Hall resistance is RH ), but at B =0 we have RH =0. The difference is explained by noting that the composite fermions respond to a combination of the external Hall voltage and the Hall voltage induced by the vortex current tied to the charge current in the CF state, but the latter is not measured by the external voltmeter. (Just like the effective magnetic field, the induced Hall electric field is also fully internal to composite fermions.) The FQHE of electrons is understood as the IQHE for composite fermions. The integral fillings ν∗ =n of composite fermions correspond to electron filling factors
 
FIGURE 7 The top panel shows the IQHE of electrons. The bottom panel shows the FQHE of electrons plotted as a function of B ∗, starting from B ∗=0 (n =1/2). A close correspondence between the prominent features is manifest. (Adapted from Clark,
1986, and Du, 1993.)
ν = n /(2pn ±1), which are precisely the observed fractions. The composite fermion is to the FQHE what the electron is to the IQHE. Just as the IQHE is an observation of the electron Landau levels, the FQHE is an observation of the composite-fermion Landau levels. The phenomena of the IQHE and the FQHE, which were at first thought to be distinct, thus turn out to be intimately related: They are both integral quantum Hall effects, but for different particles. This unification of the FQHE and the IQHE is not surprising in view of the empirical similarity between the two (Fig. 2).
F. Computer Experiments
For a finite number of particles, the Hilbert space in lowest Landau level is finite, allowing a complete and exact solution of the problem through a brute force numerical diagonalization of the Coulomb Hamiltonian. Even though the systems are finite, they are sufficiently large (10–15 particles) to provide the opportunity for rigorous, detailed, and nontrivial tests of the theory. The computer experiments are also cleaner than the real experiments, in that the idealized limits of no disorder and large magnetic field can be explicitly implemented. For these reasons, computer experiments have played an important role in the theory of the FQHE. Figure 8 shows a number of exact spectra for interacting electrons in the lowest Landau level at the special filling factors of ν = 1/3, 2/5, and 3/7. The spherical geometry (Haldane, 1983) is used in these calculations, which considers electrons moving on the surface of a sphere with a radial magnetic field of appropriate strength through the surface of the sphere; the total orbital angular momentum L is used to label the eigenstates.
The energy spectrum predicted by the CF theory, obtainedwithoutanyadjustableparameters,isshownbydots
 
FIGURE8 Energyspectrumforsystemswith N =8–12iteracting electron at n =1/3,2/5 and 3/7 moving on the surface of a sphere inthepresenceofaradialmagneticfield.Thedashesshowtheexact eigenenergies and the dots show the CF predictions obtained without any adjustable parameters. L is the total orbital angular momentum. The ground state (encircled) is described as an integer number of filled CF-LLs, and the branch of low-lying excited states, decorated with dots, represents the CF-exciton in various possible configurations. The energy is quoted in units of e2/l, where l is the magnetic length. (Adapted from Jain and Kamilla, 1998.)
in Fig. 8. The CF energies agree with the exact eigenenergies to within 0.05–0.1%, and the overlaps between the exact eigenstates and the corresponding CF wave functions are close to perfect (typically >99%) for all systems studied. Numerous such studies have confirmed the description of the FQHE ground state as the state containing n-filled CF-LLs, and the lowest energy branch of excitations as the CF-exciton (a particle-hole pair of composite fermions).
G. Excitations and CF Mass
The quantitative understanding of real experiments is less accurate than that of computer experiments, because the experimental numbers are unavoidably affected by the nonzero transverse thickness of the wave function (the dynamics is still strictly two dimensional because only the lowest transverse subband is occupied), Landau level mixing, and disorder, all conveniently set to zero in the computer experiments. As a result, the experimental resultsthemselvesvaryfromsampletosample,depending on various parameters such as the form of the confinement potential, electron density, band mass, or mobility. An incorporation of these sample-specific effects into theory requires approximations which, even in the best cases, introduce uncertainties on the order of 20–30% in the theoretical numbers.
The dispersion of the neutral CF exciton (Fig. 3F) contains, in general, several minima, called rotons. The roton at ν = 1/(2p + 1) was first obtained by S. M. Girvin, A. H. MacDonald, and P. M. Platzman in 1985 in a single-mode approximation theory. The roton energies have been determined experimentally for several FQHE states in both Raman and ballistic phonon scattering experiments, and are in good agreement (10–20%) with the theoretical calculations of V. W. Scarola and co-workers (2000). The neutral excitation in the long wavelength limit was observed by A. Pinczuk and co-workers in 1993 in Raman experiments (Fig. 9).
The longitudinal resistance displays activated behavior,
RL ∝ exp[−a/2kBT], over a range of temperature. The activation energy a is identified with the energy of a far separated particle-hole pair of composite fermions. The agreement between theory and experiment is somewhat worse in this case (∼factor of 2), presumably because the energy of the charged excitation is more strongly affected by disorder, neglected in theory. a is interpreted as the effective cyclotron energy for composite fermions, −heB∗/m∗c, which defines a composite fermions mass, m∗ (Du, 1993). A reasonably consistent interpretation of the activation energies for different FQHE states is obtained in terms of a single mass parameter. For typical parameters, the mass of the composite fermion is comparable to
 
FIGURE 9 The long-wavelength collective mode (labeled the “gap excitation”) at n =1/3 in Raman scattering. The inset shows a comparison between the experimental data (stars) (Kang et al., 2001) and the theoretical estimation of two-roton bound state energy (dashed line). Theoretical estimates (Park and Jain, 2000) are obtained by considering Landau level mixing as well as finite thickness effects. (Adapted from Pinczuk, A. et al. 1993.)
the electron mass in vacuum and approximately an order of magnitude larger than the band mass of the electron in GaAs, but unrelated to either; it is completely determined by the interaction between electrons.
H. Fractional Charge
Laughlin showed in 1983 that the charge of the excitation in a FQHE state is fractionally quantized. At ν = n/(2pn±1), the value of the charge is |e∗|=e/(2pn±1), as seen most simply from the following argument. Take the state at ν =n/(2pn±1) and adiabatically insert a flux through the origin from zero to φ0. For a nondegenerate state, this creates a vortex (or an antivortex depending on the direction of the flux), the charge of which can be shown to be of magnitude νe, as follows essentially from the definition of the filling factor. The vortex is in general a collection of an integral number (r1) of “elementary” excitations, i.e., r1|e∗|=[n/(2pn±1)]e. On the other hand, because an added electron must decay into elementary excitations, we must also have r2e∗ =e, r2 being another integer. The two conditions are compatible only with fractional values for e∗, the largest solution being |e∗|=e/(2pn±1). This derivation clarifies that the fractional charge is an inescapable, model-independent consequence of the existence of a nondegenerate ground state in a partially filled LL, and its valued is fixed by the filling factor. In the CF theory, the fractional charge of the
I. Spin Physics
At sufficiently large B, when the Zeeman splitting
EZ →∞, the low-energy states are maximally polarized, and the spin of the electron is frozen. However, EZ is quite small for typical experimental parameters (Halperin, 1983). Due to a small band mass (0.07 of the free electron mass) and a small g factor (−0.44 as opposed to 2 in vacuum), the ratio EZ /−hωc is only ∼1/70 in GaAs. EZ
FIGURE 11 The positions (dots) of transitions between states with different spin polarizations as a function of the Zeeman energy (y-axis) at various fillings (x-axis) around n =3/2 (The filling factors n =(3n±2)/(2n±1) are related to n =n/(2n±1) by particle-hole symmetry, which relates n to 2−n for spinful electrons). The CF-LL occupation is shown pictorially in each region, labeled by n :n . The solid lines emanating from the origin are
	↑	↓
from a model of independent composite fermions with the CF mass and g factor treated as adjustable parameters. (Adapted
from R. R. Du et al. (1995).)
 
Quantum Hall Effect 
observations verify that the spin of the composite fermion is 1/2.
J. Even Denominator Fractions
At ν =1/2, the simplest even-denominator fraction, the effective field vanishes for composite fermions. V. Kalmeyer and S. C. Zhang (1992), and B. I. Halperin, P. A. Lee, and N. Read (1993) formulated the metallic state hereintermsofaFermiseaofcompositefermions.Atprecisely ν = 1/2, composite fermions move in straight lines. Slightly away from ν = 1/2, where B ∗ is very small, they are expected to execute semiclassical cyclotron orbits. The radius of the cyclotron orbit of a composite fermion at the Fermi surface is given by R∗ =−hk∗F/eB∗, with k∗F = ,asappropriateforafullypolarizedFermisea. R∗ involves only known parameters, and can be orders of magnitude of larger than any electronic length scale in the problem. The cyclotron radius of the charge carriers was measured in 1993–1994 through magnetic focusing
(Fig. 12), geometrical antidot resonances (Fig. 13), and surface-acoustic-wave attenuation measurements (Willett et al., 1993), and was found to be in agreement with R ∗ of the CF theory. Besides demonstrating the existence of composite fermions outside of the FQHE (because no FQHE is seen in the vicinity of ν =1/2), these exper-
 
FIGURE 12 Direct determination of the effective magnetic field by magnetic focusing of composite fermions by injecting them into one constriction and collecting into another, possibly after an integer number of bounces (inset). The lower panel shows the fo-
focusing peaks for composite fermions withcusing peaks for electrons at B≈0, while the upper depicts theB∗≈0. The focus-
ingpeaks(superimposedovermesoscopicresistancefluctuations due to disorder) align after scaling B∗ by a factor of √2 to account forthefactthattheelectronFermiseaisspinunpolarizedwhereas the composite-fermion Fermi sea is spin polarized. (Adapted from Goldman et al., 1994.)
 
FIGURE 13 The upper panel shows the usual magnetoresistances. The lower panel shows geometric resonances in an antidot superlattice (inset) for electrons (lower curve) and composite fermions (upper curve). The two pairs of peaks for electrons near the origin correspond to two smallest cyclotron orbits of electrons commensurate with the antidot lattice, shown in the inset. The two broad peaks for composite fermions corresponds to the resonance due to the smallest CF cyclotron orbit. The x-axis is the real magnetic field for electrons and the effective magnetic field for composite fermions. (For comparison, B∗ has been scaled by
 
√2 as in Fig. 12.) (Adapted from Kang, W., et al. (1993).)
iments also explicitly confirmed the fermionic nature of compositefermionsthroughtheobservationoftheirFermi sea. The Shubnikov-de Haas oscillations, thermoelectric power, and spin polarization measurements are also consistent with the composite-fermion Fermi sea description. The absence of FQHE at ν =1/2 is explained because the Fermi sea has no gap to excitations.
K. Exactness of Hall Quantization
The principle governing the exactness of the Hall quantization can be traced to the topological feature that the number of vortices bound to each electron must be exactly quantized to be an integer, as required by the fundamental principle of single-valuedness of the quantum-mechanical wave function. This results in an exactly quantized quasiparticle charge, which in turn guarantees the exactness of the Hall quantization, following Laughlin’s 1981 argument that relates the quasiparticle charge to the value of the Hall resistance. The odd-denominator rule is a consequence of the antisymmetry of , which requires 2p to be an even integer. The Hall quantization is thus a macroscopic manifestation of microscopic postulates of quantummechanics.(Itshouldbeemphasizedthattheaccuracy of the wave functions  does not by itself imply the exactness of the Hall quantization, but it gives us confidence that the physics of binding of 2p vortices to each electron is exact.)
IV. MORE PHENOMENA
Many other phenomena have been investigated in the context of the QHE. In all cases, there has been a healthy interaction between theory and experiment to produce rapid progress.
A. 2D Localization in Magnetic Field
As discussed earlier, localization of states is crucial for the establishment of plateaus. This has motivated an intense investigation into the nature of single particle states in the QHE regime in the presence of disorder, and much progress has been made (Das Sarma and Pinczuk, 1996). Numerical solution of the Schrodinger equation¨ makes a strong case that truly extended states occur at only one energy (Ec) in each Landau band, with the localization length diverging as ξ ∼|E − Ec|−γ with γ ≈2.3. The width of the transition region between two plateaus is experimentally found to vanish as T−0.42 with temperature; the value of the exponent is consistent with the theoretical value 1/γ z ≈0.43, provided the dynamical exponent is taken to be z =1, as expected for quantum phase transitions in Coulomb systems.
B. Wigner Crystal
When the interaction energy dominates over the kinetic energy, it is believed that electrons form a lattice called the Wigner crystal (WC). Because the kinetic energy is effectively suppressed in the lowest LL, one might a priori have expected a WC here rather than the FQHE. A variational calculation, reproduced in Fig. 14, shows that the CF liquid has a significantly lower energy than the WC for a range of ν, but the WC wins at sufficiently small ν. There is good experimental evidence for an insulating behavior at small ν(<1/5), interpreted as a pinned Wigner crystal (Jiang, 1990); observation of nonlinear I–V (Goldman, 1990) supports this view.
C. Skyrmion
The neglect of interactions at integral fillings is valid in the B →∞ limit, but interactions may affect the nature of excitationssignificantlyundertypicalexperimentalconditions. In 1993, S. L. Sondhi, A. Karlhede, S. A. Kivelson, and E. H. Rezayi showed theoretically that the excitation at ν =1 is typically not a simple spin reversed electron but has a nontrivial spin texture, described in a (nonlinear sigma-model) field theory as a skyrmion. It was observed in 1995 by S. E. Barrett and coworkers. The size of the skyrmion shrinks rapidly with increasing Zeeman energy,
 
FIGURE 14 The variational energies per particle of the CF liquid and the Wigner crystal as a function of the filling factor. Ecl /el is the energy of a classical twodimensional Wigner crystal with triangular symmetry. The open diamond on the right vertical axis is the estimate of the CF Fermi sea energy at n =1/2, obtained by an extrapolation. The energy of the CF liquid is shown only at the special n/(2pn+1) filling factors; the full curve will have downward cusps at these points.
(Source: Jain and Kamilla, 1998; Lam and Girvin, 1984.)
butskyrmionswithasmanyas30reversedspinshavebeen observed in systems where the g factor was suppressed by application of hydrostatic pressure.
D. Edge States
Even when there is a gap to excitations in the bulk, gapless excitations exist at the edges of the sample. It is believed that the physics of the edges is effectively one dimensional, described by the well-developed theory of Tomanaga-Luttinger liquids. In 1990 X. G. Wen argued that the quantized value of the Hall resistance fixes the parameters of the Luttinger model, leading to definite predictions for various power laws, say, for the resistance associated with tunneling into and out of the edges of a FQHE system through a weak link. Significant progress toward experimental tests of some aspects of theory has been made, notably by A. M. Chang and co-workers.
E. Pairing of Composite Fermions
At filling factor ν =5/2=2+1/2, the lowest Landau level is fully occupied and the filling factor is 1/2 in the second Landau level. Treating the electrons in the lowest LL as inert, one would naively expect a Fermi sea of composite fermions in the second Landau level. However, a FQHE was observed here already in 1987 by Willett and co-workers. There is growing support to the view that the FQHE originates here due to a pairing of composite
Quantum Hall Effect
fermions, which opens up a gap. Variational and exact diagonalization studies indicate that the paired CF state is described by a particle-hole symmetrized version of a Pfaffian wave function written in 1991 by G. Moore and N. Read.
F. Stripes
The abundance of FQHE in the lowest LL is in contrast to its near absence in higher LLs. Very few fractions are seen in the second LL (2<ν <4) and none whatever in third and higher LLs, indicating that some other physics takes over in higher Landau levels. In a HartreeFock calculation, A. A. Koulakov, M. M. Fogler, and B. I. Shklovskii showed in 1996 that close to ν = n + 1/2 in high LLs the system prefers to phase separate into alternating stripes of ν =n and ν =n +1. Observation of a strongly anisotropic RL at ν ≈ n + 1/2 for n > 4 (M. Lilly and co-workers, 1999; R. R. Du and co-workers, 1999) supports this picture.
G. Multilayer Systems
Two far-separated layers are simply two single-layer systems. However, when the layers are sufficiently close, new structure may arise. An interesting example is the FQHE at  4 , observed by Y. W. Suen et al. and J. P.
Eisenstein et al. in 1992. It is well described by a multicomponent wave function of Halperin (1983).
H. Topological Considerations
In 1985, to explain the precision of the Hall quantization, Niu, Thouless, Wu, and Kohmoto showed that the value of the quantized Hall resistance in the integral QHE is related to a topological invariant called the Chern number. Thouless et al. (1982) also considered QHE in periodic geometries, for which the Landau level splits into Hofstadter bands, and showed that the Hall resistance of each band is integrally quantized, with the integer characterizing the quantization depending sensitively on the value of flux per plaquette.
ACKNOWLEDGMENTS
The author was supported in part by the National Science Foundation. He thanks V. W. Scarola, K. Park, and M. Marder for help with figures.
SEE ALSO THE FOLLOWING ARTICLES
ELECTRODYNAMICS, QUANTUM • ELECTRON SPIN RESONANCE • QUANTUM MECHANICS
BIBLIOGRAPHY
Barrett, S. E., et al. (1995). “Optically Pumped NMR Evidence for Finite-Size Skyrmions in GaAs Quantum Wells near Landau Level Filling ν =1,” Phys. Rev. Lett. 74, 5112–5115.
Buttiker, M. (1998).¨ “Absence of backscattering in the quantum Hall effect in multiprobe conductors,” Phys. Rev. B38, 9375–9389. Chang, A. M., et al. (2001). “Plateau Behavior in the Chiral Luttinger Liquid Exponent,” Phys. Rev. Lett. 86, 143–146.
Clark, R. G., et al. (1986). “Odd and even fractionally quantized states in GaAs-GaAlAs heterojunctions,” Surf. Sci. 170, 141–147.
Das Sarma, S., and Pinczuk, A. (eds.) (1996). “Perspectives in Quantum Hall Effects,” Wiley, New York.
DePicciotto,R.,etal.(1997).“Directobservationofafractionalcharge,” Nature 389, 162–164.
Du, R. R., et al. (1993). “Experimental evidence for new particles in the fractional quantum Hall effect,” Phys. Rev. Lett. 70, 2944–2947.
Du, R. R., et al. (1995). “Fractional quantum Hall effect around ν =3/2: Composite fermions with a spin,” Phys. Rev. Lett. 75, 3926–3929.
Du, R. R., et al. (1999). “Strongly anisotropic transport in higher twodimensional Landau levels,” Solid State Commun. 109, 389–394.
Eisenstein, J. P., et al. (1992). “New fractional quantum Hall state in double-layer two-dimensional electron systems,” Phys. Rev. Lett. 68, 1383–1386.
Girvin, S. M., MacDonald, A. H., and Platzman, P. M. (1985). “Collective Excitation Gap in the Fractional Quantum Hall Effect,” Phys. Rev. Lett. 54, 581–583.
Goldman,V.J.,Santos,M.,Shayegan,M.,andCunningham,J.E.(1990). “Evidence for two-dimensional quantum Wigner crystal,” Phys. Rev. Lett. 65, 2189–2192.
Goldman, V. J., Su, B., and Jain, J. K. (1994). “Detection of composite fermions by magnetic focusing,” Phys. Rev. Lett. 72, 2065–2068. Goldman, V. J. (2000). “The Quantum Antidot Electrometer: Direct Observation of Fractional Charge,” J. Korean Phys. Soc., in press.
Haldane, F. D. M. (1983). “Fractional Quantization of the Hall Effect: A Hierarchy of Incompressible Quantum Fluid States,” Phys. Rev. Lett. 51, 605–608.
Halperin,B.I.(1983).“TheoryofthequantizedHallconductance,”Helv. Phys. Acta 56, 75–86.
Halperin,B.I.,Lee,P.A.,andRead,N.(1983). “Theoryofthehalf-filled Landau level,” Phys. Rev. B47, 7312–7343.
Heinonen, O. (ed.) (1998). “Composite Fermions,” World Scientific, New York.
Jain, J. K. (1989). “Composite Fermion Approach for the Fractional Quantum Hall Effect,” Phys. Rev. Lett. 63, 199–202. Jain, J. K., and Kamilla, R. K. (1998). Chapter 1 in Heinonen, O. (ed.) “Composite Fermions,” World Scientific, New York. Jain, J. K. (2000). “The Composite Fermion: A Quantum Particle and Its Quantum Fluids,” Physics Today 53(4), 39–45.
Jeckelmann, B., Inglis, A. D., and Jeanneret, B. (1995). “Material, Device, and Step Independence of the Quantized Hall Resistance,” IEEE Transactions on Instrumentation and Measurement, 44, 269–272. Jeffery, A., et al. (1998). “Determination of the von Klitzing constant,” Metrologia 35, 83–96.
Jiang, H. W., et al. (1990). “Quantum liquid versus electron solid around ν =1/5 Landau-level filling,” Phys. Rev. Lett. 65, 633–636.
Kalmeyer, V., and Zhang, S. C. (1992). “Metallic phase of the quantum Hall system at even-denominator filling fractions,” Phys. Rev. B46, 9889–9892.
Kang, M., et al. (2001). “Observation of Multiple Magnetorotons in the Fractional Quantum Hall Effect,” Phys. Rev. Lett. 86, 2637–2640.
Kang, W., Stormer, H. L., Pfeiffer, L. N., and West, K. W. (1993). “How real are composite fermions?” Phys. Rev. Lett. 71, 3850–3853.
Kohmoto, M. (1985). “Topological Invariant and the Quantization of the Hall Conductance,” Ann. Phys. 160, 343–353.
Koulakov, A. A., Fogler, M. M., and Shklovskii, B. I. (1996). “Charge DensityWaveinTwo-DimensionalElectronLiquidinWeakMagnetic Field,” Phys. Rev. Lett. 76, 499–502.
Lam, P. K., and Girvin, S. M. (1984). “Liquid-solid transition and the fractional quantum-Hall effect,” Phys. Rev. B30, 473–475.
Laughlin, R. B. (1981). “Quantized Hall conductivity in two dimensions,” Phys. Rev. B23, 5632–5633.
Laughlin, R. B. (1983). “Anomalous Quantum Hall Effect: An Incompressible Quantum Fluid with Fractionally Charged Excitations,” Phys. Rev. Lett. 50, 1395–1398.
Lilly, M. P., et al. (1999). “Evidence for an Anisotropic State of TwoDimensional Electrons in High Landau Levels,” Phys. Rev. Lett. 82, 394–397.
Lopez, A., and Fradkin, E. (1991). “Fractional quantum Hall effect and Chern-Simons gauge theories,” Phys. Rev. B44, 5246–5262. Moore, G., and Read, N. (1991). “Nonabelions in the fractional quantum Hall effect,” Nucl. Phys. B360, 360–396.
Niu, Q., Thouless, D. J., and Wu, Y. S. (1985). “Quantized Hall conductance as a topological invariant,” Phys. Rev. B31, 3372–3377.
Park, K., and Jain, J. K. (2000). “Two-Roton Bound State in the Fractional Quantum Hall Effect,” Phys. Rev. Lett. 84, 5576–5579.
Pinczuk, A., Dennis, B. S., Pfeiffer, L. N., and West, K. (1993). “Observation of collective excitations in the fractional quantum Hall effect,” Phys. Rev. Lett. 70, 3983–3986.
Prange, R. E., and Girvin, S. M. (eds.) (1990). “The Quantum Hall Effect,” Springer-Verlag, New York.
Saminadayar, L., Glattli, D. C., Jin, Y., and Etienne, B. (1997). “Observation of the e/3 fractionally charged Laughlin quasiparticle,” Phys.
Rev. Lett. 79, 2526–2529.
Scarola, V. W., Park, K., and Jain, J. K. (2000). “Rotons of composite fermions: Comparison between theory and experiment,” Phys. Rev. B61, 13064–13072.
Shankar, R., and Murthy, G. (1997). “Towards a Field Theory of Fractional Quantum Hall States,” Phys. Rev. Lett. 79, 4437–4440.
Sondhi, S. L., Karlhede, A., Kivelson, S. A., and Rezayi, E. H. (1993). “Skyrmions and the crossover from the integer to fractional quantum Hall effect at small Zeeman energies,” Phys. Rev. B47, 16419–16426.
Stormer, H. L., and Tsui, D. C. (1996). Chapter 10 in Das Sarma, S., Pinczuk, A. (eds.) “Perspectives in Quantum Hall Effects,” Wiley, New York.
Suen, Y. W., et al. (1992). “Observation of a ν =1/2 fractional quantum Hall state in a double-layer electron system,” Phys. Rev. Lett. 68, 1379–1382.
Thouless, D. J., Kohmoto, M., Nightingale, M. P., and den Nijs, M. (1982). “Quantized Hall Conductance in a Two-Dimensional Periodic Potential,” Phys. Rev. Lett. 49, 405–408.
Tsui, D. C., Stormer, H. L., and Gossard, A. C. (1982). “TwoDimensionalMagnetotransportintheExtremeQuantumLimit,”Phys. Rev. Lett. 48, 1559–1562.
Von Klitzing, K., Dorda, G., and Pepper, M. (1980). “New Method for High-Accuracy Determination of the Fine-Structure Constant Based on Quantized Hall Resistance,” Phys. Rev. Lett. 45, 494–497.
Wen, X. G. (1990). “Chiral Luttinger Liquid and the Edge Excitations in the Fractional Quantum Hall States,” Phys. Rev. B41, 12828–12844.
Willett, R. L., Ruel, R. R., West, K. W., and Pfeiffer, L. N. (1993). “Experimental demonstration of a Fermi surface at one-half filling of the lowest Landau level,” Phys. Rev. Lett. 71, 3846–3849.
Willett, R. L., et al. (1987). “Observation of an even-denominator quantum number in the fractional quantum Hall effect,” Phys. Rev. Lett.
59, 1776–1779.
 
 
Quantum Mechanics
 
Albert Thomas Fromhold, Jr.
Auburn University
I.	Classical Model of the Atom
II.	Special Relativity
III.	Quantum Concepts
IV.	Wave Motion
V.	Wave–Particle Duality
VI.	Wave Equations for Particles
VII.	Quantum Mechanical Current Densityand Particle Beams
VIII.	Bound-State Problems
IX.	Electron Transport in Solids
X.	Summary
GLOSSARY
Eigenfunction Wavefunction for a specific stationary state of a physical system.
Eigenvalue Specific value of a physical quantity corresponding to a specific eigenfunction.
Eigenvalue equation Particular mathematical relation in which a mathematical form, known as an operator, acts on an eigenfunction to produce the corresponding eigenvalue multiplied by the eigenfunction.
Excited states States of a system having energies above the ground state.
Exclusion principle Statement that no two identical particles of a particular statistical type can simultaneously occupy the same quantum state.
Ground state Lowest energy state of a system.
Hermitian operator A mathematical operator having real eigenvalues, which is a necessary condition for
it to be capable of representing a physical observable.
Lifetime Mean time before an excited state spontaneously decays to another state, such as the ground state.
Particlelike Localizedandactinginanindividualmanner as an entity.
Probability density Relative probability of a particle being at a specified position in space; alternately, the relative probability of some other physical quantity, such as momentum.
Quantization Discrete value or set of values for a physical quantity, such as energy or angular momentum.
Stationarystate Specific state of a physical system characterized by the fixed value of some physical quantity, such as energy.
. 	359
Time-dependent Schro¨dinger equation Equation for determining the time-dependence and spacedependence of the eigenfunctions for a system.
Time-independent Schrodinger equation¨ Eigenvalue equation used to obtain energy eigenvalues and energy eigenfunctions for a system.
Uncertainty relation Mathematical form relating the maximum precision of measurement of some physical quantity, such as position or energy, to the precision of some related quantity, such as momentum or time.
Wavefunction A mathematical form, usually complex, used to deduce the probability density.
Wavelike Nonlocalized and periodic, with the capability of interacting constructively or destructively.
Wave–particle duality Coexistence of wavelike and particlelikeaspectsinaphysicalentity,suchasanelectron.
QUANTUM MECHANICS is a theory that is capable of predicting the behavior of atomic and subatomic systems. In fact, it is the only theory to date that is adequate for the microscopic domain in nature. Quantum mechanics not only correctly predicts the results of physical observations in the microscopic world where classical physics is often quite unsuccessful but also leads to valid predictions in the macroscopic world experienced by human senses.
I. CLASSICAL MODEL OF THE ATOM
A.	Structure of the Atom
Ernest Rutherford’s (1871–1937) interpretation of his extensive scattering experiments in 1911 gave overpowering evidence that atoms consist of a dense, positively charged nucleus surrounded by a cloud of electrons. The electron had been discovered a few years earlier in 1887 by Joseph John Thomson (1856–1940), who attributed a definite charge-to-mass ratio to the particle. Before the discovery of the wave-like properties of the electron in 1927 by George Paget Thomson (1892–1975), the son of J. J. Thomson, it was expected that the mechanical properties of atoms could readily be explained by applying classical mechanics in a straightforward way to this model. In fact, the successful model of planetary motion around the more massive sun, under the action of gravitational forces between the planets and the sun, and the perturbations to such motion due to the gravitational forces between planets, provide the closely related classical analog model for describing the motion of electrons about a single, massive nucleus: the electrical forces between charged particles replace the gravitational forces in the solar system.
The forces between electrons are repulsive instead of attractive, and these repulsive forces are of the same order of magnitude as the attractive forces between an electron and the nucleus. Therefore these forces between electrons are not merely perturbations, as is the case for the gravitational forces between planets orbiting the sun.
However, it was expected that the hydrogen atom, containing only a single electron and thus free of the repulsive Coulomb force between electrons in two-electron and many-electron atoms, should be easily amenable to treatmentbyclassicalmechanics.Themodelisasimplepicture in which the single electron orbits the far more massive proton nucleus under the action of a centripetal force provided by the attractive electrical force between electron and nucleus.
B.	Classical-Mechanical Treatmentof the Single-Electron Ion
Let us consider the more general case of a single electron atom or ion, where the charge of the nucleus is Ze, with the quantity e representing the magnitude of the electron charge. For the hydrogen atom, Z =1. The electrical force between a nucleus of charge Ze separated by a distance r from an electron of charge −e has magnitude
KZe2
FE =	 2 ,	(1) r
where K is a constant that for SI units has the value
	K ,	(2)
where ε0 is the electric permittivity of free space having the value 8.854×10−12 farad/meter (F/m). Let us make the assumption here that the nucleus is stationary and the electron travels around the nucleus. Although this view is absolutely correct in classical mechanics only if the nucleus is infinitely massive, it can be shown to be approximately correct whenever the nucleus is much more massive than the electron, and this is satisfied for all oneelectron ions. Thus, we consider the radius of the electron orbittobeequaltothedistanceseparatingtheelectronand the nucleus; corrections for deviations caused by the finite nuclear mass can easily be incorporated into the treatment atalaterstage.Theelectricalforceprovidesthecentripetal force mv2/r, which causes the electron to travel in the hypothesized circular orbit, m being the electron mass and v being the electron speed, so that
mv2 KZe2 r = r2
	.	(3)
This at once gives the following nonrelativistic expression for the kinetic energy K of the electron:
	K = 1 mv2 =  KZe2 .	(4)
	2	2r
The potential energy P associated with the Coulomb force is given by
so that	P =	r
−KZe2
	,	(5)
	K .	(6)
The sum of potential and kinetic energies gives the total energy T:
T  . (7)
The kinetic energy is intrinsically positive, as can be noted from Eq. (4), so that the total energy is negative. This means that the electron is bound to the nucleus. As the electron separation from the nucleus increases, the potential energy algebraically increases toward zero. If the electron cannot separate to an arbitrarily large distance from the nucleus, we say that it is bound to the nucleus.
The centripetal force relation given by Eq. (3) relates the electron speed v to the radius r of the classical orbit, so that
KZe2
r =  	(8) mv2
or, equivalently
	v .	(9)
The rotation angular frequency ω is given by
v
ω =   = . (10) r	mr3
This development not only allows the kinetic energy to be expressed in terms of the radius, as given by Eq. (4), it also allows the angular momentum L = pr =mvr for an electron in a circular orbit to be expressed in terms of the radius,
L = pr = mvr = mr  (KZe2mr)1/2.
(11) Equivalently, this gives the radius in terms of the angular momentum
L2
	r =  ,	(12)
KZe2m
which can then be substituted into Eq. (9) to give the speed in terms of the angular momentum
	KZe2	KZe2m	1/2	KZe2
v	 . (13) m	L2	L
The kinetic energy in terms of the angular momentum is then given by
	1	mK 2 Z2e4
	K  mv 	(14)
Equations (1)–(14) are based entirely on classical mechanics.
C.	Electromagnetic Fields Producedby an Orbiting Electron
Let us explore the classical viewpoint a bit further by means of the planetary model of the one-electron atom, where a single electronic charge −e is considered in motionaboutanequal-magnitudechargeofoppositesigndue to the proton. This constitutes a rotating electric dipole, although admittedly the center of rotation is located very near one end of the dipole. This rotating dipole produces a time-varying electric field at distant points in space. The electric field so produced is cyclic, being the same as the rotation frequency of the dipole. An oscillating electric field is thus produced at the observation point, the frequency of the field ν being equal to the frequency of rotation of the dipole. According to classical electrodynamics, the energy associated with this oscillating electric field can propagate outward in space or be absorbed at the field point (e.g., by accelerating the conduction electrons in a metal).
D.	Electromagnetic Radiation Predictionsof Classical Physics
The energy radiated away or absorbed from a rotating dipole source, as previously described, must come at the expense of the potential energy of the configuration of the two charges if it is not supplied by some source connected with the rotation of the dipole. For a hydrogen atom, there is no such source. The consequent decrease in total energy of the electron in the one-electron atom would mean that the total energy becomes more negative, which corresponds to an increase in the kinetic energy of the electron in accordance with Eq. (7). This corresponds to a decrease in the radius of the electron orbit and to an increase in the rotation frequency according to Eqs. (4) and (10). On the basis of this classical model of radiation, the frequency of the radiated electromagnetic wave would then increase. The changes which occur would thus be continuous; that is, since there could be arbitrary values for the radius of each electron orbit, the electron would be capable of having any one of a continuous range of values of kinetic energy. This speed could be changed continuously by adding or extracting arbitrarily small quantities of energy. As the speed and frequency of rotation change, corresponding continuous changes occur in the radius of the orbit. According to classical electrodynamics, an acceleratedchargeradiatesenergy,sothepotentialenergyof theelectronwouldsteadilydecrease.Thisultimatelyleads to a catastrophe: there would be theoretically no limit to theprocess,evenasthetotalenergyoftheelectron–proton systemapproachednegativeinfinity,withtheconsequence that an infinite amount of energy would be radiated away.
E.	Logical Failure of Classical Mechanics
Clearly, the results deduced on the basis of the classical modelareunreasonable.Inaddition,thepredictionsdonot correspond in any way to the experimental observations of optical spectra, which are not continuous, but instead contain many sharp spectral lines. Hence, this classical model cannot be used to describe the mechanical properties of an atom.
The true state of affairs is that all atoms have a lowest energy state, labeled the ground state by Niels Henrik Bohr (1885–1962), for which no further energy emission ispossible.Furthermore,evenwhileinsomegivenhigherenergy configuration, the atom does not emit energy continuously; excited states emit energy only sporadically, each such event being accompanied by a sudden jump to a lower-energy configuration. Bohr called the various discrete energy states of an atom stationary states, since such states are stable until the time when a transition to a lower-energy state actually takes place.
Thelogicaldeductionfromthepreviousdiscussiononly can be that the classical approach, which is so successful for describing the motion of the planets, fails completely for the hydrogen atom. So much for arguing by analogy! Moreover, the failure of classical mechanics for the hydrogen atom is manifested not in our lack of ability to see and follow the electron, because it might be too tiny to be seen with the eye or even with a microscope, but instead in experimentalmeasurementsyieldingdatasuchasthelight spectrum emitted by excited gases of atoms. The observed spectra can in no way be explained without additional assumptions quite foreign to classical mechanics.
Even considered statistically, an attractive, inverse square force, as typified by Eq. (1) for the Coulomb electric force, leads to a negative potential energy that varies inversely with the separation distance between charges (or of masses, in the case of gravitational forces). The potential energy is conservative, meaning that a decrease in separation distance yields energy that can be extracted by an external agency or converted into heat. If the separation distance can be imagined to decrease to zero, then the potential energy approaches negative infinity. This implies thataninfiniteamountofenergysimultaneouslywouldeither be extracted or be converted into heat. Conceptually, all machines in the world could be run for a day, a month, a year, or even as long as one wishes, by allowing an electron to come closer and closer to a proton in a controlled manner. This means that in the original creation of the oppositecharges,aninfiniteamountofenergywasexpended. Alternately, we could imagine an explosion dwarfing even that of the most powerful fission or fusion weapon available today coming about by merely allowing or triggering the collapse of a configuration of two point charges of opposite sign. Such incomprehensible conclusions resulting from pushing the classical model to its logical endpoint are sufficient in themselves to force us into the realization that nature actually must behave under constraints additional to those contained within the formalism of classical mechanics.
To bring in evidence bearing on this matter, electron– positron pairs can be produced from gamma rays, and it is known from these experiments on pair production that an infiniteamountofenergyisnotrequiredtoseparatetheoppositely charged particles so produced. In fact, the γ-ray energy required is only of the order of the rest mass energiesoftheelectronandthepositron.Likewise,pairannihilation does not lead to the emission of an infinite quantity of γ-ray energy, so again we must conclude that the negative Coulomb energy must be restricted by nature to have a finite magnitude. This end could be accomplished by restricting the separation distance between opposite charges to some minimum, nonzero value corresponding, perhaps, to the electron–proton separation distance in the so-called ground-state configuration of the hydrogen atom.
F. New Foundations of Mechanics
It is important to note that classical mechanics does provideagenerallyadequatetheoreticaldescriptionofmotion forallobjectsthatcanbeseeninanordinarywaytraveling at ordinary speeds. By “ordinary,” we mean observable to the human eye and traveling at speeds low enough to be able to follow the position of the object with the eye. In fact, the theory is found to apply even in the domain of far smaller particles, such as can be seen only with the aid of an optical microscope, as long as the speed is well below that of light propagation. However, the extremely versatile framework provided by classical mechanics yields inaccurate results in two domains, which can be distinctly different: (i) particles traveling at speeds approaching the speed of light and (ii) particles having very tiny masses.
First of all, objects traveling at speeds v of the order of 0.1c or larger manifest marked departures from Isaac Newton’s (1642–1727) predictions based on a fixed mass. Thisisduetotherelativisticdependenceofmassonvelocity. Second, very small mass particles, such as the smaller atoms and nuclei (e.g., the hydrogen and helium atoms, proton, neutron, and α-particle) and especially the even less massive electrons, all exhibit diffraction properties typical of wavelike phenomena.
In both of these domains—namely, the domain of very fast particles and the domain of very tiny particles— entirely new forms of mechanics were erected that had essentially different premises than those inherent in classicalmechanics.Thiswasnecessarybecauseclassicalmechanics simply fails to describe and correctly predict the motions and trajectories of objects under such conditions. The domain listed in (i), very high-speed motion, requires the use of Albert Einstein’s (1879–1955) theory of special relativity (1905). The domain listed in (ii), very smallmass particles, requires the use of the theory of quantum mechanics, the subject of this article.
Special relativity and quantum mechanics constitute a pair of theories that enable one to make accurate calculations in the separate domains listed. The relativistic mechanics provided by Einstein’s theory of special relativity accurately describes and predicts motions of particles and bodiesmovingwithspeedsapproachingthespeedoflight; quantum mechanics describes and predicts experimental observations for very tiny particles, atoms, and the properties of ensembles of atoms. Einstein’s theory of special relativityalone,however,isunabletoaccountforthepropertiesofatomsandthediscretenessoftheemittedradiation that constitute the optically observed atomic spectra.
For very small-mass particles traveling at relativistic speeds, more complicated theories (relativistic quantum mechanics) have been formulated that have had their successes, one of the most prominent being Paul Adrien Maurice Dirac’s (1902–1984) theory predicting the existence of the positron. Ideally, one would like to have a very general framework that not only predicted the motion of particles correctly for each of these domains but also gave the correct results under more ordinary conditions in which classical mechanics already does a completely satisfactory job. It must be admitted, however, that the basis for a perfectly general theory of mechanics, if it is within the province of human beings to conceive, still remains to be developed. Even Einstein’s general theory of relativity does not contain the power to interpret the microscopic world but, instead, gives answers to cosmological questions relating to the macroscopic world. Simply put, no completely general theory exists today.
II. SPECIAL RELATIVITY
A. Essential Relations for Quantum Mechanics
Becausespecialrelativityiscoveredadequatelyinanother part of this encyclopedia, only the relationships essential for the present development are presented here. It is vital to point out that the profound prediction by Einstein of the variation of the measured mass of an object with its speed has immediate implications for motion which are quite contrary to those predicted by Newton’s second law, applied in the restricted sense of a fixed, unvarying mass for any given object. Contained within the theory of special relativity is not only the experimentally observed mass variation with speed but also the concept of the equivalence of mass and energy. The latter concept, which is directly verified in electron–positron pair production, has of course far-reaching consequences with regard to presentday energy production.
Definingthevelocityvasavectorwithmagnitudeequal to the speed and pointing in the direction of motion, the momentum p is then simply
	p = mv.	(15)
Newton considered the mass m to have a fixed value m0. The acceleration a is defined as the time rate of change of the velocity
dv
a =  .	(16) dt
Newton’ssecondlawF=m0athuscanbewritteninterms of the time rate of change of the momentum
dp
F =  .	(17) dt
Thisformisvalideveninspecialrelativity,asareNewton’s first and third laws. Time t, however, is not absolute in special relativity as it is within the framework of Newton’s formalism.Also,weknowfromspecialrelativitythatmass m depends upon speed in accordance with
	m = γm0,	(18)
where m0 is referred to as the rest mass and the parameter γ isdeterminedbyv/c,theratioofthespeedoftheparticle to the speed of light, in accordance with
	 .	(19)
Energy is related to mass m in special relativity:
	 = mc2.	(20)
This relation holds true for any speed v. When v =0, this reduces to the rest mass energy
	0 = m0c2.	(21)
The energy versus momentum relation for a free particle in special relativity is
	 ,	(22)
which differs from the energy–momentum relation in Newtonian mechanics.
Energy–momentum relations are needed to develop the deBroglierelation,whichunderliestheSchrodingerequa-¨ tion of quantum mechanics.
B. Philosophical Implications
There is unquestionably a great philosophical difference between Einstein’s special relativity and modern-day quantum mechanics. It is unlikely that Einstein could have foreseen in 1905, the year of publication of his works on special relativity and the photoelectric effect, the great philosophical differences that eventually would split the quantum way of thinking from the relativity way of thinking.Relativisticmechanics,likeclassicalmechanics,leads to a world view of an absolutely predictable future, at least in principle, based on the specified state of the universe at any given time. Quantum mechanics, on the contrary, contains an intrinsic margin of uncertainty regarding the future evolution of the system, even if the state of the universe is known as completely as possible at any given time. For example, descriptions of the motion of an electron by Newtonian and Einsteinian mechanics are both quite precise, although not necessarily in agreement with each other, in predicting a specific position and velocity at a time t whenever the exact position and velocity at any other time t are specified as well as all forces that act on the particle in the time interval between t and t. Quantummechanics,ontheotherhand,givesonlyrelative probabilities for a broad range of possibilities.
One must be flexible enough to accept experimental facts and not reject, for example, relativistic mechanics simply because one dislikes the concept that the masses of objects vary with speed. In the same way, experimental demonstration of the wave properties of matter requires thattheoreticalformulationsbebroadenedtoincludethese properties. This leads in a natural way to the concept of indeterminism.
The lack of determinism inherent in quantum mechanics was the “Achilles heel” that eventually led Einstein to the conclusion that quantum mechanics provides, at best, an incomplete description of the universe. His powerful intuition, which should not be lightly discounted, led him to the belief that quantum mechanics more than likely would be superseded eventually by a more complete theory, completely deterministic in form, which would allow exactpredictionsofthecompletefutureevolutionofasystem, given only the initial conditions at some prior point in time. This viewpoint, which means that nothing is left to chance, was hotly disputed by prominent contemporaries of Einstein. It would seem to belie even the possibility of free will in humans. Max Karl Ernst Planck (1858–1947) and Dirac, on the contrary, believed that the uncertainty inherent in quantum mechanics was in fact an intrinsic reality in nature, never to be overcome by any better theory purported to be more comprehensive or general. For these philosophically minded physical theorists, the important uncertaintyprincipleiselevatedfromitsroleasanintegral part of quantum mechanics theory to an even more lofty philosophical principle.
Philosophicalspeculation,ofcourse,isnotphysics.One shouldaskdifferentquestions,suchashowtobestdescribe and predict experimental observations in a logical manner frommodelsdevelopedfromacombinationofobservation and intuition. To go beyond this end by inquiring why nature behaves in such a fashion can prove interesting and stimulating but does not, in itself, constitute the furthering of the subject proper of physics.
The best approach is to develop formulations that represent a synthesis of all experimentally verified properties of matter, including variation of mass with velocity and wavelike interference of particles. The roots of the most fundamental relation (the de Broglie relation, developed by Louis Victor de Broglie) in the wavelike description of particles are to be found most naturally in Einstein’s explanation of the photoelectric effect and in the equations of special relativity. It is an enigma that the seeds of quantumtheoryliewithinoneofEinstein’screativeexplanations of a very puzzling experimental observation, the photoelectric effect. The enigma arises from the fact that Einstein’s best-known work, the theory of special relativity, is an entirely separate and remarkably different theory philosophically from that of quantum mechanics.
III. QUANTUM CONCEPTS
A.	Early Quantum Theory
Old quantum theory is essentially the patchwork of classical and quantum ideas that were pieced together to yield Planck’s theory of black-body radiation, Einstein’s explanation of the photoelectric effect, and Bohr’s theory of the one-electron atom. Old quantum theory included the concept of the particle nature of radiation (i.e., the photon) and the quantization of the radiation energy in elemental units hν. However, it did not include the concept of the wave nature of matter.
B.	Einstein’s Concept of Lightas an Energy Quantum
The origin of the word “quantum” in quantum mechanics can be understood from its use in the explanation of some ofthepropertiesoflight.ItwasEinstein,inhisexplanation of the interaction of light with metal surfaces, who gave impetus to the concept that electromagnetic radiation is made up of discrete increments of energy. At that time (1905), light was generally considered to be an electromagnetic wave somewhat similar to water waves or sound waves, with an accompanying energy density that could lead to energy exchange with another body. A light wave in free space may be viewed classically as coupled, timedependent electric and magnetic fields that are in phase, each varying periodically in time and space. This leads to signal propagation through free space and material media. The electric field of the wave leads to an electric force on charged particles; charged particles can thus be accelerated and thereby gain kinetic energy at the expense of the energy density of the electromagnetic wave. This picture leads to the prediction of electrons in a solid being accelerated to various energies, depending upon the acceleration time, with no sharp cutoff for the maximum energy that can be attained and with no indication that there should be a wavelength- or color-dependence of the effect. It also leads naturally to the conclusion that a more intense light wave of the same wavelength should exert a larger electric force and hence produce more acceleration and consequently higher-energy electrons. In addition, it might be expected that if the light is of extremely low intensity, there would be a measurable time delay before the electron could gain sufficient energy to overcome the surface energy barrier (given by the workfunction) and thereby escape from the metal.
Theclassicalpredictionsfortheinteractionoflightwith solids were not in accord with the experimental data. No timedelaywasobserved.Electronemissionfromthemetal surface was either observed or not observed, depending upon whether the wavelength was less than or greater than some critical wavelength characteristic of the metal used for the experiment. Furthermore, all emitted electrons had a kinetic energy equal to or less than a given maximum energy that increased with the wave frequency. (The wave frequency ν is given by c/λ, where c is the speed of light and λ is the wavelength; it is also the reciprocal of the time period of the oscillation and thus typically has units of cycles per second, termed Hz.)
Einstein pointed out that all of these observations could be explained in a neat way by postulating that the energy transfer between light wave and electron occurs only in well-defined, discrete quantities of size hν, with h being the fundamental constant introduced by Planck in the year 1900 to resolve the black-body radiation spectrum problem. According to this postulate, light is quantized in elemental units of energy that are incapable of further decomposition. From this viewpoint, the properties of light are similar to the properties of elemental particles, such as the electron and the proton, which have basic units of
 
FIGURE 1 Photoelectric effect. [Fig. 1.1 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the author.]
mass and charge of specific values that are ordinarily incapable of further decomposition. The energy hν of each light quantum, called a photon, could be transferred to a conduction electron in the metal to enable it to escape from the metal with a kinetic energy given by
	K = hν − φ,	(23)
where the workfunction φ is the energy step that must be overcome by the electron at the metal surface in order to become free. The action of the photon in promoting electron emission from a metal is illustrated in Fig. 1.
The idea that light has particlelike properties was in one sense a resurrection of the corpuscular theory of light espoused by Newton. Since that theory had long been abandoned, in view of the wavelike properties of diffraction and interference later discovered by Christian Huygens (1629–1695), the particlelike picture invoked by Einstein to explain the photoelectric effect was once again revolutionary. Even Planck, who had chanced upon the explanation of the black-body radiation spectrum by introducing the concept that the radiation in a cavity could only have discrete values for the energy, did not believe that the discreteness was associated with light in any fundamental way. Instead, Plack believed initially that the discreteness proceeded only from constraints on the absorption and emission of radiation by the cavity walls themselves. Light itself generally was viewed as a wave phenomenon, with periodic variations in the electric and magnetic fields but no sharp discontinuities in space and time. To postulate, as Einstein did, that the energy could be localized in space such that it could be exchanged with the electron in a metal instantaneously and in discrete quantities, when the wave nature of light already had been experimentally confirmed, was quite revolutionary.
Indeed, it was nearly akin to postulating that light had dual properties.
C. Transitions between Atomic States; Photon Emission
Lookingintothephenomenonoflightproductioninalight source (i.e., the origin of optical spectra), one is led to the concept of excited states of the atoms in the source. An atombecomesexcitedwhenitabsorbsenergyinsomeway (e.g., from the heat associated with a rise in temperature). Such an excited atom can give off energy in the form of a light wave or, more generally speaking, by emitting some form of electromagnetic radiation. From the viewpoint of classical mechanics, the atom can have a continuous range of energies in the excited state and therefore can emit a continuous range of electromagnetic wave energies. [See, for example, Eqs. (4), (7), and (14).] The optical absorption and emission spectra, from this classical viewpoint, would be quite nondescript and, moreover, would vary little from element to element in the periodic table. Such simplicity, however, is belied by the experimental optical spectra. The optical spectrum obtained from a gas discharge is usually very complex, and it is so characteristic of the atoms making up the gas that it can serve as a “fingerprint”identifieroftheelementmakingupthegas.From a classical view the most unexpected characteristic of the experimental optical spectrum is the sharpness of peaks in intensity at certain wavelengths (or frequencies). Such peaks are difficult or impossible to explain on the basis of a classical mechanics picture of the atom.
IfEinstein’sviewoflightascomposedofdiscretequantities of energy is to be sustained, then it is natural, if not absolutely necessary, to conclude that these entities are produced by the atoms in the light source. The relationship between light wave frequency and the light quantum energy existent in the photoelectric effect leads one to speculate on the reason for the sharp emission spectrum at certain wavelengths in optical spectra. The spectra, which are so characteristic of the atoms comprising the source, must indicate that the changes in the atom configuration leading to light emission occur in such a way that individual quanta of energy hν are created and emitted. Figure 2 illustrates the concept of energy absorption and energy emission. The energy hν of the photon emitted, for example, is the difference in energy between the initial state n and the energy of the final state n of the quantum system given by
	h .	(24)
The experimentally unconfirmed expectation on the basis of classical mechanics that the optical spectrum should be rather more or less continuous, with no sudden, sharp
 
FIGURE 2 Quantum transitions involving photon absorption and emission.[Fig.1.5inQuantumMechanicsforAppliedPhysicsand Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the author.]
changes in intensity with wavelenght, therefore had to be superseded by the view that the changes in the mechanical configuration are catastrophic and instantaneous. Classically, a sudden change in the total energy of an inversesquare force system must be accompanied by a sudden change in the radius of the orbit and also a corresponding changeintherotationfrequencyoftheparticleintheorbit. [See Eqs. (4), (7), and (10).] The accompanying change in the energy therefore must occur suddenly, the difference in energy between the two characteristic configurations determining the energy of the emitted photons. The mechanical states of the physical system are thus specific and characterized by fixed energies, with the transition between any two such fixed energy states occurring suddenly with the emission of a fixed quantum of energy. Collapse must occur from one characteristic configuration to another characteristic configuration of lower energy when thephotoniscreated.Eachconfigurationmayindividually becomparedtotheintricateworkingsofafinewatch,with the change in configurations occurring as a sudden transition between two well-defined and self-regulated states.
D. Intensity Peaks in Optical Spectra
The resonance nature of the absorption and emission of electromagnetic radiation by gases found experimentally requiresrejectionofthesimpleclassicalpictureofanatom derived from a planetary model of one or more electrons revolving about the nucleus. One is led to the viewpoint that only certain characteristic mechanical configurations of the electrons in an atom are allowed. This provides a plausible explanation of why radiation energy can be abstracted only in units of quanta hν of radiation energy. The total energy therefore always changes by discrete photonenergy increments hν. To the extent that the electron can be viewed as changing speed in its orbital motion to yield the emission of energy, that change in speed must occur in a single-step process. Clearly, an entirely new type of mechanics is required for the description of atomic systems having such properties. Due to the discreteness of the stationary states and the quantum nature of the energy emitted as photons, this new type of mechanics was called quantum mechanics.
E. Ideas of de Broglie, Heisenberg, and Schrodinger¨
Matter was discovered in 1927 to have wavelike properties by means of the electron diffraction experiments of Clinton Joseph Davisson (1881–1958) and Lester Halbert Germer (1896–1971), and G. P. Thomson (1892–1975). This was preceded (1923) by de Broglie’s deduction from special relativity considerations that a particle of energy hν and momentum p had a wavelength λ associated with it. In the same way that electromagnetic radiation can be observed to behave in a wavelike manner under certain conditions and in a particlelike manner under other con-
ditions (witness radio-wave interference on the one hand and the photoelectric effect on the other), de Broglie postulated that there was a wave–particle duality for all of nature. Wave–particle duality asserts that nonzero mass particles, such as electrons, protons, neutrons, and atoms, can be observed to behave in a wavelike manner under the proper conditions and in a particlelike manner under different conditions.
This very important concept of particles possessing an intrinsic wave character underlies the Schrodinger¨ equation—that cornerstone of present-day quantum mechanics dating from 1926. The birth of quantum mechanics, in fact, dates to the developments of Werner Karl Heisenberg (1901–1976) in 1925 and of Erwin Schrodinger (1887¨ –1961) in 1926, both of which intrinsically contain the wave properties of matter, although somewhat differently. Whereas Schrodinger directly de-¨ veloped a wave equation to describe the behavior of matter, Heisenberg incorporated the wave properties into a theory in a somewhat different way, setting up a noncommuting matrix operator formulation. Heisenberg was able to show that certain pairs of physical observables representedbynoncommutingoperators,inprinciple,couldnot be measured to arbitrary precision; rather, the more precise the measurement of one member of the pair was, the less precise the knowledge of the other would be. Thus was born the Heisenberg uncertainty principle. This type of uncertainty follows naturally from a wavelike description of matter such as that represented by the Schrodinger¨ equation. The Schrodinger formulation can be used to de-¨ duce a matrix formulation of quantum mechanics analogous to Heisenberg’s formulation, so in this sense the two theories are equivalent.
F. Bohr Quantized Energy Levels for Hydrogen Atom
It is remarkable that Bohr was able to put together a successful theory of the hydrogen atom, since its formulation in 1913 predated by more than two decades the discovery of the wave diffraction of particles and even predated by a decade the postulate of wave–particle duality by de Broglie and his deduction that a particle of momentum p has a wavelength λ associated with it. Fundamentally, Bohr utilized the data given by experimental optical spectratogetherwithheuristicargumentsbasedontheclassical limit.Asomewhatdifferentlineofreasoning,basedonthe experimentally confirmed de Broglie relation, is followed here in deducing the quantized energy levels of Bohr.
As a preliminary to the development of the Schrodinger¨ equation utilizing the experimentally verified de Broglie relation
h
λ =  	(25) p
between the wavelength λ associated with a particle and the momentum p of that particle, where h is Planck’s constant having the value 6.6262×10−34 Joule-second (J-s), let us use that same relation as a selection device for choosing a series of discrete orbits for an electron imagined to circle a proton from the continuous range of orbits allowed in the purely classical planetary model of theone-electronatom.Thekeyadditionistherequirement that a wave associated with a trajectory must be a singlevalued function of position on the trajectory. For a circular orbit, this requires that the wavelength be commensurate with the circumference of the orbit, namely
2πr
	 n,	(26)
where r is the radius of the circular orbit, λ is the wavelength, and n is any integer ≥1. Note that no attempt is made to interpret the meaning of the wave, which is assumed to exist around the circumference of the orbit; instead, only one of the most general properties of waves (i.e., single-valuedness) is relied on when writing the condition given by Eq. (26). The logic of this approach is merely that if the properties of matter are wavelike and if a planetary orbit exists, then the condition given by Eq. (26) shouldbemet.Laterinthetreatmentofthehydrogenatom by means of the Schrodinger equation, the concept of a¨ well-defined planetary orbit will be found to be too naive, except in what is designated the classical limit. This is due to the fact that a wave does not usually have a precise localization. Nevertheless, there do exist well-defined values of the most likely separation distance of the electron relative to the nucleus of the one-electron atom. Substituting Eq. (25) into (26) gives
	2πpr/h = n	(27)
which, in terms of the new constant h defined as
h
	h ,	(28)
takes the form
	pr = nh.	(29)
Because for a circular orbit, the product pr is the magnitudeofthevectorangularmomentumL,Eq.(29)constitutesarestrictiveconditionontheangularmomentum;that is, the values of the angular momentum L are restricted to the discrete set of values Ln given by
	Ln = nh	(n = 1,2,3,...).	(30)
This is a statement of the quantization of angular momentum. Thus, one arrives at the startling conclusion that not only is angular momentum conserved for the one-electron atom, as can be readily deduced from classical mechanics, but also that the new quantum condition establishes that the angular momentum must be quantized. The elemental unit for the mechanical angular momentum is thus h. Because angular momentum quantization proceeds entirely from the wave description, it is a direct consequence of the wave nature of particles.
Now let us show that the quantization of the angular momentum leads to the quantization of the energy values for the one-electron atom. Introducing the quantum condition given by Eq. (30) into Eqs. (12), (7), and (14) gives discrete values for the radius
 
	rn	2m	(31)
KZe
and leads to the following quantized values for the total energy of the Bohr atom
−mK 2 Z2e4
T 
Using 1/(4πε0) for K, this expression for the total energy can be written as
n 
	 	(n = 1,2,3,...). (33)
Thus, the average value of the orbit radius is predicted to increase with an increase in the integer n while the energy increases algebraically from negative values to approach the asymptotic limit of zero corresponding to an unbound state. At the other extreme of small values for n, the negative total energy becomes algebraically smaller, corresponding to tighter binding of the electron and more localization of the electron in the neighborhood of the nucleus. The lowest energy state is given by n =1, so this is the ground state of the one electron atom. Denoting the total energy in this state by 0 gives
	 2e4	2 4
		32π2ε2h2	8ε02h2 .	(34)
0
Substituting the values m =9.1096×10−31 kg, e = 1.6022×10−19 Coulombs (C), h =h/2π =1.0546×
10−34 J-s, and ε0 =8.854×10−12 F/m gives
0 = −Z2 × 2.180 × 10−18 J
	= −Z2 × 13.60eV	(35)
as the ground-state energy in electron volts (eV) for the one-electron atom. For hydrogen, Z =1, so the groundstate energy of the hydrogen atom is predicted to be −13.6 eV. The corresponding Bohr radius, as deduced from Eq. (31), is 0.529×10−10 m. As will be deduced shortly by using these results to examine the predictions foropticalspectra,thetheoryyieldsresultsthatareingood agreement with experiment. Thus, this amalgam of classical mechanics and the assumption of a wavelike character fortheelectroninorbit,asgivenbythedeBroglierelation, leads to a new picture for electrons in atoms.
Needless to say, the electron is too small to be observed directlyinitsorbit,evenifsuchapictureweretenablefrom a fundamental standpoint, so the theory cannot be proved ordisprovedinthisway.Ontheotherhand,opticalspectra can be measured, so optical measurements can serve as a point of contact between microscopic mechanical models of the atom and the world of observation. The predictions of the model therefore can be tested in this manner. In Section III.H, the Bohr theory will be shown to lead to a reasonably accurate explanation for the optical spectra for the one-electron atom.
Despite the success of the Bohr theory for one-electron atoms, it is incapable of giving realistic predictions for atoms having two or more electrons and, a fortiori, fails to giveageneralexplanationoftheperiodictableforthegreat variety of elements to be found in nature. Therefore, it can be concluded that a stronger wave theory is needed for understandingandpredictingnature.Theplanetarymodel, as modified in the simplest possible way by the concept of the wave nature of matter, is sufficiently successful to indicate a promising way to proceed, since it gives some insight into the types of thought processes and concepts required to begin a better treatment.
G. The Heisenberg Uncertainty Relations
There is a still more fundamental problem with the Bohr theory as deduced on the basis of the wave properties of matter inherent in the de Broglie relation. This problem has to do with the basic meaning of the position of an electron on one of the Bohr orbits in the hydrogen atom. The philosophical question is whether or not a physical quantity is actually meaningful if it cannot be measured. TheHeisenberguncertaintyprincipleactuallyimpliesthat thepositionofanelectrononthesmallerorbitsintheBohr model cannot be measured without serious disruption of the electron trajectory itself, as we shall prove later. First of all, let us examine one approach that can be used to rationalize the uncertainty relation.
Let us consider the experimental aspects of a position measurement of the location of a point mass by means of a microscope utilizing electromagnetic waves of wavelength λphoton and frequency νphoton =c/λphoton. It is a well-known fact that the resolution of a microscope is limited by the wavelength of the light utilized for the measurement such that the uncertainty xmass of the position measurement will be of the order of (or greater than) the wavelength:
	xmass ≥ λphoton.	(36)
However, as already discussed, photons have momentum p =h/λ, and the conservation of momentum when the measuring photon scatters off the point mass will cause an uncertainty in the final momentum of the point mass of this order—namely, pmass ≈h/λphoton. Therefore, it must be concluded that, following the measurement,
xmasspmass ≥(λphoton)(h/λphoton)=h. Thus, there is some lower limit to the precision with which the two physical variables of momentum and position of a particle can be measured. This conclusion is consistent with a rigorous version of what is known as the position— momentum form of the Heisenberg uncertainty relation, which states that the minimum value of (x)(p) is of the order of  h. There is no particular limit to the maximum value. Therefore,
	xp .	(37)
Two variables for which the uncertainty relation holds are known as complementary variables.
An alternate pair of complementary variables is given by the energy of a particle in a quantum state and the lifetime of the particle in the state. This means that there is also a lower limit to the product t, where  is the uncertainty of the energy of the particle and t is the uncertaintyinthetimetheparticlewillremaininthatstate.
Thus, in analogy with Eq. (37), t .
For a meaningful electron orbit, the uncertainty in position of the electron must be less than the radius of the orbit. Applying Eq. (37) to this situation yields
h
	pn > 	(38)
2rn
for a Bohr orbit of radius rn. The radius rn is given by Eq. (31), so that for Z =1, rn =4πε0n2h2/me2. Thus
me2
	pn >	 2h .	(39)
8πε0n
The corresponding total energy T given by Eq. (32) is n =−me4/32π2ε02n2h2. The momentum pn for state n obtained by means of the general relation p =(2mk)1/2 is given by pn =(2m|n|)1/2, since K =−T according to Eq. (32). Substituting the expression for n then gives pn =me2/4πε0nh. Now let us establish the requirement on n provided by pn evaluated above. Again using K =−T, with K = p2/2m, it is found that K =(p/m)p, so that n =(pn/m)pn. Substituting the above expressions for pn and pn then gives
me4
	n	 n /n.	(40)
When n =1, the ground-state Bohr orbit having radius r1 is denoted by a and the ground-state energy 1 is denoted by 0. For this case,  . This surprising result indicates that the uncertainty introduced into the energy by an attempted measurement of the position of the electron on its ground-state orbit exceeds the binding energy itself, so the stable configuration will be seriously disrupted by the measurement, if not totally destroyed. Thus, if one subscribes to the debatable tenet that a quantity is not physically meaningful unless it can be experimentally measured, then the very meaning of an electron orbit associated with the ground-state energy of the Bohr model is brought into serious question. In any event, an electron cannot be observed directly in orbit about a proton, so it is impossible to say exactly what the separation distance is between electron and proton at any given instant. However,theenergyabsorptionandemissionduetotransitions of the hydrogen atom between various states of excitation can be measured. This is indeed an experimental point of contact with the theory. Therefore, let us examine the predictions of the Bohr theory for the optical spectrum of hydrogen.
H. Optical Spectrum of Hydrogen
If the electron in the hydrogen atom with energy corresponding to the integer n suddenly undergoes a transition to an energy corresponding to a different integer n, with the energy difference being positive so as to create a photon of energy hν, then energy conservation gives the relation
hν = n  , (41)
where 0 is given by Eq. (34), with Z =1. Since for the photon
	hc	c
	h 	(42)
the relation given by Eq. (41) can be used to write
 
This is usually written in the form
	 ,	(44)
where
	0	me4
	R	 	(45)
2πhc	 c is known as the Rydberg constant. Thus, transitions from the various excited states (n >1) to the ground state (  1) leads to a series of spectral lines with frequencies ν =c/λ given by
This series of lines is known as the Lyman series, which is in the ultraviolet region of the spectrum. Yet a second series of spectral frequencies can be generated by transitions from excited states with n > 2 to the state n  2. It can be noted that these frequencies are given by
 
The spectral lines in this series, known as the Balmer series, have wavelengths in the near ultraviolet and visible region of the spectrum. Similar series of lines determined from n , and 5 can be written using the above prescription; these three series, labeled Paschen, Brackett, and Pfund, respectively, have spectral lines with wavelengths in the infrared region of the spectrum.
These various series of spectral lines were known from experimental observation long before the invention of the Bohrmodeloftheatomandindeedconstitutedsomeofthe major evidence that classical mechanics was inadequate for the treatment of atomic systems. The frequency relationships deduced from the Bohr theory agree quite well with the experimental spectra. Even better agreement is obtained when the finite mass of the nucleus is included in the theory; the correction comes about because electron and proton revolve about the center of mass, giving a slightly smaller orbit radius than the one obtained above (assuming the radius is the same as the separation distance between electron and proton). This is the so-called reduced mass effect, which is purely classical in nature.
I. The Laser
The absorption and emission of light due to electron transitions between quantized energy levels provide the basis foroneofthemostpowerfulresearchtoolsdevelopedover the past 50 years—namely, the laser. The key property of a laser beam is its phase coherence. The phase coherence of the beam is to be contrasted with the random phase relationships between the light emitted from various regions of an ordinary light source, such as an incandescent filament. The phase-coherent beam in a laser is produced by reflecting the emitted light back and forth between parallel mirror surfaces bounding the emitting medium, so that any light already emitted triggers additional emission and influences the phase of such additional light emission from the excited atoms of the medium. The phase of the newly emitted light turns out to be the same as that of the already emitted light. It is not intuitive from a quantum mechanical viewpoint that this should occur, but it is as one might expect on the basis of classical physics, since the electric field provides the accelerating force for the atomic electrons. That phase coherence does occur is, in fact, basic to the nature of the process referred to as stimulated emission. Stimulated emission is to be distinguished from spontaneous emission, which prevails in ordinary light sources which lack phase coherence.
The emission of light in a laser can initiate due to prior electronic transitions in atoms in a gas (e.g., a helium— neon mixture) or in a solid (e.g., ruby) that have been preexcited by some process, such as the flash of an ordinary discharge lamp. As the phase-coherent beam builds in intensity within the laser, a portion of it is allowed to emerge continuously from the active lasing medium by a partial transmission through one of the mirrored surfaces. The intense phase-coherent beams produced by lasers allow many enhanced experiments involving light interference to be carried out. The laser has enabled the speed of light to be measured to much greater precision than ever before, such that the wavelength of a laser beam can be used as an accurate standard for the measurement of length. The angular divergence of a laser beam can be held to quite small values, so that reflectance of a measurable signal from very great distances (e.g., from earth to moon and return) becomes possible. By measuring the time for round-trip light travel, large distances can be measured more accurately than was posible previously. The Michaelson–Morley experiment for determining the speed of light in different directions relative to the earth’s instantaneous velocity vector in its orbit about the sun also can be performed with greater precision with the aid of the laser.
IV. WAVE MOTION
A. Development of the Wave Equation for Transverse Vibrations
The essential equations for classical wave motion constitutethefoundationfordevelopingintuitiveinsightintothe fundamentals of quantum mechanical wave equations for particles. It is well known that wave motion can describe as varied phenomena as the transverse displacement of a wire in tension, the propagation of sound in gases, the motion of electromagnetic radiation in free space, and the longitudinal displacements associated with elastic waves in a solid. All of these classical phenomena can be treated theoretically by means of the same differential equation technique, which moreover proves to be adequate for describing the wave properties of particles.
Consider, for example, the basic classical problem of the time and position dependence of the transverse displacement of a vibrating wire, string, or rope, as indicated in Fig. 3. The transverse displacement y(x, t) of a thin wire under tension T, with mass per unit length along the x-direction given by ρ, is determined as a function of time t by a differential equation that can be obtained from a straightforward application of Newton’s second law of motion, F =ma, where F is the force and a is the acceleration. A net force Fy acting in the y-direction on a length x produces an acceleration ay that is inversely proportional to the mass ρx,
	Fy = (ρx) .	(48)
 
FIGURE 3 Transverse wave.
The net force Fy is given by the difference between the y-directed components of the uniform axial tension force T at the two ends of the element x. Considering θ to measure the angle in radians between the wire and the horizontal line representing the wire when it has no transverse displacement, θ can be visualized as varying with position x along the wire and with time t as the wire vibrates. The tensile force T is considered to have a line of action that is always parallel to the wire. This leads to a projected component in the y-direction given by (T sinθ). At the ends of the segment x the tensile force T acts in opposite directions, as is required of a tensile force. If the segment is not to be accelerated in the x-direction, then the x-components of these end forces must essentially cancel each other. The component of T projected in the x-direction is given at any point by (T cosθ), so this cancellation condition is met adequately if θ is small enough. In the small θ limit, the net force in the y-direction on the segment x, namely,
	Fy x	(49)
reduces to the approximation
	Fy  x	(50)
which, in turn, can be approximated by
	Fy .	(51)
Because tanθ is the slope ∂y/∂x, this last equation is equivalent to
	Fy = T 	(52)
Equating this expression for Fy to the partialderivative equivalent of Eq. (48) gives
 
Dividingthroughbyx andtakingthelimitx →0gives
∂2y ∂2y
	ρ  = T	(54)
The unit of tension T in SI units is Nt and the units of ρ are kg/m, so T/ρ has the dimensions of m2/s2, the square of a speed. Denoting the square root of this quantity by
	vp 	(55)
where vp has the units of velocity, the equation for a vibrating wire takes the form
 	(56) ∂x
This is the well-known classical wave equation. It is a linear, second-order differential equation that governs, in the present example, the transverse displacement y(x,t) as a function of position along the wire as time proceeds. Both standing-wave modes and running-wave modes are possible, depending upon the boundary conditions imposed on the wire.
The classical wave equation given by Eq. (56) also has a three-dimensional form to describe motion in arbitrary directions in space. There are various ways to generalize Eq. (56), but it is simplest first of all to think of wave motion along the z-axis, in contrast to the x-axis. The simple change in dependent variable from x to z naturally yields the relevant equation. It is clear that to include the three independent directions in space will require three terms involving spatial derivatives in place of the single term in Eq. (56). If these three Cartesian coordinates are denoted by x, y, and z, then it is necessary to use some alternate notation for the wave displacement. Denoting the wave displacement by ψ(x, y, z,t), the classical three-dimensional wave equation then can be written as
	 ,	(57)
where ∇2 symbolizes the differential operator (∂2/∂x2)+ (∂2/∂y2)+(∂2/∂z2).
B. Solutions to the Classical Wave Equation
Let us attempt a trial solution for Eq. (56) of the form
	y = C exp[i(kx − ωt)],	(58)
where, at the moment, C, k, and ω are unspecified constants, perhaps even complex numbers. Substituting Eq. (58) into Eq. (56) gives a condition on the constants ω and k in terms of vp:
k .	(59) v2p
The complex form of the trial solution is troublesome for those who are more concerned with physical phenomenathanwithmathematics,sincethedisplacementisareal quantity. In point of fact, the mathematical solution, in itself, does not have any physical interpretation associated withit.Tobeabletoclothethemathematicalsolutionwith physical content, it is often necessary to restrict somewhat the range of solutions that can be accepted.
The physically meaningful solutions for the present problem of a vibrating wire are thus given by
	[y] physically	 (kx − ωt)]}. (60)
meaningful subject
where   means “take the real part of.” It is expedient at this point to restrict the constants k and ω to real values. However, it proves very useful, as will be shown, to maintain the constant C in its most general complex form,
	C ,	(61)
where D and  are real numbers. The trial solution therefore can be written in the form
	y ,	(62)
thus giving real solutions of the form
	y .	(63)
The right-hand side of Eq. (63) has the sort of space dependence and time dependence seen for vibrating wires in the laboratory. Larger values of ω yield shorter repetition periods in time, and larger values of k yield shorter repetition periods in space. Considering that a cosine function repeats itself when its phase is increased by 2π, it can be concludedthatkλ=2π andωr =2π givethebasicspatial unit λ and temporal unit τ for repetition. These parameters are called wavelength and period, respectively. Note that
	k 	(64)
and
	 .	(65)
The temporal frequency ν is the reciprocal of the period τ, or
	 ,	(66)
so that		
	ω = 2πν.	(67)
Here, the explicit assumption was made that the constants ω and k are real. For wave motion, this is consistent with the physical interpretations relating these parameters to the temporal frequency and the reciprocal of the spatial periodicity.
C. Phase Velocity of Waves
It is a universal property of wave motion that
 ,	(68) k 2π/λ τ
and this ratio gives the speed vphase of the sinusoidal wave, where τ is the period for one temporal oscillation. This is readily understood by visualizing a moving sinusoidal spatial wave pass by a given point in space, the length λ passing in time τ. The speed of an individual sinusoidal wave is called phase velocity. and is denoted by
vphase  .	(69) k
Therefore, Eq. (55) states that the quantity vp =(T/ρ)1/2 is the speed with which the sinusoidal wave moves along the wire. The phase velocity may depend upon frequency or wavelength in some instances. Note that in the present example, however, the phase velocity depends directly upon the square root of the tension in the wire and inversely upon the square root of the mass per unit length of the wire, independent of the frequency or the wavelength of the wave.
D. Development of the Wave Equation for Electromagnetic Waves
It can be readily shown that electromagnetic waves in free space also satisfy a wave equation analogous to Eq. (57) for transverse waves along a wire and thus have solutions that are mathematically the same. To develop this wave equation, consider Maxwell’s equations of electromagnetic theory
∇ · D = ρ	(70)
∇ · B = 0	(71)
∂B
	∇ × E = − 	(72)
∂t
∂
	,	(73)
∂t
where D is the electric displacement vector, B is the magnetic induction vector, E is the electric field vector, H is the magnetic field vector,  is the electric current density vector, and ρ is the electric charge density. In free space, the linear relations
D = ε0E	(74)
B = µ0H	(75)
are applicable, where ε0 is the electric permittivity of free space and µ0 is the magnetic permeability of free space. In the absence of free charge and with no electric current density, the following relations are obtained:
∇ · E = 0	(76)
∇ · H = 0
∂H	(77)
	∇ × E = −µ 	(78)
∂E
∇ × H = ε0  .	(79)
∂t
Taking the vector curl of Eqs. (78) and (79) yields
	∇ × ∇ × E µ (∇ × H)	(80)
	∇ × ∇ × H ε0	(∇ × E).	(81)
∂t Applying the vector identity
	∇ × ∇ × V = ∇(∇ · V) − ∇2V,	(82)
which is valid for any vector V, to the left-hand sides and simultaneously utilizing the relations ∇ · E=0 and ∇ ·H=0 given by Eqs. (76) and (77) yields the following relations:
	 E µ0	(	H)	(83)
∂t
	 H ε0	(	E).	(84)
∂t
Substituting the expressions for ∇ ×E and ∇ ×H then reduces Eqs. (83) and (84)
∂2E
∇
2
E = µ 	(85) ∂2H
∇
2
	H = µ .	(86)
These are vector equations; each represents three scalar equations, one for each of the three vector components. By considering any one component of these fields (e.g., Ex, Ey, Ez, Hx, Hy,or Hz)andcallingtheparticularcomponent ψ, Eqs. (85) and (86) lead to the three-dimensional wave equation
	 	(87)
where, in the present problem, the phase velocity c is determined from the physical constants µ0 and ε0 in accordance with c =(µ0ε0)−1/2. This is the propagation velocity for electromagnetic waves in free space. Substituting the values ε0 =8.854×10−12 F/m and µ0 = 4π ×10−7 henry/m (H/m) gives the speed of light in free space as c =2.998×108 m/s.
Equation (87) has particularly simple solutions depending on position r and time t. For example, plane waves represented by A cos(k · r−ωt +α) satisfy the equation, where A,k,ω, and α are constants. The magnitude of the vector k determines the wavelength λ, so that
	 .	(88)
The wave is traveling at phase velocity c =ω/|k| in the direction of k. The amplitude A of the wave is the maximum value of the transverse field component represented by ψ.
E. Dispersion Relations for Waves
The ω versus k relation for any wave is called the dispersion relation for that wave. The dispersion relation always givesthemagnitudeofthephasevelocityvphase ofthewave in accordance with vphase =ω/k. With this generalization, Eq. (57) can be viewed as a more general equation for one-dimensionalclassicalwavemotion.Thesameformof the equation holds for electromagnetic wave propagation in free space, according to Eq. (87). The phase velocity is then the speed of light, and the appropriate dispersion relation is
	ω = ck.	(89)
Light propagates in a dielectric medium according to essentially the same wave equation as that for free space. In that case, however, the phase velocity depends upon the refractive index n of the medium, so that c
vphase =  ,	(90) n
wheren usuallyvarieswiththewavelength.Theactionofa prismindispersingthecolorsfromincidentwhitelight,for example,isprimarilyduetothefactthatthephasevelocity is color dependent. Red light travels approximately 0.5% faster than blue light in fused quartz. Both colors travel in fusedquartzatapproximatelytwo-thirdsthespeedoflight in free space, but since the speed of blue light is decreased slightly more than the speed of red light as the white light enters the quartz from the vacuum, the blue light is bent more toward the normal direction than the red light. The colors thus become dispersed as the white light enters the prism at an angle with respect to the normal to the surface of the prism. The dispersion relation for this situation
is
ck
	ω = vphasek =  ,	(91)
n(k)
where n explicitly depends on k, denoting a wavelengthdependence since λ=2π/k. This example also will be useful in understanding group velocity in the development that follows.
F. Boundary Conditions
The next consideration is the type of boundary conditions that are imposed by the physical situation. If the endpoints ofawireoflength L arefixedatpositions x =0and x = L, then the fact that the displacements must be zero at these points leads to the requirement that the wave must have stationary nodes at these points. A similar type of boundaryconditionholdsforelectromagneticwavestrappedina highly conducting metal box, since the metal walls cannot support an electric field. Equation (63) cannot satisfy such boundary conditions as time progresses, but two such solutions having the same magnitude k but differing in sign of k, with properly chosen phases, can be superimposed to yield a solution that can satisfy the condition. For example, the superposition solution y = D[sin(kx −ωt) + sin(kx +ωt)] = 2D sin(kx)cos(ωt) satisfies the boundary condition at x =0; the boundary condition at x = L is satisfied if the wavelength is chosen to have any value λ= L/n, where n can be any positive integer. The amplitude of this wave is 2D. The nodes (y =0) and extremum values (y =±2D) of the wave do not change position x in time t, so this solution is called a standing wave.
On the other hand, for an infinitely long wire (or an unbounded medium for electromagnetic wave propagation), there may be no constraints on the displacement at any particular position, so the solution described by Eq. (63) may be quite acceptable. The particular values of position x for which the wave has nodes and extremum values change with time t. This wave is not stationary and thus is called a running wave. For positive values of ω and k, Eq. (63) shows that a given value of the phase is maintained as time increases if one focuses on an observation point x that moves along the x-axis linearly with t. Thus, the phase velocity ω/k is said to be constant and the wave moves in the positive x-direction. If k is negative but ω is again chosen to be positive, as is conventional, then the phase velocity is negative and the wave moves in the negative x-direction. The standing wave constructed to satisfy the fixed-boundary conditions situation can be viewed simply as the superposition of two equal-amplitude running waves having the same frequency and wavelength but moving in opposite directions. Considerations of more complicated superpositions follow.
G. Superposition Solutions
An arbitrary superposition of solutions to the linear, timedependent wave equation considered above also satisfies the same equation. There is no way for the terms to mix as products if the equation is linear, so the terms for each solution can individually add to zero. The superposition couldbewrittenasasumoftermshavingdifferentweighting coefficients Dj, so that
y k j x  , (92)
j
where each ratio ωj/k j has the appropriate value of vphase. The superposition could yield a shape for y(x) at a given time t that differs markedly from any of the sinusoidal components. If each component moves in the same direction at the same speed, corresponding to a value of vp, whichisafixedconstant,thenmotionwouldbeanticipated but not distortion of shape. In wave packets considered below,itmayhappenthatdifferentcomponentwaveshave different phase velocities. That is, the phase velocity may be a function of the frequency (or wavelength). Variations in the phase velocity can lead to a change in shape, since phase relationships among the individual components continually change if they are traveling at different speeds.
H. Group Velocity of Waves
It is known from the theory of Fourier series and Fourier integrals that the superposition of sinusoidal waves can yield almost any physically reasonable periodic or nonperiodic function. Thus, by superposing solutions of different wavelengths, nearly any function shape can be generated at any given time. The superposition of waves bearing a harmonic relationship to one another yields a spatially periodic function, whereas the superposition of waves having amplitudes over a continuous narrow band of frequencies yields a spatially localized function. The waves in the superposition may or may not have the same phase velocity. Consider, for example, the case of electromagnetic wave motion in dielectrics, where the physical properties of the medium determining the wave speed are frequency- or wavelength-dependent. Whether or not the shapechangesovertime,itwillgenerallymove.Theproblemtoaddressnowistheevaluationofthespeedofmotion of the shape.
To simplify the problem, let us confine our attention to a narrow band of wavelengths, corresponding to a narrow range of k values centered about some central value k0. For example, a pulse of light having a certain shape could have a range of wavelengths closely centered about the green 5461 A line of mercury. If the amplitude is a contin-˚ uous function of the wavelength over the band, in contrast to the superposition of a finite number of discrete wavelength components, then an amplitude function χ(k) can be defined that peaks at k0 and has very low values outside the narrow band of interest. It is known from the theory of Fourier integrals that the shape of χ(k) as a function of k depends directly upon the position-dependent shape of the pulse. If ψ(x,0) denotes the pulse in space at time t =0, then a Fourier inversion directly yields χ(k). It can be shown that the widths of the two functions are related inversely: the broader χ(k) is, the more narrow ψ(x,0) will be, and vice versa. This is a manifestation of a relationship between the spread (or uncertainty) in wavelength versus the spread (or uncertainty) in position of the wave packet. This point is crucial for the Heisenberg uncertainty principle but is not directly relevant to the present development for pulse velocity.
Considering any reasonable shape for χ(k), the superposition can be written
	 .	(93)
This form has the character of a complex Fourier integral. Alternately, the same problem could be treated in terms of integrals involving the real functions, sine and cosine, with the real argument (kx −ωt) replacing the imaginary argument [i(kx −ωt)] of the exponential form. To obtain general properties of the superposition, no specific choice is made regarding the functional form of χ(k), except that it be chosen to be moderate in functional behavior and smooth. In general, it is complex, with the roles of the real and imaginary parts being exactly the same as the roles of the real and imaginary parts of C  utilized in Section B—namely, to supply both amplitude and phase information. In this situation, both are supplied as a function of k. Let us assume that the dispersion relation ω versus k is known for the wave in question in the neighborhood of k0, where the components are presumed to have larger amplitudes. These conditions are then sufficient to use a Taylor series expansion of χ(k) on k about the value k0:
ω(k) = ω(k0)  k0)
  k0)2 + ···. (94)
Substitutingthefirsttwotermsofthisexpansionyieldsthe following result for the wave packet under consideration:
 
 dk. (95)
In terms of the defined quantities
	vgroup = 	(96)
k=k0
	β0 = ω(k0) − k0vgroup	(97)
Eq. (95) becomes
 vgroupt) − β0t]}dk.
(98)
To find out where ψ is peaked in space at any given t, one canconsidertherealandimaginarypartsofthisexpression individually. Writing
	χ(k) = χr(k) + iχi(k),	(99)
then the real part of Eq. (98) is
 vgroupt) − β0t]dk
 vgroupt) − β0t]dk.
(100)
The imaginary part can be obtained similarly. Focusing first on the cosine integral, the coefficient of k (namely, x −vgroupt), will determine how rapidly the cosine function oscillates as k is varied during the integration over k. Rapid oscillations lead to much cancellation between positive and negative contributions to the integral, with the consequence that the integral will not be large. On the other hand, very small values of the coefficient mean far fewer oscillations over the band of wavelengths where χr(k)issignificant,andthesmalleramountofcancellation means that the integral will be larger. The same arguments can be employed for the sine function integral. Thus, for a given t, the maximum value of ψ occurs at the position where the coefficient is zero—namely, at x =vgroupt. Since this position of the peak moves with the velocity vgroup, the reason for calling this quantity the group velocity is apparent. The identical state of affairs holds for the imaginary part of ψ. Thus, a very general expression for the one-dimensional group velocity is given by Eq. (96).
The additional term β0t in Eq. (100) can be written as a phase factor (t)—namely, (t)=β0t—which increases linearly with the time. Because it does not depend upon the variable k of integration or the position x, it is not a very important quantity for determining how relatively large ψ will be as a function of x. Its primary effect is to shift the phase of all superimposed waves by the same constant factor  at any given time t, which leads to a modulation of the spatial function over time.
More effects come into play if the third term in the Taylorseriesexpansionofω(k)giveninEq.(94)isbrought into the wave-packet integral. The packet can then spread and possibly change shape as time evolves.
Let us now apply our results for the group velocity to thesituationofelectromagneticwavepropagationthrough a dielectric. Presuming wavelengths in a narrow band to be superimposed to form the packet, the group velocity can be obtained in terms of the refractive index n(k) of the dielectric. Consider a narrow band of wavelengths of green light centered about the 5461A line of mercury as˚ those waves travel in fused quartz. The phase velocity being c/n(k), the dispersion relation is ω(k)=ck/n(k), so the group velocity is
vgroup
k=k0
. (101)
k=k0
Since k =2π/λ, it follows that
dn
.	(102) dk dk/dλ
Thus, an alternate form of the group velocity for this
situation is
vgroup. (103)
	n(k)	dλ =k0
Consider n(k) in this expression in terms of its λdependence.Thephasevelocityvphase isthatforthecentral component wave in the packet—namely, at wavelength 5461 A. Note from this result that for situations in which˚ the refractive index is independent of λ, the group velocity is equal to the phase velocity. Estimates for fused quartz, however, give n =1.46 and dn/dλ=−4×10−6 A˚ −1 at λ=5461A. Using these numbers in Eq. (103) gives˚ vgroup/vphase =1−0.015 =0.985. Thus, the group velocity for the wave packet of green light in fused quartz is ∼1.5% less than the phase velocity. This may seem to be an unimpressive figure until it is realized that the similarly small difference in phase velocities between 4500 A and˚ 6500 A yields the dispersion in a fused-quartz prism that˚ enables the splitting of incident white light into its spectrum of colors.
Although it is interesting to consider that the group and phase velocities can differ, as shown here, there is actually nothing so mysterious about it. The individual sinusoidal waves extend throughout space and, in this sense, are nonlocalized.Anygivenpointonanyoneofthewaves,suchas oneoftheextremumpointsoroneofthenodes,moveswith the phase velocity. The superposition of a group of such waves to form a localized packet occurs by a subtle phase interference that is, on the whole, constructive only over a localized region in space and destructive throughout the remainder of space. The phase interference changes with time if the component waves move at different speeds, so the spatial peak in the localized shape can move over time, even relative to a given point on the moving component wave that has a k-value exactly equal to that of the center of the band of superimposed waves.
If a packet is moving in some direction in space that is not parallel to the x-axis of our coordinate system, then the group velocity will have components along the three axes of the coordinate system. The dispersion relation will take the form ω=ω(k), where k is a vector pointing in a given direction. Since ω is a scalar quantity, ω(k) maps outatypeofthree-dimensionalsurfaceforthedependence of frequency on direction and magnitude of the k-vector. Thek-vectorrepresentsthedirectionofpropagationofone component wave of the packet, and the magnitude of the k-vector still has the interpretation of being 2π/λ, where λ is the wavelength of the component wave in its propagation direction. The group velocity components in the x, y, and z directions in space can be obtained by generalizing Eq. (96), which was derived on the assumption that there was only x-motion. A proper way to carry out the derivation is to use the Taylor series expansion of ω(k) in three dimensions. Three first-derivative terms can be obtained in place of one, and the multipliers of kx,ky, and kz are, respectively, [x  ], and [ ],
where
vgroup(x)(104)
k=k0
	vgroup(y)	=(105)
k=k0
	vgroup(z).	(106)
k=k0
The conclusion to be reached is that the group velocity is a vector with components given by Eqs. (104)–(106). These results can be abbreviated by writing
	vgroup = ∇kω(k)|k=k0	(107)
as the general expression for the group velocity for wave motion in three-dimensional space.
V. WAVE–PARTICLE DUALITY
A. Ideas of de Broglie
The discovery that particles diffract like waves was one of the most important in physics, since the entire discipline of quantum mechanics is based on a wave description of matter. Preceding that discovery, de Broglie carried out an analysis of the hypothetical wave properties of matter by employing special relativity theory, with an insightful hunch that matter is not all that different in its fundamentalwavebehaviorfromelectromagneticradiation.His idea was that since radiation had been shown to have both wavelike and particlelike properties, perhaps nonzero rest mass “particles” also could manifest both wavelike and particlelike properties. However, different experimental conditions might be required for matter to manifest one property or the other. De Broglie called his idea wave– particle duality.
In 1926 Walter Maurice Elsasser suggested that the de Broglie hypothesis could be tested by aiming an electron beam at the surface of a crystalline solid to see if diffraction spots were obtained in the same way as observed in X-ray diffraction. Experiments were carried out shortly thereafter by Davisson and Germer and also by G. P. Thomson, so that by 1927, the de Broglie hypothesis had been experimentally verified. Thus, the electron discovered by J. J. Thomson in 1987 enjoyed its status as a classical particle for a period of less than 30 years before its schizophrenic nature surfaced. Amazingly, it was later confirmed not only that electrons had this dual nature but also that other particles, including neutrons and atoms, could be diffracted. Particles somehow have the inherent property of being able to experience mutual interference even while maintaining such an extremely high degree of localization in space that they would not appear to have any physical overlap. What boggles the mindevenmore,singleparticlesthemselvesbehavestatistically in accordance with the same diffraction probability distribution.
Because electromagnetic radiation can manifest discreteness properties, with the photon energy  related to frequency according to
	 = hν = hω	(108)
de Broglie reasoned that, in analogy, any wave properties of particles would also have some associated frequency. Moreover, in accordance with the concept of wave–particle duality and the similarity of particle and electromagnetic radiation in nature, he assumed that the energy–frequency relation for particles would be the same as the energy–frequency relation for photons given by Eq. (108).
The term particle generally is utilized to refer to those fundamentalentitiesforwhichtherestmassm0 isnonzero. Exactly what the frequency of a particle refers to is not known, but it can be imagined that there is some internal mode of oscillation.
B. Development of the de Broglie Relation
If a particle can ever be localized to any extent in space, as there is certainly every right to expect, and simultaneously is to have its experimentaly observed wavelike character described in some fashion by waves, then it is quite logical to consider a wave packet of the sort treated in Section IV.H. The waves forming the packet necessarily would be matter waves, but the diffraction results lead to the belief that these waves have the same linear superposition properties of all other familiar types of waves. The waves must be associated with the presence of the particle in some way, so it is reasonable to expect that the group velocity vgroup of the wave packet will be equal to the particle velocity vparticle, or
p
vgroup = vparticle =  ,	(109) m
where p is the momentum of the particle of mass m. Let us for the moment confine our attention to a single direction in space. The discussion will be generalized to three dimensions later, whenever there are important implications.
The group velocity expression vgroup =dw/dk given by Eq. (96), which was derived in Section IV.H, together with the derivative of the energy–frequency relation given by Eq. (108), postulated by de Broglie, can be utilized to obtain
d = h dω = hvgroup dk.
Next, the energy–momentum relation	(110)
	 	(111)
given by Eq. (22) is differentiated and the mass–energy relation given by Eq. (20) in Section II on the special theory of relativity is used to obtain a second independent expression for d,
c2p dp	c2p dp d =	=
p
=	dp = vparticle dp.	(112) m
Equating the two independent expressions given for d by Eqs. (110) and (112) gives
	vparticle dp = vgrouph dk.	(113)
Identifying the group velocity with the particle velocity, according to Eq. (109), and dividing Eq. (113) by this quantity gives
	dp = h dk.	(114)
This remarkable result relates the change in the reciprocal of the wavelength of a particle matter–wave component to a change in the momentum of the particle. Since by definition k = 2π/λ, the relation given by Eq. (114) also can be written in the physically more meaningful form,
	h	2π	h
	dp  d	(115)
Integrating Eqs. (114) and (115) from any arbitrary reference point, denoted by subscript 0, gives
p  . (116)
Thus
h
	p ,	(117)
which derives the de Broglie relation, a relationship between the momentum of a particle and the wavelength of the matter wave associated with a particle having this precisely defined momentum. Built into this development is the fundamental hypothesis of de Broglie that matter has associated with it a frequency that is related to the total energy in the same way that the frequency of electromagnetic radiation is related to the individual photon energy.
If the photon is considered to be a quantum particle in every respect, except for being a limiting case from the standpoint of having zero rest mass, then
h
pphoton = hkphoton =  	(118) λphoton
As an alternative, applying the energy–momentum relation given by Eq. (22) to the case of photons, which have zero rest mass and, hence, zero rest-mass energy in accordance with 0 =m0c2, gives
	photon = ±pphotonc.	(119)
The sign of the root is chosen to give a positive value for the photon energy, since there is no physical interpretation for negative photon energy at the present moment.
Next, let us use the energy–frequency relation given by Eq. (108) to obtain an independent relation for the photon energy:
photon = hωphoton = h(2πνphoton)
hc
	= hνphoton =  .	(120)
λphoton
Equating the two independent results of Eqs. (119) and (120) for the photon energy and dividing through by the light velocity c gives
h
	pphoton =  .	(121)
λphoton
This relation is consistent with Eq. (118) and the experimentally proven hypothesis that light has a momentum associated with it. This fact is also a part of classical electromagnetic theory, but the form is somewhat different from the quantum result given here.
As is evident from the development of Eq. (117), the relation is valid for particles of any rest mass, including the limiting case of zero rest mass, and it is valid at any velocity, including the limits of low velocity and relativistic velocity. This relation has been confirmed experimentally by accelerating electrons to different velocities, including relativistic velocities.
Itseemsabitstrangethatsuchafundamentalrelationof quantum mechanics is deduced from the theory of special relativity, considering the discussion in Section II.B of the difference in philosophical bases for the two theories. To be specific, the fundamental equations of a deterministic theory have been used here to deduce a wavelength relationship for particles, the preciseness of this wavelength determining to a large extent the inherent uncertainty in the specification of the location of the particle. One should not be misled, however, into believing that relativity theory has predicted the wave nature of particle. Instead, the wave nature of particles is the initial hypothesis that, in itself, is supported by experimental observation that particles diffract from crystal lattices in a wavelike manner.
C. Phase Velocity for Free Particles
The relations ω=/h and k = p/h can be used to evaluate the phase velocity vphase of matter waves:
	mc2 vphase =
p
=(122) vparticle
The phase velocity of matter waves thus depends upon the particlevelocity.Astheparticlespeedincreases,thephase velocity decreases.
Although the phase velocity takes its most natural form when expressed in term of the particle velocity, it also can be expressed in terms of the particle momentum: ω 
vphase = = = p k	p
	= c ,	(123)
where pC =m0c. This also can be expressed as
1/2 vphase = c
1/2
	= c,	(124)
where kC = pC/h =m0c/h and λC =2π/kC =h/m0c.
TheparameterλC iscalledtheComptonwavelengthwhenever m0 is the electron rest mass. It is not the wavelength of an electron at rest, of course, since the de Broglie relation yields infinity as the wavelength of a particle with zero momentum.
For the special case of photons and other particles that have zero rest mass, the phase velocity is given by
vphase	0  m0=0
pc
	c.	(125)
= p =
Matter waves have phase velocities ranging upward from c, with the phase velocity approaching infinity as the particle speed approaches zero. The phase velocity represents the speed of motion of a single, isolated and completely extended component wave having no position modulation of its shape and, by itself, can carry no information. Thus, there is no conflict with the tenet of special relativity that a signal cannot travel with a velocity exceeding the speed of light.
Tosummarizeformatterwaves,thegroupvelocitymust be equal to the particle velocity and the phase velocity varies inversely with the particle velocity. The critical quantity for evaluating the wavelength is the momentum, whereas the critical quantity for evaluating the phase velocity is the particle velocity. Particles having different rest-mass values have the same wavelength whenever the velocitiesdiffersuchastogivethesamevaluesforthemomentum. Particles having different rest-mass values have the same phase velocity, however, whenever they have the same value for the particle velocity.
D. Dispersion Relation for Free Particles
It has been shown in Section IV that the dispersion relation for light is ω=ck. This immediately gives the phase velocity ω/k =c and the group velocity dω/dk =c.
The dispersion relation for free particles is deduced by
utilizing the energy–momentum relation from special relativity and substituting =hω and p =hk, so that
	h .	(126)
This free-particle dispersion relation also can be written in the form
	 ,	(127)
where ω0 =m0c2/h, the frequency corresponding to the rest mass m0. In terms of parameters λC =h/m0c and kC = 2π/λC, Eq. (127) becomes
	ω = ckC .	(128)
Binomial expansion illustrates a quadratic dependence of ω on k with a cutoff in frequency below the rest-mass frequency ω0:
	 .	(129)
For low values of the particle momentum, k is small and the frequency does not depart very much from the restmass frequency. This is merely a reflection of the fact that =mc2 =γm0c2 =hω predicts that
	 γ,	(130)
where γ is the parameter defined by Eq. (19) in Section II on special relativity. This might be described by considering the particle as initially created in a zero potential energyregionwithaproperfrequency,whichitthenmaintains always during its lifetime. Any perceived difference in frequency due to motion is then merely due to the relativistic shift in energy with Galilean reference frame. This is analogous to the increase in mass with the particle speed; that is, m =γm0, so =mc2 =γm0c2. Thus, =hω=γhω0, thereby giving ω=γω0 in Eq. (130).
This does maintain the de Broglie premise that a particle has a frequency associated with it even when it is stationary, that frequency being dependent upon the rest mass m0 in accordance with the relation 0 =m0c2 =hω0.
E. Energy–Momentum Relations for Particles with Potential Energy
It may be appreciated that developing the dispersion relation ω(k) versus k can be sufficient preparation for evaluating the phase velocity vphase =ω(k)/k, according to Eq. (69). Because most applications of quantum mechanics involve particles with some type of potential energy, it is necessary to consider this situation.
A force F changes the momentum p of a free particle in accordance with F=dp/dt, or, equivalently, the change dp in particle momentum is given by Fdt. Since the work done by a force in moving a particle through a vector distance dr is dW =F·dr, the power input =dW/dt from the source is F·dr/dt =F·v. In one dimension, = Fv.
In our case, the power to change the motion energy of the particle comes from the internal potential energy. For a conservative system, the potential energy change with position leads to an internal force on the particle
	F = −∇U(r)	(131)
which, for one dimension, is simply
(r)
F.	(132) dr
Thus
dp  = −dU(r) dt = dr
F(133)
or, equivalently
dU .	(134) dt
But vparticle =dr/dt, so dr =vparticle dt, and the result is
	= −dp	= −
dU(r)vparticle dt vparticle dp dt
−p
	dp	(135)
This relation cannot be integrated directly because m dependsuponparticlevelocityand,hence,upon p.However, substituting m , with  given by the usual energy– momentum relation of special relativity in Eq. (22), leads to a perfect differential:
dU 
	 .	(136)
Integrating from a classical turining point, defined as a position where p =0 so the potential energy at the point is the total energy  T in classical Newtonian physics, we obtain
U . (137)
The classical total energy is conserved as long as no rest mass is created or annihilated. A new constant (T) thus can be defined as
	 c2	(138)
and Eq. (137) can be written as
	 .	(139)
This is the energy–momentum relation for a particle having a potential energy. Note from this relation that when the potential energy is zero, T() becomes the total relativistic energy  of a free particle. The constant T(), in lieu of , is the conserved quantity when a potential energy is included. Let us also define a quantity (K)
	 )	(140)
or, alternatively, T 	K	U(r). By employing
Eq. (138), Eq. (140) can be written in the form
   c2	(141)
and, by employing Eq. (139), this expression can then be written in the form
	K	 .	(142)
Equation (141), in the form
	T 	K	+ U(r) + m0c2	(143)
seems intuitive from a scalar-energy viewpoint. This form has its primary usefulness in the low-velocity limit. In the relativistic limit, the best form for T() is that obtained from Eq. (139):
	 )	(144)
since this form is intuitive from a free-particle viewpoint. Squaring Eq. (139) and solving for p2 gives
	p	 c2	T	−	− . (145)
Substituting Eq. (141) then gives
p	 2	K	−	, (146) c
 
which relates the momentum to the quantity K	. Rearranging Eq. (146) to obtain (K) explicitly in terms of p gives
	 K	m
Employing the binomial expansion then gives the series approximation
	 .	(148)
Inthelow-velocitylimitdefinedby	 1,whichrequires
 1[seeEq.(19)], p v,andthequantity(K ) thus reduces in lowest order to the Newtonian expression for the kinetic energy
	 m0v2.	(149)
F. Dispersion Relations for Particles with Potential Energy
To develop a wave dispersion relation applicable to particles having a potential energy, the wavelength is again associated with the particle momentum by means of the de Broglie relation λ=h/p. Equivalently, p =h/λ= (h/2π)(2π/λ)=hk, in accordance with Eq. (117).
According to the de Broglie hypothesis, a frequency ω must be associated with the particle energy. Although the nature of the frequency of a particle is not yet understood, a guideline can be the familiar results from the particular limiting case of a zero rest-mass quantum particle— namely, the photon. One must remain alert, however, to avoid introducing subtle errors in using the analogy.
The photon has a wavelength λ and a frequency ν. As the photon travels in free space, it has a speed c =λν. When the photon enters a dielectric material medium of refractive index n, its speed decreases to c/n but its frequency ν does not change. The photon energy =hν thus does not change. The wavelength decreases in accordance with λmedpho =λvacpho/n, where λmedpho is the wavelength in the medium and λvacpho is the wavelength in free space. The photon velocity is still given by the product of photon frequency and the appropriate photon wavelenght, whether the medium be a dielectric or free space. The momentum p h/λvacpho of the photon in free space changes to pphomed =h/λmedpho as it enters the dielectric medium. Thus, the constant of motion for the photon is the frequency ν =ω/2π, with wavelength λ and momentum p being medium-dependent. It is an interesting observation that, from the viewpoint of Eq. (142), all energy of the photon is kinetic.
One might be tempted to assume, in analogy with the photon, that the frequency of a particle located in a purely conservative potential energy region is a constant of motion. This would give rise to the picture of a particle entering a region of varying potential energy, where it could be accelerated. Its speed would change with its acceleration. Its momentum would change, so its wavelength would change also. However, the total energy of the particle would not change. Both remaining unchanged, the frequency would then maintain a direct relationship to the total energy. The analogy with the behavior of a photon as it enters a region of varying refractive index would, in this way, be exploited to the fullest. However, this might seem to do great violence to the earlier conclusion that the frequency of the wave associated with a free particle depends upon the speed of the particle. In the present case, one would be considering the particle changing speed due to the change in internal potential energy as it moves through the potential energy region, yet one would be proposing to hold its frequency ω to be a constant. Moreover, the constantfrequencywouldnotbeequaltotheproperfrequency ω0 for the particle in the relativistic sense but would have somevaluethatwouldnecessarilyberelatedtoU(r),since eventhechoiceofthezeropointformeasuringU(r)would affect the value of ω.
This strange state of affairs might be viewed as unacceptable. The seeming enigma can be resolved, however, in the following way. The total energy of a particle in a potential energy U(r) can be viewed, apart from some constant reference energy, as the energy of a quantum system consisting of the particle in question plus the source medium responsible for the potential energy. As the particle moves about in the potential-energy region, its kinetic and potential energy changes in such a way that the total energy remains invariant. Thus, an increase in the kinetic energy of the particle comes at the expense of its potential energy, so the chemical binding energy of the systemisincreased.Similarly,adecreaseinthekineticenergy of the particle means that its potential energy is algebraicallyincreased,whichcorrespondstoadecreaseinthe chemical binding energy of the system. The relationship between energy and frequency for the particle in the system can be postulated to involve the kinetic energy of the particle and the attendant local modification in the binding energy of the system. This is consistent with choosing hω  T instead of  ), so that
 
T
ω =  ,	(150) h
 
where (T) is defined by Eq. (144).
G. Phase Velocity of Particles with Potential Energy
Taking the frequency of the particle wave from Eq. (150) and using the de Broglie relation k = p/h given by Eq. (117) leads to an evaluation of the phase velocity
 
ω hω T
vphase = = = . (151) k hk p
VI. WAVE EQUATIONS FOR PARTICLES
A. Master Equations for Particles with Potential Energy
In this section, it is assumed at the outset that the reader already has studied carefully the material presented earlier, especially the fundamentals of classical wave motion in Section IV and the ideas of wave–particle duality in Section V. This section relies heavily on the concepts of dispersion relations and phase velocity in wave motion covered in those sections.
Utilizing the three-dimensional classical wave equation [Eq. (57)] and substituting Eq. (151) for the phase velocity gives the wave equation for particles
 ∂2
	   	(152)
∂t2
T
or, equivalently
1∂2
	 	(153)
 
with ≡[p/(T)]2. It should be noted from Eq. (145) for p that  will depend upon position r, but it does not depend explicitly upon the time t. Therefore, the variables can be separated in Eq. (152), so a solution can be carried out by the separation-of-variables technique. Substituting the product trial solution
	 )	(154)
into Eq. (153) and dividing through by ψ yields
 . (155)
The usual argument for the separation of variables holds. The right-hand side is a function (at most) of the variable t, the left-hand side is a function (at most) of the variable r. Since the two sides are required to be equal, then neither can vary with t or r. Setting the right-hand side equal to the constant  and employing the trial solution
	T )	(156)
yields a solution, provided that
	 .	(157)
Since T0 is unspecified, it can be conveniently chosen to be unity. The right-hand side of Eq. (155) equals , so the left-hand side must equal  also. Thus, the differential equation for (r) is
	2	2
	 = −	(158)
or, equivalently
	 (r) = 0.	(159)
There still remains the task of evaluating the constant . The approach used is to consider the limiting case of a constant potential energy U(r)=U0, so that the momentum p is a constant. There is then no position-dependence of . The quantity 2 is always a constant [cf. Eq. (157)], so that the product 2 is then a constant. As a consequence, Eq. (159) has particularly simple solutions. The trial solution

	)]	(160)
satisfies the equation, with k being a vector constant. This solution represents a wave having wavelength 2π/k, with k , which is traveling in the direction of the fixed vector k. In one dimension (e.g., a particle moving along the x-direction), the exponential function reduces simply to exp(ikx). The k-vector involves the wavelength for the particle wave and therefore is associated with the particle momentum p in accordance with the de Broglie relation p=hk. The momentum in this case of a constant potential energy is a constant of motion. Substituting this solution into Eq. (159) gives
	 0	(161)
so that
k2
2
	 =   =	p2	T .	(162)
Since p=hk, this leads to the conclusion that
 
T
 =  .	(163) h
It can be noted from comparison of this result with Eq. (150) that the separation constant   is equal to −ω2. Since, for a conservative system, T is a constant, independent of whether or not U(r) is a function of r, it may be concluded that Eq. (163) provides a reasonable result for  for any arbitrary form of U(r). This form converts Eq. (159) to the form
	 (r) = 0	(164)
or, equivalently, by using the definition of 
p2
	.	(165)
	h	=
An alternate form of this equation involving the potential energy U(r) is obtained by utilizing Eq. (145) for p2, which leads to what is referred to herein as the “master equation”
 (r) = 0.
(166)
B. Approximation to the Master Equation in the Nonrelativistic Limit
In the nonrelativistic limit
	p ,	(167)
 
where (T) is the Newtonian total energy discussed in Section V.E. Thus, Eq. (165) reduces in the nonrelativistic limit to the form
 , (168)
where φ is used instead of  to indicate the nonrelativistic result. This represents the general nonrelativistic equation for the motion of a particle in a region of variable potential energy.
C. The Schrodinger Equation¨
Equation	(168),	known	as	the	time-independent
Schrodinger equation, is usually written in the form¨
	  U j,	(169)
where the subscript denotes a set of possible solutions φj with attendant discrete values for the Newtonian total energy T(). The φj solutions are called the Schrodinger¨ time-independent energy eigenfunctions. Equation (169) is an energy eigenvalue equation, since it can be written in the form
	(T	) )	(170)
 
with the total energy operator T() defined by
()	h2 TU(r).	(171)
0
 
Usually, (T ) is denoted by  and is called the Hamiltonian operator. It is of the nature of an eigenvalue equation that an operator representing some physical quantity operates on a functions known as the eigenfunction [in this case, φj(r)] to produce the product of a constant with the eigenfunction.Theconstantistheeigenvalue.Itrepresents the constant of motion associated with the physical state represented by the eigenfunction.
Let us define an oscillatory, time-dependent function involving the Newtonian total energy T = j = hωj
for the particle
 iωjt). (172)
Multiplying Eq. (169) through by this factor leads to the equation
	h2	2
	− ∇ ψj + U j,	(173)
2m0 where
	ψj = φj(r)θj(t).	(174)
It can be noted from Eq. (154) and the subsequent development that with T0 =1, for a selected energy solution denoted by the subscript i, i = i(r)exp[−i/h) T()t]. In Eq. (174), with the choice θ0 =1, the corresponding nonrelativistic solution is given by ψi =φi(r)
 ]. The ratio of the two wavefunctions is
,	(175) ψ φ h
where 0 is the rest mass energy m0c2. The ψj are called the Schrodinger time-dependent eigenfunctions. Note that¨
	ih  j	(176)
∂t
so that Eq. (173) can be written in the form
	h2	2	∂ψj
− ∇ ψj + U(r)ψj = ih  . (177)
	2m0	∂t
This is a linear equation, so a general solution ψ can be constructed by superposition of all individual linearly independent solutions
	 j,	(178)
j
wheretheaj arearbitrarycomplexconstants.Thisiscalled the Schrodinger wavefunction. The equation analogous to¨ Eq. (177) representing the most general solution is thus
	2	∂ψ
	.	(179)
This is called the time-dependent Schrodinger equation.¨
D. Interpretation of Schrodinger¨ Equation Results
The idea underlying the Schrodinger equation is that the¨ wavelike behavior of matter, as postulated by de Broglie in 1923 and confirmed by the electron diffraction experiments of Davisson and Germer and by G. P. Thomson in 1927, should be capable of being described within the mathematical framework of a wave equation. The concept of wave equations, of course, underlies all of the present work, but Schrodinger was the¨ first to apply this idea to a theory for describing particles, from which he developed that ubiquitous workhorse of present-day quantum mechanics known as the Schrodinger equation.¨
Now it should be pointed out straightway that the Schrodinger equation was not in any strict sense¨	“derived” by Schrodinger. In fact, it cannot be rigorously derived. It¨ only can be rationalized in its form and then shown to predict results that agree with experiment. The conventional approach to this rationalization process can be found in nearly any standard quantum mechanics textbook. In the present work, a more novel approach has been developed based on the more general concept of dispersion relations. In many respects, this represents an intuitively satisfying approach. Be that as it may, the time-independent and time-dependent Schrodinger equations are usually written¨ in the forms given by Eqs. (169) and (179), respectively. The complexity of the differential equations given by the time-dependent and time-independent Schrodinger equa-¨ tions is related directly to the complexity of the potential energy U(r) for the problem in question.
Solutoin of the Schrodinger equation gives functions¨ ψ() that are usually complex. The square of the magnitude of ψ() evaluated at position r has been interpreted by Born (1882–1970) as the relative probability that the particle is located at that position. By judicious choice of values for the otherwise unspecified constants, such as T0 and θ0 in Eqs. (156) and (172), respectively, the integral of the probability over all space can be set equal to unity, a process called normalization. This is physically meaningful because the particle is presumed to be somewhere but not to be at more than one place at a given time. The normalization process requires that the wavefunction decrease sufficiently rapidly with distance away from the general location of the particle to give a bounded value for the integral of the square of the function. This restriction severely limits the physical set of solutions from the great numberofmathematicalsolutionsthatformallysatisfythe
Schrodinger equation.¨
For the hydrogen atom, for example, where the relevant potential energy for the time-independent Schrodinger¨ equation [Eq. (169)] is given as U(r)=−e2/4πε0r by Eqs. (2) and (5), with Z =1, the various functions φj satisfyingtheequationandmeetingthephysicallyreasonable boundary conditions constitute a discrete set. The attendant energies j are essentially those given by Eq. (33), which are deduced by the simpler Bohr theory. A logical extension of the potential energy to include the energy of the electron-spin magnetic moment in an external magnetic field leads to a close correlation of the quantum mechanical predictions for the energy levels of the oneelectron atom with detailed, experimental, optical spectral data.
Other standard problems can be attacked with the knowledge developed to the present point. One such problem is that of the one-dimensional, simple harmonic oscillator, characterized by the potential energy U , where K is a constant. This problem has applications in a number of fields; e.g., the harmonic oscillator is important for quantized lattice vibrations (phonons) in solids.
Other revealing problems are those of a particle trapped in one-dimensional and three-dimensional boxes. The “particle in a box” model is quite important for the freeelectron theory of metals as well as for the consideration of present-day quantum-well semiconductor devices. The general problem is actually quite analogous to the analysis of electromagnetic radiation at thermal equilibrium with the conducting walls of a cavity. The density of allowed modes is computed essentially the same way for both problems.
Later, several standard one-electron problems will be examined. However, let us first develop the concept of quantum mechanical current density and apply it to problems involving constant potentials for which plane-wave solutions to the Schrodinger equation are appropriate.¨
VII. QUANTUM MECHANICAL CURRENT DENSITY AND PARTICLE BEAMS
A. Probability Current Density
The probability density ρ =|ψ(r,t)|2 represents a convenient starting point for the consideration of particle and chargecurrentsascomputedinquantummechanics.Ifthis is considered to be a statistical quantity that is a continuous function of position, then the time derivative gives the rate of change of the particle density with time
	∂ρ ∂	 
 =	∗	(180) However, a time rate of change of the probability density at any given point in space requires a difference between the particle currents flowing into andout of the differential volume surrounding the point in question. The mathematical statement of this fact is the well-known microscopic equation of continuity
	 J	(181)
∂t where ∇ · J is the divergence of the particle current J at the point in question.
Equating Eqs. (180) and (181) for ∂ρ/∂t gives the
relation
	 	(182)
that must be obeyed by the quantum mechanical analog of the particle current density J. For further development of this expression, the time-dependent Schrodinger equation¨ (179) and its complex conjugate can be employed:
	ih U(r)ψ	(183)
	∂t	2m
∂ψ∗
 . (184)
Taking the complex conjugate utilizes the relations r∗ =r, t∗ =t, and U(r)∗ =U(r) due to the fact that the concern is with real positions, real times, and real potential energies. Multiplying the Schrodinger equation by¨ ψ∗ and its complex conjugate by ψ gives
ih U(r)ψ (185)
	∂t	2m
	∂ψ∗	 
Subtracting Eq. (186) from Eq. (185) gives
ih ,
(187)
where, in equating ψ∗U(r)ψ with ψU(r)ψ∗, the property of U(r) is utilized merely as a multiplicative operator, so that the factors in the product ψ∗U(r)ψ commute. The right-hand side of Eq. (187) involves the Laplacian operator, so that it is reasonable to expect that perhaps it can be expressed as the divergence of some vector quantity. Taking the divergence of ψ∗∇ψ yields
	∇ · (ψ∗∇ψ) = ∇ψ∗ · ∇ψ + ψ∗∇2ψ,	(188)
whereas taking the divergence of ψ∇ψ∗ gives
	∇ · (ψ∇ψ∗) = ∇ψ · ∇ψ∗ + ψ∇2ψ∗.	(189)
Recognizing that the dot product of two vectors such as ∇ψ ·∇ψ∗ is commutative, so that ∇ψ ·∇ψ∗ =∇ψ∗ · ∇ψ, these two quantities can be subtracted to give the
relation
∇ · (ψ∗∇ψ − ψ∇ψ∗) = ψ∗∇2ψ − ψ∇2ψ∗. (190)
The right-hand side of Eq. (190) can be identified with the factor in the right-hand side of Eq. (187), so that ih 
Substituting into Eq. (182) for ∇ · J gives h
 .
Within an arbitrary constant, then	(192)
h
	J	∗	∗ .	(193)
2
The arbitrary constant is zero if J=0 whenever ψ =0, as one would expect. Knowledge of the wavefunction ψ therefore allows one to calculate the particle current density J in quantum mechanics. For the case of electrons, the charge per particle is −e, so that the charge density  follows immediately from
	 = −eJ.	(194)
ItisilluminatingtoapplytherelationgivenbyEq.(193) to the specific case of plane waves exp(ik · r), which can be shown to be eigenfunctions of the so-called momentum operator∇ψ =−∗, so thatih∇. Thus, ∇ψ =(i/h)pψ. Also
∗ =(−i/h)pψ
	J	2mi 	h	−	h	
p
	= 2m (ψ∗ψ + ψ∗ψ) = ψ∗ψv.	(195)
This is simply the product of the particle probability density ψ∗ψ and the particle velocity v, which is readily interpreted as the particle current density on the basis of physical considerations.
B. Piecewise Constant Potential Energy Problems
It is worthwhile to work through the details of an illustrative example that typifies the quantum treatment of a particle-beam incident on potential energy steps, rectangular potential barriers and wells, and arrays of configurations that may be useful in understanding currents in modern solid-state devices. Figure 4 illustrates the three regions defined by the potential energy function chosen for this example:
0
U(x) = U0
W	(x < 0)
(0 ≤ x ≤ L).
(x > L)	(196)

 
FIGURE 4 Piecewise constant potential energy regions. [Fig. 1.34 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproducedwiththepermissionofAcademicPress,DoverPublications, and the author.]
The figure is drawn with U0 >0 and W <0, but actually either sign is possible for either parameter. Whenever W →U0, the limit is a single potential step; it constitutes a step up for U0 >0 but a step down for U0 <0. Whenever W →0, the limit is a rectangular barrier if U0 >0 but a rectangular potential well if U0 <0. The rectangular potential barrier is a common example used to illustrate quantum tunneling, which is a penetration of the barrier for particle energies  below the barrier height U0, even though such penetration would be disallowed from the standpoint of classical physics. The results are immediately applicable to the tunneling of electrons between metals separated by a thin insulator.
Before considering the several possible cases individually, let us first clarify the predictions of classical physics for this example to sharpen our understanding of the problem and to highlight the differences in the predictions of the quantum mechanics and classical mechanics theories. Classically, if >U0 and > W, there is total transmission, since the momentum of the particles does not change sign and is not decreased to zero as the particle crosses the barriers. On the other hand, the classical picture states that whenever <U0, all particles will be reflected by the barrier,sothereshouldbenotransmissionthroughthebarrier. As will now be shown, the quantum mechanics predictions are somewhat different. The classical mechanics result is more straightforward in a sense, because the reflection or transmission, as the case may be, is total. The quantum mechanics results, on the other hand, are a bit more mysterious, there being cases of partial transmission and partial reflection of a particle beam. The quantum mechanics predictions, however, are found to agree with the experimental results.
C. Incident Beam with Particle Energy Exceeding Both Steps
This is the case for >U0 and > W, algebraically speaking. All wavefunctions will be of the plane-wave type. The momentum is real, and propagation of the particle is possible, even in the classical sense. The problem will be developed in terms of the Schrodinger picture,¨ using ψ and φ, although the problem can be developed equally well within the framework of a relativistic master equation given by Eq. (166), using  and . Let the incident wave be given by
	ψinc = Aei(kx−ωt)	(197)
where, in the Schrodinger picture¨
k 	(198) with  representing the total Newtonian energy (T) and with

ω =  	(199) h
for this picture, in contrast to the ω given by Eq. (150) in the relativistic picture. The corresponding reflected wave can be written as
	ψref = Bei(−kx−ωt)	(200)
Then for region I in Fig. 4
	ψI = ψinc + ψref = (Aeikx + Be−ikx)e−iωt	(201)
The transmitted wave is the propagating wave in region III. Let us denote the transmitted wave by
where	ψtrans = Ce	− ,	(202)
i(x ωt)
	  .	(203)
In the absence of sources and other variations in region III that could lead to a reflected wave there, then
 
	ψIII = ψtrans = Ceixe−iωt.	(204)
Region II must now be considered. Due to the finite thickness of the region (0≤ x ≤ L) and the discontinuity at x = L, it is possible to have a reverse traveling (reflected) wave in this region in addition to a forward propagating wave. Denote the forward wave by [Fei(βx−ωt)] and the reverse wave by [Gei(−βx−ωt)], where
	 	(205)
then
	ψII = (Feiβx + Ge−iβx)e−iωt.	(206)
The boundary condition at x =0 of wavefunction
continuity
	ψI(0) = ψII(0)	(207)
issufficienttoensurecontinuityoftheparticledensity.The boundary condition of continuity of the first derivative of the wavefunction
d
(208)
dx
is sufficient to ensure continuity of the current density, as can be noted from Eq. (193). These two conditions lead directly to the following two relations:
A + B = F + G	(209)
ikA − ikB = iβF − iβG.
Rewriting this pair of equations in the form	(210)
A + B = F + G	(211)
	A  	(212)
makes it easy to obtain expressions for A and B in terms of F and G. Adding the two equations gives
A	 	(213)
and subtracting the two equations gives
B	 .	(214)
	Fe	+ Ge−	= Ce	(215)
	iβFeiβL − iβGe−iβL = i Cei	L.
Rewriting this pair of equations in the form	(216)
Let us next apply boundary conditions at the barrier discontinuity at x = L. Continuity of the wavefunction ψII(L)=ψIII(L) and continuity of the first derivative of the wavefunction dψII
dxx=L lead directly to two additional relations:
	iβL	iβL	iL
Fe	+ Ge−	= Ce	(217)
FeiβL − Ge−iβL =L β
(218)
	iβL	iβL	iL
leads to expressions for F and G in terms of C. Adding the two equations gives
F	 Cei	L
	 .	(219)
and subtracting the two equations gives
G	 Cei	L
	 .	(220)
Substitutingthetwoexpressionsjustobtainedfor F and
G into the expressions previously obtained for A and B gives A and B in terms of C:
A 
 iβL
	 Cei	L. (221)
B 
 iβL
	 Cei	L. (222)
Thus, the relationship between A and C and the relationship between B and C are obtained.
The product [(A/C)∗(A/C)], which is useful for the transmission coefficient, can now be evaluated:
 eiβL
 
 iβL
 
+ e2iβL 
+ e 
 
	 	(223)
The transmission coefficient	follows from the ratio of the transmitted intensity Itrans to the incident-beam intensity Iinc:
Substituting the evaluation for the denominator given in Eq. (223) then yields the transmission coefficient.
The reflection coefficient  can be obtained from the ratio of the reflected intensity to the incident-beam intensity:

(225)
Already B in terms of C and A in terms of C have been obtained. The ratio of these two expressions then
gives
It can be shown that  ), which means that whatever current density is not transmitted is reflected. Now let us consider the limit W →0, in which case
Thus, the following limit is obtained:
	=
8
 .
[6+(β/k)2 +(k/β)2]+[2−(β/k)2 −(k/β)2]cos2βL
	B	[1 − (β/k)][1 + ( /β)]e−iβL +  [1 + (β/k)][1 − ( /β)]e
	=	.	(226)
A	[1 + (β/k)][1 + ( /β)]e−iβL + [1 − (β/k)][1 − ( /β)]eiβL Thus
 
(227)
or, equivalently
 
(230)
This rectangular barrier solution contrasts markedly with the classical result	=1. The cosine factor in the denominator leads to a decided oscillatory dependence of the transmission coefficient on energy of the incident particles, as will be demonstrated later in a graphical example. If, in addition, the barrier height U0 is taken to be zero, then β =k and	=1, as expected. This limit is also well approximated for  , since then  .
In the alternate limit, W →U0, so that  →β, and
Eq. (224) yields
4 k
		 .	(231)
This is the transmission coefficient for a step potential of height U0 for the case >U0. In this same limit W →U0, Eq. (228) for the reflection coefficient reduces to
	 .	(232)
D. Incident Beam with Particle Energy below First Step Only
Let us now consider a case for which W <<U0 algebraically. For <U0, the wavefunction in region II (see Fig. 4) cannot be of the plane-wave type, because the kinetic energy would be negative and the momentum consequently would be imaginary. It is easy to show that the wavefunction
	ψII = (De−αx + Eeαx)e−iωt	(233)
satisfies the Schrodinger equation¨
∂ψ
(234)
t
appropriate for this region, where α is obtained by substituting ψII into the equation
h2
	 iω)ψII,	(235)
which gives
h2
	  U0	(236)
or, since hω = 
	 .	(237)
The positive sign is conventionally chosen for α; the choice of a negative sign would simply interchange coefficients D and E.
Since > W, the solution in region III (see Fig. 4) is again of the propagating type:
ψIII = ψtrans = Cei(x−ωt) = Ceixe−iωt. (238)
As before, the wavefunction ψ1 for region I is ψI = ψinc + ψref
	= (Aeikx + Be−ikx)e−iωt,	(239)
where the constants   and k have their previously defined values
	 	(240)
k(241)
The boundary conditions at x =0 of continuity of the wavefunction ψI(0)=ψII(0) and continuity of the first derivative of the wavefunction d dx
lead directly to the following two relations:
A + B = D + E	(242)
ikA − ikB = −αD + αE.
Rewriting this pair of equations in the form	(243)
A + B = D + E	(244)
	A  )	(245)
makes it easy to obtain expressions for A and B in terms of D and E. Adding the two equations gives
A	 	(246)
and subtracting the two equations gives
B	 .	(247)
Next, let us apply boundary conditions at the barrier discontinuity at x = L. The conditions of continuity of the wavefunction ψII(L)=ψIII(L) and continuity of the first derivative of the wavefunction d
	dx x=L	dx x=L
lead directly to the two additional relations:
	De−	+ Ee	= Ce	(248)
	−αDe−αL + αEeαL = i Cei	L.
Rewriting this pair of equations in the form	(249)
	αL	αL	iL
De−	+ Ee	= Ce	(250)
De	 Ce L.	(251)
	αL	αL	iL
leads to expressions for D and E in terms of C. Adding the two equations gives
D	 Cei	L
L
(252)
and subtracting the two equations gives
E	 Cei	L
L
	.	(253)
Substituting these two expressions for D and E into the expressions obtained in Eqs. (246) and (247) for A and B gives A and B in terms of C:
A 
 eαL
	 Cei	L. (254)
B 
 
 eαL
	 Cei	L. (255)
Thus, the relationships between A and C and between B and C have been obtained. The ratio of B to A now is easily obtained:
 
	B	[1 + (α/ik)][1 − (i /α)]eαL + [1 + (α/ik)][1 + (i /α)]e−αL
A = [1 − (α/ik)][1 − (i /α)]eαL + [1 + (α/ik)][1 + (i /α)]e−αL
= [1 − (i /α) + (α/ik) − ( /k)]eαL + [1 + (i /α) − (α/ik) − ( /k)]e−αL
[1 − (i /α) − (α/ik) + ( /k)]eαL + [1 + (i /α) + (α/ik) + ( /k)]e−αL = {[1 − ( /k)] − i[( /α) + (α/k)]}eαL + {[1 − ( /k)] + i[( /α) + (α/k)]}e−αL
L
(256)
The reflection coefficientcan be obtained from the ratio of the reflected intensity Iref to the incident-beam intensity Iinc:
	.	(257)
Therefore
  Since, for arbitrary  ) and sinh(	), it follows that cosh2(θ)=1+ sinh2(θ) and
cosh2(θ)+ sinh2(θ)= cosh(2θ). Thus
 
 
	 .	(259)
The transmission coefficient	is readily evaluated from this expression for the reflection coefficient:
		= 1 − 
 
	 . 	(260)
 
If the limit W →0, then  →k and the transmission coefficient reduces to that for a rectangular barrier:
	 
 
This is the transmission coefficient for particles having energy <U0 through a rectangular barrier of height U0. If the further limit αL 1, then sinh( L and the approximate form is
	 
1 + (1/4)[(k/α) + (α/k)]2(1/4)e2αL
2
e−2αL. (262)
	[(	) + (	k)]2	1 + (	k)2
If the barrier thickness L approaches infinity, then the potential energy becomes a step potential and the transmission coefficient can be noted from Eq. (262) to approach zero for the presently considered case of <U0.
Torecapitulate,theremarkablequantummechanicalresulthasbeenderivedthatparticlescan,insomecases,penetrate potential energy barriers that are even higher than the particle energy. This result, which contrasts markedly with the classical result that	=0, has the greatest relevance for quantum electronic devices. It likewise provides the explanation for the decay of radioactive nuclei by αparticle emission.
An example calculation spanning the domains for <
U0 and >U0, with W =0 for both cases, has been carriedout.Thevalueoftheelectronicmassisutilized,and the rectangular barrier is chosen to have a thickness of
10 A and a height of 10 eV.˚ Figure 5 illustrates the variation of the transmission coefficient with incident electron energy. The remarkable oscillatory behavior is due to the wavelike nature of the particle; the peaks coincide with certain relationships between the de Broglie wavelength
 
FIGURE 5 Transmission coefficient versus incident-particle energy for a rectangular potential energy barrier. [Fig. 1.35 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the
author.]
and the barrier thickness, which can be deduced from Eq. (230). Note that	approaches unity whenever cos(2βL)=1, which occurs when 2βL =2mπ (m =
1,2,3,...). Since β =2π/λII, the condition is met when m(λII/2)= L (i.e., whenever there are an integer number of half wavelengths over the barrier distance L). On the other hand, for (2m +1)(λII/4)= L, which corresponds to an odd-quarter wavelength over the barrier distance L, then cos(2βL)=−1 and the transmission coefficient goes through the value 4/[(β/k)+(k/β)]2. In this odd-quarter wavelength condition, for βk corresponding to particle energiesnotfarabovethebarriermaximum,	 , which is very small in value. Thus, there are transmission resonances as the particle energy continuously increases above the barrier height U0. For the odd-quarter wavelength condition with the particle energy far exceeding the barrier height, however, β is not too different from k and so	is not much less than unity. In short, the depth of the transmission resonances decreases as  increases.
It should be pointed out that although the odd-quarter wavelength condition usually provides a very good approximation for minimum	, it does not provide the exact minimum. A quantitative evaluation based on d	/d=0 for fixed U0, utilizing Eq. (230), leads to the condition
βL
	tan(βL) =	 +
	1	(β/k)2
and the roots of this equation yield the distinct values of  for minimum	. This transcendental equation can be solved graphically. The problem is simplified in the limit where (β/k)2 1, since then the roots depend only on the energy difference above the barrier, thereby leading to pure wavelength conditions in the barrier region itself for the transmission minima. Further, in the large βL limit, the equation requires tan(βL) to be large, so that the roots approach values that are approximately the same as the values leading to the odd-quarter wavelength condition just discussed.
Finally, care must be taken not to draw the erroneous conclusion from a casual inspection of Eq. (230) that 	is unity when β =0, which corresponds to the particle energy being equal to the barrier height. A similar erroneous conclusion also could be reached from Eq. (261) in the same limit, since then α is zero. Careful inspection of these two equations reveals indeterminate forms in the denominators of the equations for this limit. In Eq. (230), for example, the two terms in the group [(k/β)2 −(k/β)2 cos(2βL)] approach ∞→∞ as β → 0, but by noting the equivalence to 2(k/β)2 sin2(βL), the indeterminateformyields2(kL)2 asβ → 0.AsgivenbyEq. (230),	therefore approaches [1 + (kL/2)2]−1 as β →0. In a similar manner, Eq. (261) can be shown to approach this same limit. The continuity in	at the limiting energy of 10 eV can be noted in Fig. 5.
E. Incident Beam with Particle Energy Below Both Steps
As a final consideration, let us examine the situation in whichtheparticleenergyislessthanthepotentialenergy in region II and in region III. Algebraically, this is the case when <U0 and < W. At the limit W →U0, this case reduces to the single step potential. In any event, since region III extends to x =∞, the probability density in region III can be expected to approach zero as x →∞.
The wavefunction for region III thus may be chosen to be
	ψIII = He−γ xe−iωt,	(263)
where
	 .	(264)
Matching the wavefunctions and the first derivatives at x = 0 yields the same results for the relationships among A, B, D, E as given by Eqs. (242)–(247), since the wavefunctions in regions I and II are exactly the same as for the case W <<U0. However, the matching of the wavefunctions and their first derivatives at x = L is different, since ψIII is now different. The result obtained from this matching is
De−αL + EeαL = He−γ L	(265)
−αDe−αL + αEeαL = −γ He−γ L.
Writing this pair of equations in the form	(266)
De−αL + EeαL = He−γ L	(267)
	De  L	(268)
facilitates the algebra. Adding these two equations leads to
D	  L	(269)
and subtracting these two equations leads to
E	 .	(270)
Substituting these two expressions for D and E into the previously derived expressions for A and B—namely,
A 
B 
yields
A
(273)
B
(274)
The ratio of these two expressions gives
A	= [1−+(α/ik)][1++(γ/α)]++[1+−(α/ik)][1−−(γ/α)]
B	[1	(α/ik)][1	(γ/α)]	[1	(α/ik)][1	(γ/α)]
	[1+(	)+1	(	)]	(α/ )[1+(	)	1+(γ/α)]
(γ/α)]
(275) The reflection coefficient for this case is
	 .	(276)
Substituting yields
 
	 ,	(277)
which is to be expected on physical grounds for this situation. These results have practical significance for modern quantum well devices based on multilayered semiconductors.
This completes the consideration of particle currents incident on stepfunction-type barriers. The basic approach also has some relevance for the simplest boundstate problem—namely, the problem of a particle trapped in a rectangular potential well—which is considered in Section VIII.
VIII. BOUND-STATE PROBLEMS
A. Introduction
A particle may be confined to a certain region of space by potential energy barriers surrounding it; e.g., the step potentials treated in Section VII could be placed on both sides of a particle having a lesser energy. Figure 6 illustrates an arbitrary potential energy function in one dimension. At positions x1 and x2, the potential energy U(x) equals the total energy  of the particle, so that the kinetic energy k, at these points given by [−U(x)], is necessarily zero. These positions are called classical turning points, because according to classical physics, the particle would simply be reflected from the barrier at these positions. The momentum becomes reversed upon reflection. In three dimensions, the situation is similar, except that it is the perpendicular component of the momentum that is reversed (comparable to the elastic rebound of a rubber ball from a concrete wall). The motion of the particle continues back and forth over the region x1 < x < x2 in the potential well delineated by the surrounding energy barries, provided the potential energy everywhere outside this region exceeds the total particle energy. The total energy  is conserved, with a continuous interchange of kinetic and potential energies.
The detailed time-dependence of the motion of a particle in a potential energy well depends upon the exact functionalformofthepotentialenergyU(x).Thecharacteristic
 
FIGURE 6 Potential energy well of arbitrary shape. [Fig. 1.38 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the
author.]
feature of bound-state problems in quantum mechanics is the fact that the application of realistic boundary conditions to the time-independent Schrodinger equation, given¨ by Eq. (169), forces a restriction on the energy values, so that the eigenvalues for the total energy are confined to a discrete set. This feature is independent of the particular functional form of the potential energy, although the details of the energy-level spectrum are dependent upon the form of U(x). In the following discussion, three different bound-state problems, for which the potential is given by squarewell, harmonic oscillator, and Coulomb potentials, are considered individually.
B. Three-Dimensional Potential Energy Square-Well Problem
Let us consider a particle of mass m confined to a region of space having the shape of a rectangular parallelepiped. The particle confinement is due to infinite potential energy barriers at the faces of the parallelepiped box. This is sometimes referred to as a square-well potential because the potential energy rises so sharply (with infinite slope) at the boundaries of the parallelepiped. If the potential energy inside the parallelepiped is taken to be zero, then the Hamiltonian  for the time-independent andtime-dependentSchrodingerequations[¨   and ψ =ih ∂ψ/∂t, given by Eqs. (169) and (179)] takes the form =−(h2/2m)∇2 within the box but is undefined outside the box, where the potential energy is considered infinite. Thus, a wavefunction ψ exists for the interior but is zero for the exterior, where the particle cannot penetrate. The time-independent Schrodinger equation for the¨ interior of the box is formally the same as that for a free particle, namely,
 
which has solutions given by the normalized plane-wave spatial functions
	 ik · r],	(279)
where V is the volume of the box. These spatial functions, whencombinedwiththetimefactorexp[  ],represent running waves
	 ,	(280)
whichconstitutethestationary-statewavefunctionsforthe particle that satisfy the time-dependent Schrodinger equa-¨ tion. These traveling-wave eigenfunctions of the Hamiltonian having the form exp[(i/h)(p · r−t)] are simultaneous eigenfunctions of the linear momentum operator  =−ih∇, since it can be noted by direct substitution
that
 ψk(r,t) = (−ih)[∇(ik · r)]ψk(r) = hkψk(r). (281)
Even though such plane-wave solutions formally do satisfy the Schrodinger equation for this problem, they do¨ not satisfy the constraint that the probability density be continuous at the walls of the box, since continuity of the wavefunction requires the wavefunction to be zero inside the box at the walls in order to equal the zero wavefunction exterior to the box. This underscores the vital role of boundary conditions in quantum mechanical solutions. AsdescribedinSectionIV.F,however,oppositelydirected but equal-amplitude plane waves can be superimposed to give standing-wave solutions that may satisfy the desired boundaryconditions.Letusconsiderthesixinfinitelyhigh potential energy barriers delimiting the rectangular parallelepipedboxtobeperpendiculartothex, y,andz axesand tobelocatedatx =0,x = Lx, y =0, y = L y,z =0,z = Lz.
The box confining the particle thus has edges of length Lx, L y, and Lz in the x, y, and z directions, respectively. One form of the three-dimensional, normalized standing waves providing solutions to the Schrodinger equation for¨ this problem is given by
 ,
(282)
where nx, ny, and nz are a triplet of positive integers represented by the symbol n. This product of sine functions satisfies the fixed boundary condition that the wavefunction vanish on six faces of a rectangular parallelepiped, and direct substitution shows that it satisfies the threedimensionalSchrodingerequationgivenbyEq.(278).The¨ corresponding quantized energy eigenvalues n thereby obtained are
n 
Only the positive integers are chosen for the triplet nx, ny, nz in the wavefunction given by Eq. (282), since the corresponding negative values yield the same wavefunction to within a factor of −1. This would represent exactly the same state for all practical quantum mechanical calculation purposes, because the particle probability density ψ∗ψ would be the same. It is a very general aspect of quantum mechanics that linearly dependent eigenfunctions are redundant whereas linearly independent eigenfunctions are not.
The standing-wave solutions of the Schrodinger equa-¨ tion given by Eq. (282) do not represent states having definite momentum values, but instead are linear combinations of plane-wave states having oppositely directed momenta. Because the particle undergoes reversals in momentum associated with reflection in the neighborhood of the classical turning points, it is not surprising that the most appropriate solutions to the problem are not those states that represent definite momentum values.
Because the standing-wave solutions can be viewed as the superposition of traveling-wave solutions of equal amplitude traveling in opposite directions, plane-wave solutions can be utilized for the present problem by means of a construct known as periodic boundary conditions: φ(x + Lx, y, z) = φ(x, y, z) φ(x, y + L y, z) = φ(x, y, z) (284)
φ(x, y, z + Lz) = φ(x, y, z).
This represents a substitute for the fixed boundary conditions previously invoked to determine the allowable k values. This is the approach generally used in the development of the free-electron theory of metals. It has the utility of simplifying the mathematics a bit while retaining the essential property of the correct number of quantum states per unit energy range required for quantum statistical calculations.
C. The Harmonic Oscillator Potential
Anotherveryimportantbound-statepotentialenergyfunction is the harmonic oscillator potential
	U 	(285)
illustrated in Fig. 7. For a one-dimensional harmonic oscillator consisting of a mass M attached to a fixed spring (with force constant K), which is set into motion on a horizontal; frictionless planar surface, the clas-
 
FIGURE 7 Harmonic oscillator potential. [Fig. 1.39 in Quantum MechanicsforAppliedPhysicsandEngineeringbyAlbertThomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the author.]
sical frequency given by the reciprocal of the period is ν0 =ω0/2π =(2π)−1(K/M)1/2. Other examples of classical harmonic oscillators also are characterized by some specific frequency (with corresponding angular frequency ω0 =2πν0) determined by the physical parameters of the system in question. The analogous quantum problem has solutions that can be expressed in terms of this classical frequency ν0.
The Hamiltonian for the harmonic oscillator problem is
	  Kx2	(286)
and the time-independent Schrodinger equation given by¨
Eq. (169) for this problem is
  Kx2 
The complete time-dependent solutions ψn(x,t) then are given as usual, by taking the product of the spatial functions with the corresponding time-dependent function  ], so that
	 .	(288)
In the present case
	 )	(289)
with
mω0
α ≡  .	(290) h
The functions Hn(y) appearing in Eq. (289), with y ≡ α1/2x, are the Hermite polynomials. These polynomials are readily generated by means of the differential relation
	dn	2
Hn y )]. (291)
Some examples of the lower-order Hermite polynomials are
H0(y) = 1
H1(y) = 2y
H2(y) = 4y2 − 2
H3(y) = 8y3 − 12y
H4(y) = 16y4 − 48y2 + 12
H5(y) = 32y5 − 160y3 + 120y
H6(y) = 64y6 − 480y4 + 720y2 − 120
H7(y) = 128y7 − 1344y5 + 3360y3 − 1680y. (292)
The normalization factors N  for the eigenfunctions, as found from the normalization integral
	 n dx = 1	(293)
are given by
	  .	(294)
The various eigenfunctions φn(x) are orthogonal, this being a common occurrence in all quantum solutions representing different energies. Plots that illustrate these lowerorder harmonic oscillator eigenfunctions can be found in various textbooks. The average amplitude for the vibrational motion increases with increasing-energy eigenvalues, in qualitative agreement with the predictions of the classical treatment. Beyond this point, there is little apparent similarity unless one examines the solutions in the so-called correspondence limit of very large quantum numbers.
Therequirementthatacceptablewavefunctionsordinarily must be capable of normalization is what actually leads to the Hermite polynomial solutions. This requirement simultaneously leads to the discrete spectrum of quantized energy eigenvalues
n  
 ,...,∞), (295)
where ω0 is the angular frequency for the classical mechanics solution. The integer n is the quantum number for this problem. An interesting feature of the quantum solution is the fact that the ground-state energy (n =0) is nonzero.Furthermore,theenergylevelsareevenlyspaced. The dashed lines in Fig. 7 indicate this energy-level spectrum.
Thetopicoflatticevibrationsinsolidsisoneexampleof an important physical problem that can be treated in terms of the harmonic oscillator. The fact that the ground-state energy is nonzero means that even at a temperature of zero Kelvin,therewillbesomevibrationalmotionofthelattice. Such motions are the so-called zero-point vibrations.
Another interesting feature of the quantum solution is the dependence of the energy upon the frequency of oscillation. The increase in amplitude (see Fig. 7) that accompanies larger values of the energy n for the classical solution seems almost incidental to the quantum solution, whereas in the classical solution, the dependence of energy upon amplitude appears as a central feature in the analysis.
The energy  ) required to excite a quantum oscillator of frequency ω from a state of quantum number n to the state of quantum number n can be noted from
Eq. (295) to be
 
	 	(296)
Thus, energy absorption occurs in integer multiples of a basic unit of energy hω, which is characteristic of the oscillator frequency. Analogously, the energy emission due to the deexcitation of an oscillator of frequency ω from a state of quantum number n to the state of quantum number n is the converse of the absorption process. If the energy is emitted in the form of a photon of energy photon =hνphoton, then the frequency of the photon will be  n)νosc and the wavelength of the emitted photon will be λphoton = c/νphoton  ]. This leads to the quantum transition picture indicated in Fig. 2.
D. Use of the Schrodinger Equation for the¨ Hydrogen Atom and One-Electron Ions
The first difficulty encountered in the use of classical mechanics was in the area of radiation absorption and emission by atoms in gases. Instead of the continuous spectra predicted by the classical mechanics approach (see Section I.D), discrete optical spectra were obtained (as described in Section III.D). Although the 1913 semiclassical approach of Bohr (see Section III.F) was successful in explaining such discrete spectra for hydrogen and also for one-electron ions, there was no way to extend the Bohr theory to the two-electron atom (helium) or similar twoelectron ions, much less to even higher electron atoms and ions. An approach that could explain only such a limited regionoftheperiodictable(i.e.,oneelement—namely,hydrogen)obviouslywasinadequateandultimatelyhadtobe replaced by a more general theory. In 1926, Schrodinger¨ developed what was to be the genesis of such a more general approach [see Section III.E].
Let us now devote some attention to the solution of the Schrodinger equation for the hydrogen atom and the¨ closely related problem of the one-electron ion, the potential energy for both being given by
2
	U,	(297)
4πε0r
where Ze is the electrical charge of the nucleus andr =|r| is the separation distance between the centers of the two charges. This potential energy as a function of separation distance appears as solid curves in Fig. 8. Although this is formally a two-body problem, it can be reduced to a one-body problem by transforming to the center-of-mass coordinate system. The so-called “reduced” mass of the
 
FIGURE 8 Coulomb potential. [Fig. 1.40 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the author.]
electron given by
mem p
m =  + , (298) me m p
where me is the actual electron rest mass and m p is the proton rest mass. The Hamiltonian
	 = − h2 ∇2 + q1q2	(299)
	2m	4πε0r
withnuclearchargeq1 = Z1eandelectronchargeq2 =−e, istobeusedinthetime-independentSchrodingerequation¨  n. The key to solving this so-called hydrogenatom problem is the recognition that the Coulomb potential energy of interaction between the electron in question and the nucleus depends only upon the separation distance r ≡ |r| and is independent of the spatial orientation of the line of centers between electron and nucleus. Therefore, in spherical polar coordinates (r,θ,φ), the Schrodinger¨ equation can be separated (in the usual way variables are separated in partial differential equations) into three equations, each involving a function of one of these three variables. In spherical polar coordinates, the Laplacian ∇2 of any arbitrary scalar function f of the vector r is given by
 
 
The variables separation technique then leads to three separated equations for the factors R(r), (θ), and (φ) appearing in the product form of the spatial portion of the wavefunction  ), with the corre-
sponding wavefunction being
	 .	(301)
Onlytheequationfor R(r)containstheCoulombpotential energy of interaction between electron and nucleus.
Single-valuedness of the wavefunction is necessary because the probability density ψ∗ψ is a physical quantity that must have only one value at a given point in space. The separation constant in the equation for (φ) is found to lead to a wavefunction ψ(r,t) ∝ exp(imφ), which is single-valued whenever the angle φ is increased by multiplesof2π onlyifm isequaltoaninteger.Them constitutes one quantum number characterizing the electronic state. It is called the magnetic quantum number, since its value determines the energy change when the ion is placed in a magnetic field. It is conceivable that m has allowable values of 0,±1,±2,..., although an upper bound on |m| is dictatedbyanotherconsideration(tobediscussedshortly). The resulting wavefunction factor (φ) is found to be an eigenfunction of the Hermitian operator  , which represents the z-component of the electron orbital angular momentum, with the eigenvalue being mh:
	  φ = mh (φ)	(m = 0,±1,±2,...). (302)
The differential equation for (θ) representing the θcomponent of the wavefunction ψ(r,t) contains m2 as well as a second separation constant λ. Whenever m = 0, the equation can be cast into a form known as Legendre’s differential equation. The solutions diverge unless λ =   1), where  represents a non-negative integer. The physically meaningful probability densities obtained for this choice of the second separation constant are represented by the solutions P(cosθ), known as the Legendre polynomials. These polynomials turn out to be eigenfunctions of the Hermitian operator [ ()]2representing the square of the orbital angular momentum of the electron, with eigenvalues  :
 
 
Therefore,  is called the orbital angular momentum quantum number.
Whenever m =0, the corresponding solutions to the
(θ) equation are the associated Legendre functions
Pm(cosθ), where m . The restriction on m is thus a mathematicalone,althoughittiesinverywellwiththecorresponding physics since the square of the z-component of the orbital angular momentum—namely, m2h2— cannot exceed the square of the total orbital angular momentum—namely,  —which, in turn requires
|m .
The differential equation for R(r) representing the rcomponent of the wavefunction ψ(r,t) contains the quantum number  as well as a third separation constant. The solutions can be expressed in terms of the associated Laguerre polynomials. The requirement that the solutions not diverge in order to have a physically meaningful probability density ψ∗ψ once again places severe restrictions on the separation constant. This, in turn, requires an integer quantum number n, known as the principal quantum number, together with the condition n >. In a straightforward way, this leads to the quantized energy eigenvalues
	1	Z2e2
	n  	(n = 1,2,3,...), (304)
where a0 is the parameter known as the Bohr radius
a 	(305) me2
since it equals the radius of the ground-state Bohr circular orbit previously deduced from Eq. (31) for n =1. The energy levels for the lower-energy states are indicated by dashed lines in Fig. 8.
From a different perspective, the hydrogenic eigenfunctionsresultingfromthemathematicalsolutiontothisproblem can be written in terms of the product
ψ = Rn 
 
m = 0,±1,±2,..., ,
where Rn(r)is the radial portion of the eigenfunction (which is correlated directly with the functional form of the Coulomb potential energy) and Ym(θ,φ)=m(θ) m(φ) is one of the spherical harmonics. The normalized spherical harmonics Ym can be written in terms of the associated Legendre polynomials Pm(cosθ):
Ym Pm(cosθ)eimφ.
(307)
Several of the lower-order associated Legendre polynomials are
 = 0	P 
 = 1	P 
P 
 = 2	P 
P  P 
 = 3	P 
	P 	(308)
P  P 
 = 4	P 
P  P 
P  P 
To obtain the corresponding polynomials for the negative m values, the relation
	P−m(cosθ) = (	 m   m)! Pm(cosθ)	(309)
can be utilized. The complete set of these polynomials can be generated in a straightforward manner.
The spherical harmonics actually are appropriate for all spherically symmetric potential energy problems. For this reason, they are used as the angular portion of the wavefunction in many approximate treatments of the manyelectron atom. Furthermore, the use of spherical harmonics is by no means restricted to quantum mechanics; e.g., they are utilized extensively in treating boundary-value problemsinelectrostatics.Theusefulnessderivesfromthe fact that they constitute a complete set of functions, so that any arbitrary function g(θ,φ) of θ and φ can be expanded as a linear combination of the spherical harmonics:
	g  amYm(θ,φ).	(310)
 
The coefficients determined from	am	in the linear combination are
	am d	(311)
with the differential d denoting the differential surface area on a unit sphere d= sinθ dθ dφ, with the limits of integration being 0 to π for θ and 0 to 2π for φ.
The normalized radial portion of the energy eigenfunctions for hydrogenlike atoms can be written in the form Rn eρ/ (ρ),
(312)
where
	 r.	(313)
The parameter a0 is the Bohr radius given by Eq. (31) with n = 1, and L  represents the associated Laguerre polynomials, which can be generated from the differential relation
	Ln+ (ρ)  	(314)
The lower-order Laguerre polynomials are therfore easily obtained, thereby yielding the radial portions of the oneelectronenergyeigenfunctions.Severalofthelower-order radial function are
n = 1	R e−ρ/2
n = 2	R ρ/2
R e−ρ/2
n = 3	R ρ/2 R ρ/2
	R ρ/2	(315)
n = 4	R 
R 
R ρ/2
R ρ/2.
To summarize the situation for the one-electron ion, the application of appropriate boundary conditions of singlevaluedness and boundedness on the wavefunction leading to the preceding solutions yields the three quantum numbers n, , and m, which are referred to, respectively, as the principal quantum number, the orbital (or azimuthal) quantum number, and the magnetic quantum number. The allowed values of the three integer quantum numbers (n,,m) required to characterize a given energy eigenfunction  ) for the hydrogen atom or one-electron ion have the following allowed values:
n = 1,2,3,...
	  1	(316)
It can be seen from these results that for a given n-value, therearen allowablevaluesandforagiven-value,there are 2+1 possible m values. Since the energy eigenvalues n given by Eq. (304) depend only on the value of the principal quantum number n and are independent of the values of  and m, it can be seen that there are many eigenfunctions for a given energy eigenvalue. The solutions for the hydrogen atom are therefore highly degenerate, except for the ground state (n  0). When thefourthquantumnumberms,representingelectronspin, is taken into account (ms = ±1/2), corresponding to spin angular momentum values of ±msh, two electrons can be accommodated in the ground state without violating the Pauli exclusion principle, developed by Wolfgang Pauli (1900–1958). That is, no two electrons have exactly the same set of quantum numbers.
Due to the degeneracy of the eigenfunctions, it is possible to construct new linear combinations for a given value of the principal quantum number n (i.e., for a given shell). Such alternative sets become extremely important where there are additional contributions to the energy that can be treated as perturbations. The appropriate choice of the basis set is often dictated by the symmetry of the perturbation.
The series of energy levels is modified in the presence of a magnetic field. There are two factors to consider— namely, the electron orbital angular momentum L for motion around the nucleus, and the intrinsic spin of the electron. A charged particle in orbit constitutes a circulating current,which,inturn,producesamagneticmoment.This so-called orbital magnetic moment µorb =−(e/2m)L interacts with an applied magnetic field B to give an additional energy term
	Uorb = −µorb · B,	(317)
which must be added to the Hamiltonian. With the magnetic field B= Bzzˆ oriented along the z-axis, the energy is mh Bz, where the integer m is the magnetic quantum number. Likewise, the intrinsic spin angular momentum of the electron with respect to an axis through its center of mass gives rise to a spin magnetic moment µs, which interacts with an applied magnetic field B to give the energy term
	Uspin = −µs · B,	(318)
which must be added to the Hamiltonian. Other energy terms also can arise, such as the energy of the interaction between the two magnetic moments µorb and µs that is designated the spin–orbit interaction energy.
E. Many-Electron Atoms and Ions
Firstofall,itisimportanttorecognizethatthepotentialenergy in a multi-electron atom depends upon the electron– electron Coulomb energies as well as on the Coulomb energy of interaction of each electron with the nucleus. Although the electron–electron interaction can be viewed asaperturbationforpurposesofverycrudeestimates,it,in fact, is much too large to be treated within the framework of perturbation theory. In the helium atom, for example, the potential energy involves the Coulomb potential energy of interaction of the attractive force between each electron and the nucleus plus the Coulomb energy of interaction of the repulsive force between the two electrons. Thewavefunctionψ thenmustbetakenatminimumasthe product of the wavefunctions for each individual electron intheatom.Theproblembecomesenormouslymorecomplicated to solve, requiring a numerical solution because anexactanalyticalsolutioncannotbefound.Nevertheless, the Schrodinger equation yields numerical results for the¨ two-electron atom problem that agree with experimental optical spectra. In this way, the Schrodinger equation pro-¨ vides the more general theory required to supplant the more limited Bohr theory.
The complexity of an exact numerical solution of the Schrodinger equation naturally increases greatly as the¨ number of electrons increases from two three. If only a few electrons are involved, as in the case for the lighter atoms, a variational treatment often can be used to obtain approximate solutions to the many-electron Schrodinger¨ equation.
For the heavier atoms, wherein a larger number of elecrons are involved, the starting point for the most calculations is the approximation that the total potential energy of interaction of a given electron with the nucleus and the other electrons can be represented by a spherically symmetric potential U(r), referred to as the central-field approximation. In practice, then, one of the most difficult parts of the problem is to estimate or calculate the potential. The details are beyond the scope of the present treatment; however, the results justify utilizing one-electron eigenvalues and eigenfunctions as a semantic framework for describing the multi-electron atom or ion. Thus, the product wavefunction
	 	(319)
is chosen to have the same form as that given by Eq. (301) for the one-electron atom. Once again, a set of four quantum numbers (n,,m, and ms) is required to specify an electronic state. The wavefunction specified by a given set of quantum numbers is called an orbital or, more specifically, an atomic orbital, in analogy with the older Bohr theoryinwhichelectronswereconsideredtotravelinplanetary orbits in accordance with classical mechanics.
The Pauli exclusion principle requires that no two electrons have the same set of quantum numbers [viz., the principal quantum number n characteristic of the total energy of the electron, the angular momentum (azimuthal) quantum number  characteristic of the total orbital angular momentum of the electron, the magnetic quantum numberm characteristicoftheorientationofthemagnetic moment with respect to the z-azis, and the spin quantum numberms characteristicoftheorientationoftheelectronspin magnetic moment]. The orbital angular momentum and magnetic quantum numbers  and m for the multielectron atom or ion are the same as the quantum numbers  and m in the hydrogen atom, since the variables separation with the more general central potential U(r) proceedsinexactlythesamewayasfortheone-electronatom, forwhichU(r)=−Ze2/4πε0r,therebyyieldingthesame equations for the (θ) and (φ) factors in ψ(r,t). The electron-spin quantum number ms =±1/2 is likewise the same as in the hydrogen atom. The radial equation, containing as it does the generalized central potentialU(r) instead of simply the electron–nucleus Coulomb potential, requires a generalized total quantum number n analogous to the principal quantum number n for the hydrogen atom. One very important difference between the results for the general central potential problem, in which the potential no longer varies as 1/r, and the hydrogen atom problem, in which the potential varies strictly as 1/r, is the fact that electronic states characterized by different values of the orbital angular momentum quantum number  with the same total quantum number n generally correspond to different energy eigenvalues, whereas in the hydrogen-atom problem, the energy eigenfunctions for a given n but different  values are degenerate. In multi-electron atoms, states of lower -value consistent with a fixed n-value lie at a lower energy. The combined values of  and n for a given eigenfunction determine the radial nodes, these being n  1 in number. As in the hydrogen atom, n must be a positive integer, and the magnitude of the integer  cannot exceed n −1. An atomic shell is specified by a given value for n, and an atomic subshell is specified by a given set of values for both n and . Taking into account the two possible spin quantum numbers ms =±1/2 and the (2  1) values for m ,−+1,...0,1,...], one deduces the result that a given subshell contains 2(2+1) degenerate electronic states. In standard spectroscopic notation, the series of shells are denoted by K, L, M, N,....
The ground state of a many-electron atom is the one in which a sufficient number of electrons populates the orbitals of lowest energy consistent with the Pauli exclusion principle to give a neutral entity. The ground-state configuration of the electrons in an atom is specified by the number of electrons in each shell. The chemical properties of the different atoms (or elements) are determined principally by the uppermost filled energy levels, since these higher-energy electrons, being less tightly bound to the atomic core, most easily share themselves with adjacent atomic cores for the formation of chemical bonds in molecules and solids. If the uppermost occupied shell is full, there is generally an appreciable difference in energy between the occupied and next-higher unoccupied state, and the atom then tends to be chemically inert.
It is standard in spectroscopic notation to give the nvalue of a shall as a number and the -value as a lowercase letter, with =0,1,2,3,4,... being denoted, respectively, by the letters s, p,d, f, g,.... The periodic filling of successive shells as Z increases explains the use of a periodic table for listing the chemical elements. The number of electrons in a given shell generally is denoted byasuperscript.Forexample,sodiumhastwoelectronsin the 1s shell, two electrons in the 2s shell, six electrons in the 2p shell, and one electron in the 3s shell; this groundstate configuration for sodium (Z =11) would be denoted by Na: 1s22s22p63s. The rule that the maximum number of electrons in a shell be 2(2+1), with  ≤ n −1, can be consulted in conjunction with this configuration to illustrate that atomic sodium consists of two filled shells (or three filled subshells) containing the core electrons and an outermost partly filled shell containing the single valence electron.
The use of one-electron states to characterize the electronic states of the multi-electron atom is a good illustration of how physical models for complicated systems are constructed. In this section, a simple framework, supplemented by the additional requirements of the problem in question, has enabled an understanding of a much more complex problem to be developed. In the present case, the simplifying assumption is that of a spherically symmetric potential and the additional condition is that of the Pauli exclusion principle. The overall approach permits a rudimentary understanding of the entire periodic table for the chemical elements.
Section IX examines the predictions of the Schrodinger¨ equation for an electron in the presence of a periodic potential energy. The periodic potential represents another example of a simple framework used as the basis for models of a very complicated physical system. This case relies on the fact that periodicity in the potential is a common attribute of the atom array in a crystalline solid. The problem of electrons in a solid involves the population of many energy levels at one time, so the quantum statistics governing the behavior of many electrons in the same system again plays an important role. The treatment of the periodic-potential problem leads to energy band theory— an interesting and important topic, since it is so successful in explaining the difference between metals, semiconductors, and insulators.
IX. ELECTRON TRANSPORT IN SOLIDS
A. Failure of Classical Physics for Electrical Currents in Solids
Another important difficulty encountered in classical mechanics is in the area of electron transport in solids. Viewing condensed matter as merely an agglomeration of hardsphere atoms packed so closely together that they are in contact, it seems intuitively clear that any particle, however small, while moving through the agglomerate in a straight-line motion, would rebound from one or another of the atoms before traveling very far. Even allowing for the fact that the atoms in the solid usually order into a lattice configuration, there still will be very few directions through the ordered array in which a particle could travel unimpeded on the basis of this purely classical picture. Despite this, it can be deduced from experimental measurements that under conditions of very low strain, very high purity, and quite low temperatures, the conduction electrons can travel distances involving hundreds of atoms without being scattered. Devising an acceptable explanation for such easy flow of electrons in metals thus constituted a problem that could not be resolved by means of a mechanics based on a purely classical viewpoint.
Before delving into the quantum mechanical explanation of easy electron transport in metals, let us first ask how it is known that atoms in a solid are actually in contact. Next, let us ask how it is known that electrons have such long, mean-free paths in metals for which the atoms are in contact. Classical radii for atoms may be deduced in a variety of ways. Scattering experiments initiated by Rutherford in the early 1900s provided direct evidence that an atom has a tiny, dense nucleus surrounded by a cloud of electrons extending for distances of the order of angstroms(1A˚ =10−10 m).Theviscosityoffluidsandthe molecular flow of gases also provide some data on atom and molecule sizes. X-ray diffraction by crystalline solids yields lattice distances that are of the same order as the atom sizes. Compressibility data for solids lend credence to the view that forces between atoms increase as a high power of the separation distance, as might be expected from a hard-sphere picture of atoms in contact. These indications, together with a variety of other types of data, lead us to picture a solid as an array of hard-sphere atoms in contact.
The second point—namely, the existence of the long, mean-free path of electrons in metals—can be deduced from the simple picture that resistance is due to electron scattering, coupled with experimental data on the temperature-dependence of the resistivity of metals and the dependence of the resistivity on purity and crystalpreparation techniques. Perhaps the most salient point is that the resistivity decreases by many orders of magnitude when the purity of the metal is increased and the metal is grown as a strain-free single crystal.
The limiting factor on the electron mean free path in metals thus actually appears to depend upon residual imperfections,impurities,andgrainboundariesinthesample instead of on atom density. There is hardly any way a classical picture can explain the fact that the ordinary atoms that make up the ordered solid themselves provide so little resistance to electron flow. The classical picture of a pointlike electron scattering in a billiard-ball manner from a hardsphere atom fails completely.
B. Quantum Mechanics Approach
Quantum mechanics permits a rationalization of the classically unexplainable observations just described. Even neglecting the ordinary Coulomb repulsion between electrons, there remains a quantum mechanical tendency for electronstoremainseparated.Thistendencycanbetreated within the framework of what is called the Pauli exclusion principle, which states that no two electrons in a system can have the same set of quantum numbers. Practically speaking, this requires higher and higher average kinetic energies for the electrons as the electron density increases. This explains why adjacent atoms resist electron-cloud overlap, even though the electron cloud otherwise would be expected to be rather soft and easily deformed under compression, and so accounts for the hard-sphere view of atoms in a crystal lattice.
The unimpeded motion of electrons moving through a lattice of such hard-sphere atoms in a solid can be understood from the wavelike properties of the electron. Even classically, it can be shown that the collective scattering of waves from a periodic array of scattering centers differs quite dramatically from the scattering of waves from a random array of scattering centers. The difference between these two situations is that a random array leads to random phases between the scattered wavefronts whereas phase coherence between the scattered wavefronts is possibleifthescatteringcentersarelocatedinaperiodicarray. (Indeed, X-ray diffraction by crystalline solids hinges on phase coherence.) In the random-array case, movement of an incident wave through the array is grossly impeded due to the partial cancellation of wavefronts having random phase with respect to one another; in the periodic array case, propagation of the wavefront becomes quite possible.
Even in the periodic case, however, there are situations in which propagation is retarded, as when a portion of the wavefront reflected from one plane of the crystalline array is superimposed upon and has a 180◦ phase difference with respect to another portion of the wavefront reflected from a different plane of the array. Such waves interfere destructively. Propagation, on the other hand, is enabled by a constructive interference of the scattered waves in the direction of propagation.
These facts of classical wave propagation are applicable immediately to electron propagation in solids once it is admitted that electrons have a wavelike character. Thus, it can be stated that due to the wavelike properties ofelectrons,theperfectlyperiodicarrayofatomsinasolid may not scatter electrons out of their straight-line path. In this sense, the periodic array may be considered to offer no resistance whatsoever to electron motion, thereby rationalizing the long, mean free paths for electrons in single, strain-free crystals of high purity held at low temperatures.
The emergent picture is that electrical resistance is not due to the scattering of electrons by the atoms of the periodic array per se but by the departures from periodicity in the crystalline array. Such departures from periodicity are provided by impurities, vacancies, strained regions, dislocations, and grain boundaries and also by thermal fluctuations of the atom array. Increased scattering at higher temperatures due to temperature-dependent thermal fluctuations in the lattice can be shown to lead to the linear temperature-dependence of the resistivity of metals. The residual resistance at extremely low temperatures is due to scattering from the impurity atoms and structural defects. A quantum mechanical approach involving the Schrodinger equation, based as it is on the wavelike¨ behavior of particles, provides a suitable framework for rationalizing and treating these varied contributions to the electron resistivity of metals.
C. Periodic Potential for Crystalline Solids
The Schrodinger equation can be applied to describe con-¨ duction electrons in metals, each conduction electron being considered to be under the influence of a potential energy function that has the same periodicity as the lattice. An illustration of a periodic potential in one dimension is given in Fig. 9. If the lattice positions in a three-dimensional array are
	Rj = j1d1 + j2d2 + j3d3,	(320)
 
FIGURE 9 Periodic potential. [Fig. 7.8 in Quantum Mechanics for Applied Physics and Engineering by Albert Thomas Fromhold, Jr. (Academic Press, Inc., New York, 1981; Dover Publications, Inc., New York, 1991); reproduced with the permission of Academic Press, Dover Publications, and the author.]
where j1, j2, and j3 are integers and d1,d2, and d3 are elementalvectorsdenotingthebasicthreeunitsofperiodicity in a three-dimensional crystalline solid, then a satisfactory potentialenergyU(r),denotedby V(r)inthisspecialcase, has the periodicity requirement
	V(r + Rj) = V(r).	(321)
The time-independent Schrodinger equation given in¨ Eq. (169) then takes the form
h2
	V .	(322)
The next step is to utilize some mathematical function for
V(r). This can be assumed to be a simple form, such as a one-dimensional, periodic step function (the Kronig¨ – Penney model), or it may be quite complex, as when one attempts to simulate mathematically the actual potential energy that would be sensed by an electron that probes different positions within each atom and between atoms in the periodic array. One very general method that lends great insight into the general problem of the motion of an electron in a periodic solid is to express the potential energy as a type of Fourier series
	V VneiGn·r	(323)
n
with the amplitudes Vn for the various harmonics chosen so that the function V(r) reproduces any periodic potential energy of interest. For a lattice in which the basic spatial periodicity vectors d1,d2, and d3 are orthogonal, thevectorsGn turnouttobeespeciallysimpleinform.For the more general case of a nonorthogonal triad d1,d2,d3, however, it greatly facilitates the problem to define a triad b1,b2,b3, called the reciprocal lattice vectors b1 = (cell)−1d2 × d3
	b2 = (cell)−1d3 × d1	(324)
b3 = (cell)−1d1×,d2
where
	cell = d1 · (d2 × d3)	(325)
is the volume of a unit cell in the real lattice. In terms of these vectors, the vectors Gn appearing in Eq. (324) are given by
	Gn = 2π(n1b1 + n2b2 + n3b3)	(326)
where n1,n2, and n3 are integers. The symbol n is used to represent the integer triplet n1,n2,n3. The set Gn maps out a lattice of points in the same manner that the set Rj maps out a lattice, but the two lattices are generally quite different. The vectors Rj are said to map out a real or direct lattice, whereas the vectors Gn are said to map out the reciprocal lattice. The vectors Gn are referred to as reciprocal lattice vectors. The functions exp(iGn · r) can beshowntohavethepropertiesrequiredofbasisfunctions for a Fourier series representation of arbitrary functions having the lattice periodicity.
Once the periodic potential energy is defined, then the Schrodinger equation given in Eq. (322) can be solved by¨ various methods. One way leading to great insight into this problem is to assume a general form for the eigenfunctions φ by utilizing a Fourier series description with the periodicity of the entire solid—namely,
	 Bmeikm·r.	(327)
m
This leads to a coupled set of algebraic equations for the unknowncoefficients Bm thatcontaintheenergyeigenvalues.Thevectorskm canbeobtainedsimilarlytotheway the vectors Gn were constructed. The algebraic equations so derived constitute a homogeneous set. Self-consistency then requires the determinant of the coefficients of the unknowns Bm to be zero. This determinant, called the secular determinant, leads directly to an algebraic equation known as the secular equation for the energy eigenvalues . Choice of a specific eigenvalue  for solution of the set of algebraic equations containing the lattice potential energy coefficients Vn yields the eigenfunction φ corresponding to that energy. Repeating the procedure for each energy eigenvalue, in principle, will yield the complete set ofenergyeigenfunctionsforthatperiodicpotentialenergy. The energy eigenfunctions obtained for a periodic potential energy are known as Bloch functions, after Felix Bloch (1905–1983). Bloch functions have the general form
r
	,	(328)
where u ) are functions having the periodicity of the real lattice. This periodicity condition is
	u .	(329)
The vectors km are propagation-type vectors for planewave functions having wavelengths greater than the basic unit of lattice periodicity but less than the length of the crystal in the propagation direction.
A Bloch function for an electron in a solid may be likened to an individual harmonic of sound in a musical cabinet. Bloch functions can be shown to have a number of very interesting properties, such as completeness of the set, linear independence, and orthogonality.
D. Energy Bands and Energy Gaps
The picture that thereby emerges is of groups of closely spaced, allowed discrete energies that can be populated by electrons, with the groups of allowed levels being separated by energy ranges called gaps that contain no allowed energy values for conduction electrons. Each group of closely allowed discrete energies is called an energy band. Each allowed energy value within a band is characterized by a set of quantum numbers. With the additional consideration of electron spin, these are four in number. An electroninoneoftheallowedlevelscharacterizedbyspecified values of these quantum numbers travels unscattered by the atoms of the crystal lattice, the straight-line motion being allowed due to a wavelike propagation through the spatially periodic lattice potential energy. This provides the quantum mechanical explanation of the long, meanfree path for conduction electrons in metals.
As a rule, the electrons in a solid are characterized by the vector k, which denotes the propagation direction. The k-vector is the analog of the momentum for a particle in a solid. (In free space, p = hk, according to the de Broglie relationderivedinSectionV.B.)Theenergyoftheelectron state is denoted by (k). The goal of solid-state bandstructure calculations is to evaluate (k) for a specified periodic potential energy. This periodic potential may be considered to be available at the outset, although the problem is best approached from the standpoint of computing the potential self-consistently with the electron states deduced in the calculation. Since  = hω, the function (k) obtained by means of a band-structure calculation represents the dispersion relation for electrons in the solid. As recalled from Section IV.H, the dispersion relation provides the basis for determining the group velocity of the particle. Thus, from Eq. (107)
	vgroup .	(330)
h
This relation is very useful for obtaining the conduction electron velocity as a function of energy for any particular direction in the crystal. In fact, this approach must be used inlieuofthefree-spacerelationvparticle =p/m becausethe inertia of an electron in a crystal is governed by an effective mass m∗ instead of its actual mass m. The difference in value between m∗ and m is a measure of the average conduction electron interaction with the periodic potential ofthelattice.Althoughaperfectlyperiodiclatticedoesnot offer a resistance by scattering the conduction electrons, it does offer a resistance to the acceleration of the electron under an applied force (e.g., an electric field) by affecting its inertial response to the force.
In considering the population of the various energy levels, it is necessary to add in as an essential component the Pauli exclusion principle—that very soul of quantum mechanics that disallows any two electrons to occupy the same state, the state being denoted by the specification of valuesforthecompletesetofquantumnumbers,including electron spin. Once this is woven into the fabric, it must be considered how the energy eigenstates are occupied by the electrons available for conduction. Under thermal equilibrium condition at temperatures near absolute zero, the lower-energy states will certainly be occupied. The lowerenergy states in any of the energy bands represent states having low kinetic energies. Because the Pauli exclusion principle does not allow more than one conduction electron to crowd into any lower-energy state, higher-energy states will be populated to the degree required for all conduction electrons to be accommodated.
The requirement by quantum mechanics that all electrons be in different states has no analog in a classical mechanics description. Classically, therefore, there is no lower limit to the energy of the conduction electrons; in fact, in a classical description, the kinetic energy of the conduction electrons decreases to zero as the absolute temperature approaches zero. In a quantum mechanical description, the average kinetic energy of the conduction electrons in a metal decreases asymptotically to a still relatively high value as the absolute temperature approaches zero.
E. Metals
The average kinetic energy for the highest populated energy band can be estimated by invoking a “particle in a box” model of a metal holding its conduction electrons within the boundary walls, with no consideration given to the actual periodic potential energy of the lattice. This simple approach, known as the free-electron model, often yields surprisingly accurate quantitative values for a number of physical properties of metals associated with the conduction electrons. In such cases, a full solution of the Schrodinger equation for the actual periodic potential¨ may not be required.
The kinetic energy of the highest filled state in a given energybandat0Kelvin(K)isdesignatedtheFermienergy. A computation of how the average energy changes with increases in the thermodynamic temperature of the system yields the specific heat of the conduction electrons. The accurate predictions obtained by quantum mechanics for the specific heat of metals at low temperatures represents a remarkable success for the theory, that is to be sharply contrasted with the total failure on the part of the classical approach to provide an adequate quantitative estimate of this physical property of metals.
Quantum mechanics gives great insight into the scattering of conduction electrons by imperfections in a metal. The quantum nature of the scattering of conduction electrons places the restriction on the process that scattering cantakeplaceonlytovacantquantumstatesofthesystem. Thismeansthatat0K,anelasticscatteringeventcanoccur only for a conduction electron having an energy equal to the Fermi energy, because that is the only energy at which both filled and empty states simultaneously exist. The situation is not quite so restrictive at higher temperatures, where there is a statistical probability that nearby states are occupied or unoccupied over a range of energy at least kBT in width in the neighborhood of the Fermi energy F [Boltzmann constant kB =1.38×10−23 J/K; T =absolute
(Kelvin) temperature]. Nevertheless, electron scattering and, hence, the electrical resistivity are still severely restricted in metals by the requirements of the Pauli exclusion principle.
F. Insulators
After accepting the preceding reasons for the success of quantum mechanics in describing the properties of the long, mean-free path in metals, one then must feel quite puzzled when confronted with the experimental fact that some crystals—even in the limit of high purity, low temperature, and perfect periodicity—do not allow the free and easy motion of electrons. These materials are called
“electrical insulators.”
What is it about insulators that causes them to differ so drastically from metals in the ability to conduct electrons? The answer is again quantum mechanical in origin. It is hardly more abstruse than the answer to the question of the existence of the long, mean-free path in metals. The solution of the Schrodinger equation for a periodic poten-¨ tial energy in the way previously outlined yields a division of the energy scale into interspersed allowable and forbidden regions of energy. Over the allowable regions (the energy bands), very closely spaced discrete energy eigenvalues are found, but within the forbidden regions (the energy gaps), there are no such energy eigenvalues. However, this property of the energy-eigenvalue spectrum characteristic of the periodic potential is, of itself, insufficient to explain the basic nature of insulators. As in the situation for electron scattering by impurities, allowance must be made for the consequences of the all-pervading Pauli exclusion principle.
A force for directed electron motion invariably leads to the prediction of a nonzero electrical current from a purely classical viewpoint; however, it does not necessarily lead to such a consequence in quantum mechanics. The reason is that acceleration of electrons by a force leads to a change in electron momentum and, generally, to an accompanying change in the electron energy. A change in electron momentum is synonymous with a change in the quantum numbers characterizing the occupied electronic state; that is, the acceleration of an electron in quantum mechanics is described by the electron vacating the state it initially occupied as it simultaneously enters a different allowed state, which, by the requisites of the Pauli exclusion principle, must necessarily be vacant before any occupation can occur. Quantum mechanically, one views the electron as being induced to enter a succession of adjacent allowed states by electric-field-induced transitions. This view can be contrasted sharply with the classical picture of a continuous acceleration of the electron through a continuous sequence of momentum vectors. For a metal having a partly filled energy band, there indeed exists the requisite sequence of nearby unoccupied states adjacent to the filled states, so that transitions can be induced by the electric force acting on the conduction electrons.
For the specific case of electrical insulators, consider the seemingly unlikely situation that there are precisely enough conduction electrons to fill every energy state up to the start of a given energy gap. Both the scattering of the conduction electrons and the electric-field excitation of electrons to nearby empty states then are impossible at 0 K and, for all practical purposes, nearly impossible even at nonzero temperatures for which kBT is far smaller than the energy gap gap extending to the next-higher empty energy level. Although zero scattering might seem to constitute the ideal situation leading to a low (or even zero) resistivity, there nevertheless is no existing electrical current in the presently described situation, nor can there be any induced electric current. There is no existing current because, in such a situation, all electrons occupy pairs of states representing equal magnitude but oppositely directed momentum, so that there is no net charge transport. There can be no induced current because the electric force cannot change the momentum of the electrons in any of thefilledstatessincetherearenonearbyunoccupiedstates for the transitions. This is the required situation for an insulator.
In actuality, the seemingly unlikely situation of there beingexactlyenoughelectronstofillaband,withnoneleft over for the next-higher empty band, is not too unlikely. The reason for this is again a bit abstruse; in simplest terms,anenergybandisfoundtocontainoneallowedstate per atom in the solid for each degree of freedom of the electron spin. If there are two degrees of freedom for the electron spin (viz., two spin states, designated “up” and “down”), then the requirement for a filled energy band is simply that two conduction electrons be furnished by each atominthecrystal.Sincethevalenceelectronsbecomethe conduction electrons in a solid, this is not an improbable condition.
G. Semiconductors
The energy-level distribution for a solid can be quite a bit more complex than just described, since there is the possibility of overlapping energy bands (i.e., energy bands unseparated by the usual energy gap). In addition, there can be energy gaps that are quite small relative to laboratory values of kBT. It can be readily appreciated that overlapping bands promote metallic conduction or else can lead to what is known as a semimetal, whereas narrow energy gaps can lead to what is called a semiconductor. In semiconductors, an increase in temperature leads to more excitation of electrons from the highest-energy filled band acrossthegaptotheadjacentemptyband,therebyyielding electrons capable of conducting in what otherwise would be an empty band. Those electrons excited across the gap leavebehindemptystates(calledelectronholes)intheotherwise filled band. These empty states also can promote conduction in the following sense. Filled states nearby in momentum and energy to the newly provided empty states can undergo transitions to the empty states by means of electric-field excitation, all such transitions being impossible in the 0 K equilibrium situation where all states in the band are filled. In this way, two distinct carrier types are simultaneously provided—namely, electrons in an almost empty band and electron holes in an almost filled band.
The number of electrons excited across the energy gap increases nearly exponentially with increasing temperature.Totheextentthatelectrontransportincreaseswiththe number of carriers, the conductivity of the semiconductor increases almost exponentially with the temperature. A material having the properties just described is called an intrinsic semiconductor.
Thepredictionoftheexperimentallyobservedexponential increase of conductivity with increasing temperature in intrinsic semiconductors represents another triumph of quantum mechanics. In a classical description, there are no energy gaps and, hence, no parallel to predictions of an exponentially increasing conductivity due to excitation across an energy gap.
The exponential increase of conductivity with temperature in semiconductors also contrasts markedly with the temperature-dependence of the conductivity of metals. In that case, the conductivity decreases (instead of increasing) with increasing temperature. This decrease of conductivity in metals, which is more or less linear with increasing temperature, is due to the increase in the thermal vibrations of the atoms of the lattice at higher temperatures. Thermal vibrations yield greater departures of the atom array from perfact periodicity, thereby leading to more random scattering of the electrons and a consequent decrease in the electron current.
The exponential increase in conductivity with temperature described for excitation of electrons across an energy gap in an intrinsic semiconductor is paralleled in another type of solid, called an extrinsic semiconductor. In extrinsic semiconductors, however, there is no band-to-band excitation. Instead, the source of electrons for the empty band is a doping concentration of impurities that have outer electrons at energies just below the empty band (socalled donor impurities, or simply donors) or, alternately, empty levels at energies just above the filled band (socalledacceptorimpurities,orsimplyacceptors).Semiconduction then takes place by means of electrons donated to theemptybandbydonorimpuritiesor,alternately,byelectron holes created in the filled band as a result of electrons accepted from that band by the acceptor impurities.
H. Superconductors
It is another well-known experimental fact that a number of metals go into a state of zero resistance at very low temperatures, below the so-called transition temperature characteristic of the material in question. The concept of energy gaps likewise turns out to play an important role in understanding this incredible phenomenon, although in a different way from that just described for semiconductors. Theenergygapinthecaseofsuperconductorsisattributed to a condensation of the electrons carrying the charge into so-called Cooper pairs, the binding energy of the pairs being attributed to indirect Coulomb-force-induced interaction between electrons as mediated by the intervening ion cores on the lattice sites in the metal.
Let us consider, for example, pairs of electrons passing one another while traveling in opposite directions through the lattice of ion cores surrounded by the attendant electron clouds. One electron exerts a force on the nearby ionic lattice, which responds to that force. The resulting disturbance in the periodic potential sensed by the second electron of the pair can lead to an effective lowering in the totalenergyrelativetothesituationofarigid,nonresponding lattice. The energy lowering is the greatest for pairs of electrons having equal magnitudes but oppositely directed momentum values, so Cooper pairs are characterized by twoelectronshavingthisproperty.Theloweringofenergy leads to a superconducting energy gap. The energy gap so produced is quite small, so that very low temperatures are usually required for the pairs to remain unbroken by thermal fluctuations. The temperature range of superconductivity has been greatly extended, however, by the discovery of the so-called “high temperature superconductors” initiated with a series of compounds based on a copper oxide matrix.
As the temperature is reduced through the superconducting transition, one speaks of the condensation of the electron system into the paired state. It is evident that electrons with oppositely directed momentum values will become separated spatially in a short time, so the pairing process must be statistical in nature. Pairs must continually exchange partners (as required, e.g., in some forms of folk dancing).
The dance of the conduction electrons, while maintaining this property of electron pairing, is a many-body problem of some complexity. The wavefunction for the entire system of electrons as a unit must be considered, not merely the single-particle wavefunctions individually. The establishment of a net electric current requires a suitable modification in the zero-current wavefunction for the system.
The importance of electron pairing for electrical resistance is that the scattering of conduction electrons in the pairedstatewillbeineffectiveinrandomizingthenetelectron momentum. Thus, there can be a zero resistivity state as long as Cooper pairs exist in the system.
Thermal fluctuations can break Cooper pairs to yield electrons in the normal state. The breaking of electron pairs by this means is tantamount to an excitation across the energy gap. In contrast to the case of semiconductors, the excitation across the energy gap in the present instance leads to an increase in the resistivity. Raising the temperature of a superconductor through the superconducting transition temperature means that the thermal fluctuations become so large that essentially no Cooper pairs remain in the metal to provide superconductivity.
I. Success of Quantum Mechanics for Electron Transport in Solids
Thus, quantum mechanics provides a framework for understanding the widely different electrical-conduction properties of superconductors, normal metals, semiconductors, and insulators. This remarkable success, coupled with the parallel failures of classical physics to lend understanding to these areas, has led to the nearly universal acceptance of quantum mechanics for most calculations in solid-state physics.
X. SUMMARY
The theory of quantum mechanics evolved in the 1920s to correlateandpredictthebehaviorofatomicandsubatomic systems. Heisenberg and Schrodinger played prominent¨ roles in the development of this theory, which proves to be the only formulation adequate for the microscopic domain of nature. Heisenberg stressed the importance of including physical observables and experimental observations of optical spectral lines in his formulation. Schrodinger¨ based his work on a differential equation for the wavelike behavior of small mass particles that includes the possibility of constructive and destructive interference of waves presumably associated with the presence of a particle. Inherent in quantum mechanics is the germ concept that accurate predictions of future trajectories of particles and the time evolution of a system involving one or more particles are at best statistical, involving a range of possibilities specified exactly only in terms of precise values for the relative probabilities. This precludes the deterministic prediction of an exactly specified future path, regardless of how accurately the initial conditions of the system are specified. Also inherent in the theory is the impossibility of exactly measuring even the initial conditions, such as initial position and initial linear momentum, due to some inherent uncertainty in the value of one of these variables following determinations of the values of the other variables to some specified degree of precision. The philosophical implications of an inherent uncertainty in quantum mechanical predictions, contrasted with the absolute determinism inherent in classical mechanical predictions, initially led many (including Einstein) to doubt whether the discipline had any fundamental merit beyond that of being an elegant and elaborate computationtoolforobtainingpredictionsofastatisticalnature.To date, no better theory for the microscopic world has been developed.
SEE ALSO THE FOLLOWING ARTICLES
BONDING AND STRUCTURE IN SOLIDS • CELESTIAL MECHANICS • ELECTRODYNAMICS, QUANTUM • ELECTROMAGNETICS • LASERS • MECHANICS, CLASSICAL •
PARTICLE PHYSICS, ELEMENTARY • QUANTUM CHEM-
ISTRY • QUANTUM OPTICS • RELATIVITY, GENERAL • RELATIVITY, SPECIAL • STATISTICAL MECHANICS
BIBLIOGRAPHY
Bohm, D. (1951). “Quantum Theory,” Prentice-Hall, Englewood Cliffs, NJ.
Born, M. (1969), “Physics in My Generation,” Springer-Verlag, New York. de Broglie, L. (1939). “Matter and Light,” Dover Publications, New York.
Fromhold, A. T., Jr. (1981, 1991). “Quantum Mechanics for Applied Physics and Engineering,” Academic Press, New York; Dover Publications, New York.
Heisenberg,W.(1930).“PhysicalPrinciplesofQuantumTheory,”Dover Publications, New York.
Ikenberry, E. (1962). “Quantum Mechanics for Mathematicians and Physicists,” Oxford University Press, New York.
Mandl, F. (1957). “Quantum Mechanics,” Butterworths Scientific Publications, Stoneham, MA.
Pauli, W. (1973). “Wave Mechanics,” Pauli Lectures on Physics, Vol. 5. MIT Press, Cambridge, MA.
Pauling, L., and Wilson, E. B., Jr. (1935). “Introduction to Quantum Mechanics,” McGraw-Hill, New York.
 
 
Quantum Optics
J. H. Eberly
University of Rochester	P. W. Milonni
Los Alamos National Laboratory
 
I.	Introduction
II.	Induced Atomic Coherence Effects
III.	Radiation Coherence and Statistics
IV.	Quantum Interactions and Correlations
V.	Recent Developments
GLOSSARY
AC Stark effect Effective increase of the Bohr transition frequency of a two-level atom which is being excited by a strong laser beam, the amount of increase being the Rabi frequency.
Blochvector Fictitious vector whose rotations are equivalent to the time dependence of the wave function or quantum mechanical density matrix associated with a two-level atom.
Coherencetime Limiting time interval between two segments of a light beam beyond which the superposition of the segments will no longer lead to interference fringes.
Coherentstate Quantizedstateofalightfieldwhosefluctuation properties are Poissonian; it is considered the most classical quantized field state.
Degree of coherence Normalized measure of the ability of a light beam to form interference fringes.
Optical bistability Existence of two stable output intensities for a given input intensity of a steady light beam transmitted through a nonlinear optical material.
Optical Bloch equations Dynamical equations that determine the motion of the Bloch vector; they are a special type of quantum Liouville equation.
Photonecho Burstoflightemittedbyacollectionoftwolevel atoms signaling the realignment of their Bloch vectors after initial dephasing; similar to the spin echo of nuclear magnetic resonance.
Rabi frequency Steady frequency of rotation of the Bloch vector of an atom exposed to a constant laser beam, proportional to the atom’s transition dipole moment and the laser’s electric field strength.
Superradiance Spontaneous emission from many atoms exhibiting collective phase-coherence properties, such as radiation intensity proportional to the square of the number of participating atoms.
Two-level atom Fictitious atom having only two energy levels which is used as a model in theoretical studies of near-resonance interactions of atoms and light, particularly laser light.
 	409
QUANTUM OPTICS is the study of the statistical and dynamical aspects of the interaction of matter and light. It is concerned with phenomena ranging from spontaneous emission and single photon absorption to the highly nonlinear processes induced by laser fields and has connections with laser physics, nonlinear optics, quantum electronics, quantum statistics, and quantum electrodynamics.
I. INTRODUCTION
A. Central Issues of Quantum Optics
Planck’squantum,announcedtothePrussianAcademyon October 19, 1900, as a solution to the blackbody puzzle reopened the wave–particle question in optics, a question that Fresnel and Young had settled in favor of waves almost two centuries earlier. Planck’s quantum could not be confinedtolightfields.Withinthreedecades,allofparticle mechanics had been quantized and rewritten in wave mechanical form, and wave–particle duality was understood to be both universal and probabilistic.
Quantum optics is fundamentally concerned with coherenceandinterferenceofbothphotonsandatomicprobability amplitudes. For example, it provides one of the main avenues at the present time for detailed study of wave–particle duality. The central issues of quantum optics deal with light itself, with quantum mechanical states of matter excited by light, and with the process of interaction of light and matter.
Questionsarisinginthedescriptionofasingleatomand itsassociatedradiationfield,astheatommakesatransition between two energy states and either emits or absorbs a photon, are among the most central questions in quantum optics. Observations of individual optical emission and absorption events are possible, and the interpretation of such observations is at the heart of quantum theory.
Various elements of these central considerations are to a degree independent of each other and are understood separately. Among these are (1) the probability that an atomic electron occupies one or another state and the rate at which these occupation probabilities change, (2) the statistical nature of the photons emitted during transitions, (3) correlations between atom and photon states, (4) the characteristic parameters that control the light–matter interaction, and (5) the intrinsically quantum mechanical features of the atom’s response to the radiation.
Quantum optics also concerns itself with problems that grow out of these central considerations and whose answers can be expressed within the conceptual framework established by the central problem. Areas related in this way to the core of quantum optics deal, for example, with correlated many-atom light–matter interactions; near-resonant transitions among three and more states of anatomormoleculeorsolid;opticaltestsofquantumelectrodynamics and measurement theory; multiphoton processes; quantum limits to noise and linewidth; quantum theory of light amplification and laser action; and manifestations of nonlinearity, bistability, and chaos in optical contexts. A wide variety of quantum optical phenomena that bear on one or another of these issues are now known and widely studied.
B. The A and B Coefficients of Einstein
The second half of the twentieth century saw remarkable advances in our understanding of light, of its generation, propagation, and detection. The laser is one manifestation of these advances. Lasers generally depend on the quantum mechanical properties of atoms, molecules, and solidsbecausequantumpropertiesdeterminethewaysthat matter absorbs light and emits light. Conversely, the propertiesoflaserbeamshavemadeopticalstudiesofquantum mechanics possible in a variety of new ways. It is this interplay that has created the field of quantum optics since about 1960.
From a different historical perspective, however, quantum optics is much older than the laser and even older than quantum mechanics. The quantum concept first entered physics in 1900 when Planck invented the light quantum to help understand black body radiation. The understanding of other quantum optical phenomena, such as the photoelectric effect, first explained by Einstein in 1905, was well underway almost two decades before a quantum theory of mechanics was properly formulated in 1925 and 1926 by Heisenberg and Schrodinger. Indeed, these early¨ developments in quantum optics played an essential role in the first quantum pictures of atomic matter given by Bohr and others in the period from 1913 to 1923.
Only two parameters are needed to understand the interaction of light with atomic (and molecular) matter, accordingtoEinstein.Thesetwoparametersarecalled Aand B coefficients. These coefficients are important because they control the rates of photon emission and absorption processes in atoms, as follows. Let the probability that a given atom is in its nth energy level be written Pn. Suppose there are photons present in the form of radiation with spectral energy density (J/m3 Hz) denoted by u(ω). Then the rate at which the probability Pn changes is due to three fundamental processes:
(dPn/dt)absorption of light = +Bu(ω)Pm	(1a)
(dPn/dt)spontaneous emission of light = −APn	(1b)
(dPn/dt)stimulated emission of light = −Bu(ω)Pn.	(1c)
Here Pm is the probability that the atom is in a lower level, the mth, which is related to the nth through the energy relation En − Em =hω, where h =h/2π and h is Planck’s famous quantum constant. Einstein’s great insight was to include stimulated emission [Eq. (1c)] among the three elementary processes, in effect, to recognize that an atom in an upper energy state could be encouraged by the presence of photons [the existence of u(ω)] to hasten the rate at which it would drop down to a lower state.
The three contributions to the rate of change of Pn shown in Eqs. (1a–c) can be added to make an overall single equation for the total rate of change of Pn:
	dPn/dt = +Bu(ω)Pm − APn − Bu(ω)Pn.	(2a)
Einstein applied this equation to an examination of blackbody light. He showed that the steady-state solution
	Pm/Pn = 1 + A/Bu(ω)	(2b)
implies the validity of Planck’s formula for u(ω):
	hω3	1
u(ω, T) =  { } − , (3) π2c3 exp hω/kT 1
and the value of the prefactor is just the ratio A/B:
A	hω3
	,	(4)
B	= π2c3
where k is Boltzmann’s constant and T the temperature in degrees Kelvin. Table I contains the values of physical constants used in evaluating various radiation formulas. For typical optical radiation, the value of the fundamental ratio A/B is approximately 10−14 J/m3 Hz. The corresponding intensity, namely cA/B, is approximately 3×10−6 J/m2, or 6π ×10−6 W/m2 per Hz of bandwidth.
The value of the spectral intensity of thermal radiation is usually many orders of magnitude lower than this because of the second factor in Eq. (3). At optical wavelengths, the second factor is much smaller than one for all temperatures less than about 5000 K.
After the development of a fully quantum mechanical theory of light by Dirac in 1927, it was possible to give expressions for A and B separately:
A	 	(5)
B	 .	(6)
TABLE I Physical Constants Used in Evaluating Radiation Formulas
Constant	Value
h (Planck’s constant) k (Boltzmann’s constant) c (Speed of light) e (Electric charge) λ (Typical optical wavelength, yellow) ν (Typical optical frequency)	6.6×10−34 J/s
1.38×10−23 J/K
3×108 m/s
1.6×10−19 C
600×10−9 m
5×1014 Hz
In these formulas we have separated the factor 1/4πε0 = 8.9874×109 N m2/C2 to display A and B in atomic units as well as SI units, and D denotes the quantum mechanical “dipole matrix element” associated with the m →n transition under consideration.
The values of these important coefficients can be obtained for transitions of interest in quantum optics by assuming that the dipole matrix element is approximately equal to the product of the electron’s charge and a “typical” electron displacement from the nucleus. Thus, we take ω= 2πν and e and h from Table I and D = er, with r equal to about 1 to 3 A (1˚ –3×10−10 m). In this case the values are A ≈108 s−1 and B ≈1022 m2/J s2, respectively.
The advantage of Einstein’s approach, and the reason it still provides one basis for understanding light–matter interactions,isthatitbreakstheinteractionprocessintoits separate elements, as identified above in Eqs. (1a–c). To repeat this important identification, these processes are (a) absorption, (b) spontaneous emission, and (c) stimulated emission.
However, it must be pointed out that Einstein’s formulas are not universally valid, and Eqs. (1) and (2) can be seriously misleading in some cases, particularly for laser light. Laser light typically has a very high spectral energy densityu(ω).Inthiscasedifferentformulasandequations, and even entirely different concepts with their origins in wave mechanics, may be required.
A large body of experimental evidence has accumulated since 1960 showing that many aspects of the interaction between light and matter depend on electric radiation field strength E directly, not only on energy density u ≈ E2. Just those aspects of the light–matter interaction thatdependdirectlyon E alsodependdirectlyonquantum mechanical state amplitudes ψ, not only on their associated probabilities |ψ|2. Issues of coherence and interference of both radiation fields and probability amplitudes are fundamental to these studies. It is principally the experiments and theories that deal with light and matter in this domain that make up the field of quantum optics.
C. Two-State Atom and Maxwell–Bloch Equations
As Einstein’s arguments suggest, in quantum optics it is often sufficient to focus attention on just two energy levels of an atom—the two levels that are closest to resonance with the radiation, satisfying the energy condition
E2 − E1 ≈ hω,
where ω= 2πν is the angular frequency of the radiation field. This is shown schematically in Fig. 1.
 
FIGURE 1 Schematic energy level diagram showing a two-level subsystem.
Under these circumstances the wave function of the atom is a sum of the wave functions for the two states
	ψ(r,t) = C1φ1(r) + C2φ2(r).	(7a)
For simplicity of description we will assume each level corresponds to a single quantum state and will usually use “level” and “state” synonymously.
The assumption that the electron is certainly in one or the other or a combination of these two levels is expressed mathematically by the equality
	|C1|2 + |C2|2 = 1.	(7b)
Each term in this equation is called a level probability, and all probabilities must add to 1, of course. These probabilities are the quantities labeled by the letter P in the Einstein equations. The C’s themselves are not probabilities, and they have no counterpart in classical probability theory. They are called probability amplitudes. It is the remarkable nature of quantum mechanics that the fundamental equation (the Schrodinger equation) governs these¨ amplitudes C, not the probabilities |C|2.
The Schrodinger equation for either one of the ampli-¨ tudes is
ih dCm/dt = EmCm + VmnCn, (8) wherem andn takeeitherthevalue1or2,butm = n.Here h is the usual abbreviation for h/2π, and Vmn is called the interaction matrix element between the atom and the radiation field. In almost all cases of interest in quantum optics, this interaction comes from the potential energy −d·E(r, t) of the atomic dipole in the electric radiation field (a dipole d=er exists because of the separation of the negative electronic charge in its planetary orbit from the position of the positively charged nucleus.
In principle E is a quantum operator field (see Section III.C).Theso-calledsemiclassicaltheoryofradiationuses its average (or “expectation”) value instead. This approximation is usually justified when the field is intense, because quantum fluctuations, which almost always occur at the single-photon level, are then negligible. In this section we describe the semiclassical theory and ignore quantum field effects entirely.
The dipole interaction is distributed over the atomic orbitals involved, with the result that
Vmn 
	 (rN,t)]φn(r)	(9a)
= −dmn · eˆE(rN,t).
In Eq. (9a) we have written
E(r,t) = eˆE(r,t) ≈ eˆE(rN,t),
where eˆ is the polarization and E(rN,t) is the amplitude of the electric field at the position of the atom (i.e., of the nucleus) rN instead of at the position of the electron. This approximation is usually well justified because the electron’s orbit, and thus the range of the integral, extends mainly over a region much smaller than an optical wavelength. Thus, over the whole range of the integral E(r,t)≈ E(rN,t) and the only r dependence comes from the dipole moment er itself. This is called the dipole approximation. The integral in Eq. (9a) is called the dipole matrix element, d,
	d = eˆ · dmn  .	(9b)
If only one atom is under consideration it is common to put it at the origin of coordinates and write E(0,t) or simply E(t). If several or many atoms are under consideration this is generally not possible [see, e.g., Eq. (20)]. Equation (8) can be written in a simpler form by anticipating an interaction with a quasi-monochromatic radiation
field
	E .	(10)
that is nearly resonant with the atom, where c.c. means complex conjugate. This means that the angular frequency ω=2πν of the radiation field is approximately equal to the angular transition frequency of the atom: ω21 =(E2 − E1)/h. In this case there is a strong synchronous response of the atom to the radiation, and the equations simplify if one removes the synchronously “driven” component of the atomic response by defining new variables an:
a1 = C1	(11a) a2 = C2eiωt.	(11b)
Note that |a1|2 +|a2|2 =|C1|2 +|C2|2 =1; thus, the a’s are also probability amplitudes.
If E(t) is sufficiently monochromatic (the field amplitude, i.e., 0 is practically constant in time; which means  ), then a rotating wave approximation (RWA) is valid if the anticipated atom field resonance is sufficiently sharp, that is, if  . The most important consequence of the RWA is that factors such as 1+e±2iωt,whichappearintheexactequationsforthenew amplitudes a1 and a2, may be replaced by 1 to an excellent approximation.Theresultisthatthefrequenciesω21 andω individually play no further role in the Schrodinger equa-¨ tion, and Eq. (8) takes the extremely compact RWA form:
i da  (12a) i da , (12b)
where	
  = ω21 − ω	(12c)
is called the detuning of the atomic transition frequency from the radiation frequency, and
	 	(12d)
is called the Rabi frequency of the interaction. For simplicity, the Rabi frequency χ will be assumed here to be a real number.
For a strictly monochromatic field (time-independent 0) the solution to Eqs. (12a and b) is easily found in terms of  , where  is called the generalized or detuning-dependent Rabi frequency. In the most important single case the atom is in the lower state at the time the interaction begins, which means that a1(0)=1 and a2(0)=0. In this case the solution is
a (i /)sin 
	a2(t) = i[(χ/)sin 	(13b)
and the corresponding probabilities are
	P ( /)2 sin2(t/2)	(14a)
	P2 = (χ/) .	(14b)
These solutions describe continuing oscillation of twolevel probability between levels 1 and 2. They have no steady state. Figure 2 shows graphs of P2(t). One already sees, therefore, that the quantum amplitude equations [Eqs. (12a–d)] make strikingly different predictions fromthetwo-levelequationsofEinstein[recallthesteadystate solution Eq. (2b)].
Within the RWA, the dynamics remain unitary or probability conserving: P1 + P2 =1 for all values of t. As a result, the compact version [Eq. (12)] of Schrodinger¨ ’s equation remains valid even for very strong interactions between the atom and the radiation. This is important when considering the effects on atoms of very intense laser fields. The limits of validity of Eq. (12) are deter-
 
FIGURE 2 Rabi oscillations for different values of  /x .
mined to a large extent by a generalized statement of the limits of the RWA:
	ω21 and  .	(15)
There are two other real quantities associated with the amplitudes a1 and a2 of the radiation–atom interaction. They belong to the atomic dipole’s expectation value  which, according to Eqs. (7a), (9b), and (11), is
	 |	.	(16)
The new quantities are designated by u and v:
u  (17a) v . (17b)
Along with u and v, a third variable, the atomic inversion w = P2 − P1 plays an important role. The solutions for u,v, and w corresponding to Eqs. (13) and (14) above are
u	= ( χ/ )	(18a)
v	= (χ/)sint	(18b)
w	 ,	(18c)
which share the oscillatory properties of the probabilities. They also obey the important conservation law:
	u2 + v2 + w2 = 1,	(18d)
which is the same as |a1|2 + |a2|2 = 1.
For many purposes in quantum optics the semiclassical dipole variables u and v, and the atomic inversion w, are the primary atomic variables. They obey equations which are equivalent to Eq. (8) and take the place of Schrodinger¨ ’s equation for the level’s probability amplitudes a1 and a2 (or C1 and C2):
du/dt = − v (19a) dv/dt  χw (19b)
	dw/dt = −χv.	(19c)
All of these considerations assume that the field is monochromatic or nearly so.
Although the field E(r, t) is not considered an operator in the semiclassical formulation, it can still have a dynamical character, which means it is not prescribed in advance, but obeys its own equation of motion. It is naturally taken to obey the Maxwell wave equation, with the usual source term µ0d2/dt2P(z,t). In the semiclassical theory P , where N is the density of two-level atomsinthesourcevolumeand theaveragedipolemoment of a single atom, already calculated in Eq. (16).
As Eq. (16) indicates, is quasi-monochromatic, essentially because a two-level atom is characterized by a single transition frequency. Therefore the E that it generates may also be regarded as monochromatic or nearly so, as Eq. (10) assumed. This internal consistency is an important consideration in the semiclassical theory. In many cases it is also suitable to regard the field as having a definite direction of propagation, say z, and to neglect its dependence on x and y (plane wave approximation):
	E .c.,	(20)
where k =ω/c and the amplitude or envelope function (z,t) is a complex generalization of 0(t) in Eq. (10). It obeys a “reduced” wave equation in variables z and t:
 Ndω/ 
ThereducedwaveequationEq.(21)andEqs.(19)foru,v, andw arecalledthesemiclassicalcoupledMaxwell–Bloch equations.
Inspection of the semiclassical Eqs. (19) and (21) reveals their major flaw. One easily sees that the semiclassical approach to radiation theory does not include the process of spontaneous emission. A completely excited atom will not emit a photon in this theory. That is, if the atom is in its excited state, then a2 =1 and a1 =0, so w =1 and u =v =0. Thus, according to Eq. (21) no field can be generated. By the same token, if =0 then χ =0 and dw/dt =0, and no evolution toward the ground state can occur. The flaw in the semiclassical Maxwell–Bloch approacharisesfromtheassumptionthatallofthedynamics can be reduced to a consideration of average values, that is, averages of dipole moment and inversion and field strength. In reality, fluctuations about average values are an important ingredient of quantum theory and essential for spontaneous emission.
Spontaneous emission does not play a dominant role in many quantum optical processes, particularly those involving strong radiation fields. The semiclassical Maxwell–Blochequationsgiveanentirelysatisfactoryexplanation of these effects, and the next sections describe some of them.
In nature there are no actual two-level atoms, of course. However, the selection rules for allowed optical dipole transitions are sufficiently restrictive, and optical resonances can be sufficiently sharp that very good approximations to two-level atoms can be found in nature. A good example is found in a pair of levels in atomic sodium, and they have been used in quantum optical experiments.
In sodium the nucleus has spin I =3/2, and the lowest electronic energy level is 3S1/2 with hyperfine splitting (F = 1and F =2).Thefirstexcitedlevels3P1/2 and3P3/2 are responsible for the well-known strong sodium D lines of Fraunhofer in the yellow region of the optical spectrum at wavelengths 589.0 nm and 589.6 nm. The “two-level” transition is between the mF =+2 magnetic sublevel of F =2 of the ground state and the mF =+3 magnetic sublevel of F =3 in the 3P3/2 excited state. Circularly polarized dye laser light can be tuned within the 15-MHz natural linewidth of the upper level, and the  m =+1 selection rule for circular polarization prevents excitation of the other magnetic sublevels.
Spontaneous decay from the upper state, which obeys no resonance condition, is also restricted in this example. The final state of spontaneous decay could, in principle, have mF =4, 3, 2. However, in sodium there are no mF =4 or 3 states below the 3P3/2 state, and only one mF =2 state, namely the one from which the excitation process began. Thus, the state of the sodium atom is very effectively constrained to this two-state subset out of the infinitely many quantum states of the atom.
II. INDUCED ATOMIC COHERENCE EFFECTS
The ability of an atomic system to have a coherent dipole moment during an extended interaction with a radiation field is a necessary condition for a wide variety of effects associated with quantum optical resonance. The dipole moment should be coherent in the sense that it retains a stable phase relationship with the radiation field. Longterm phase memory may be difficult to achieve, for example, because spontaneous emission and collisions destroy phasememoryataratethatistypicallyintherange108 s−1 or much greater. Coherence is also lost if the radiation bandwidth is too broad. The importance of dipole coherence effects shows that light–matter interactions do depend most fundamentally on the dipole moment and electric field strength, not on radiation intensity and the B coefficient.
A. p Pulses and Pulse Area
The solution for the level probabilities given in Eq. (14) is the single most important example in quantum optics of the coherent response of an atom to a monochromatic radiation field. “Coherence” in this context has several connected meanings, all associated with the well-phased steady oscillation of the probabilities considered as a function of time. This time dependence was shown in
Fig. 2 for several values of the parameters   and χ. The significance of the Rabi frequency χ is clear—it is the frequency at which the inversion oscillates when the atom andtheradiationareatexactresonance,when =0,since
	w(t) = −cosχt.	(22)
Fruitful connections to the spin vector formalism of magnetic resonance physics are obtained by regarding the triplet [u,v,w] as a vector S. Equations (19) for u,v, and w can then be written in compact vector form:
	dS/dt = Q×S,	(23)
where Q is the vector of length  with components [−χ, ]. The vector Q can be called the torque vector for S, which is variously called the pseudo-spin vector, the atomic coherence vector, and the optical Bloch vector. This vector formulation in Eq. (23) of Eqs. (19) shows that the evolution of the two-level atom in the presence of radiation is simply a rotation in a three-dimensional space. The space is only mathematical in quantum optics becausethecomponentsoftheopticalBlochvectorarenot thecomponentsofasinglerealphysicalvector,whereasin magneticresonancetheyarethecomponentsofarealmagnetic moment. In both cases the nature of the torque equation leads to a useful conservation law: d/dt(S·S)=0. That is, the length of the Bloch vector is constant. In the u,v,w notation this means u2 +v2 +w2 =1, and it implies that the vector [u,v,w] traces out a path on a unit sphere as the two-level atom changes its quantum state.
Furtherconsiderationoftheon-resonantatoms(  → 0 and  → χ) gives information about the interaction of atoms with (nonmonochromatic) pulsed fields. According to Eq. (19a) u(t) can be neglected if  =0 and a new form of solutions to Eqs. (19b and c) follows immediately:
v(t) = −sinφ(t)	(24a) w(t) = −cosφ(t),	(24b)
where φ(t) is called the “area” of the electric field because it is related to the time integral of the electric field envelope:
t
	 .	(25)
In the monochromatic limit when 0 =constant, then φ(t) → χt.
Recallthattherotatingwaveapproximation(RWA)will not permit 0 to vary too rapidly. If τp is the pulse length, then 0 is not too rapidly varying if τp is long enough, namely if 1/τp  . Pulse lengths in the range 1 ns ≥ τp ≥10 fs are of interest and are compatible with the RWA [1 fs (femtosecond)=10−15 s].
The significance of φ(t) is evident in Eq. (24). The term φ is just the angle of rotation of the on-resonance Bloch vector S=[u,v,w] during the passage of the light pulse. A light pulse with φ =π is called a π pulse, that is, a pulse that rotates the initial vector [0, 0, −1], which points down, through 180◦ to the final vector [0, 0, +1], which points up. Thus, a π pulse completely inverts the atomic probability, taking the atom from the ground state to the excited state. A 2π pulse is one that returns the atom via a 360◦ rotation of its Bloch vector to its initial state, after passingthroughtheexcitedstate.Theremarkablenatureof this rotation is not so much that an inversion of the atomic stateispossible,butthatitcanbedonefullycoherentlyand without regard for the pulse shape. Only the total integral of 0(t) is significant.
The physics behind Bloch vector rotation is essentially the same in magnetic resonance, but perhaps less remarkable since the Bloch vector in that case is a physically “real” magnetic moment. In optical resonance there is no “real” electric moment vector whose Cartesian components can be identified with [u,v,w]. Early evidence of the response of the optical Bloch vector to coherent pulses was obtained in experiments of Tang, Gibbs, Slusher, Brewer, and others (see Sections II.B and II.C), and further experiments probing these properties continue to be of interest.
B. Photon Echoes
Photon echoes are an example of spontaneous recovery of a physical property that has been dephased after many relaxation times have elapsed. In the case of echoes the physicalpropertyisthemacroscopicpolarizationofasampleoftwo-levelatoms.Recoveryofthepolarizationmeans recovery of the ability to emit radiation, and the signature of a photon echo is the appearance of a burst of radiation from a long-quiescent sample of atoms. The burst occurs at a precisely predictable time, not randomly, and is due to a hidden long-term memory. The echo principle was discovered and spin echoes were observed by Hahn in 1950 in magnetic resonance experiments. Photon echoes were first observed by Hartmann and co-workers in 1965.
Photon echoes are possible when a sample of atoms is characterized by a broad distribution g( ) of detunings. This may occur in a gas, for example, because of Doppler broadening or in a solid because of crystalline inhomogeneities. For the latter reason it is said that g( ) indicates the presence of inhomogeneous broadening. The Maxwellian distribution of velocities in a gas is equivalent to a Maxwellian distribution of detunings since each atom’s Doppler shift is proportional to its velocity. If the number of atoms in the sample is N, then the fraction with detuning   is given by Ng( )d , where g	 √
(2π)δωD
Here  ¯ is the average detuning and δωD is the Doppler linewidth, δωD =ωL(kT/mc2)1/2.
The Bloch vector picture is well suited for describing photon echoes. Assume that the Bloch vectors for a collection of N atoms all lie in the equatorial (u −v) plane of the unit sphere along the negative v axis, that is, S=[0,−1,0]. This arrangement can be accomplished byexcitationfromthegroundstate[0,0,−1]withastrong π/2 pulse for which Q χ,0,0] if χ  . The total Bloch vector is then SN =[U, V, W]=[0,−N,0], which corresponds to a macroscopic dipole moment of magnitude Nd. After this excitation pulse the sample begins to radiate coherently at a rate appropriate to the dipole moment Nd. However, following the excitation pulse we again have χ =0 and Q=
[0,0, ], and according to Eq. (23) the individual Bloch vectors immediately begin to process freely about the w axis(intheu −v plane)atratesdependingontheirindividual detunings  . Specifically, (u −iv)t =(u −iv)0e−i t for an atom with detuning  , if χ =0.
As a consequence, the total Bloch vector will rapidly shrink to zero in a time δt ≈1/δω, where δω is the spread in angular velocities in the N atom collection. That is, the coherent sum of N dipoles rapidly dephases and [0, N,0]→[0,0,0], with the result that the sample quickly stops radiating. This is called free precession decay, or free induction decay after the similar effect in magnetic resonance, because the decay is due only to the fact that the individual dipole components u −iv get out of phase with each other due to their different precession speeds, not because any individual dipole moment is decaying.
If the distribution of  ’s is determined by the Doppler effect, as in Eq. (26), then since (u −iv)0 =i, one finds
U  d  g i t
	 .	(27)
The decay is very rapid if the Doppler width is large. Typically δωD ≈109 to 1010 s−1, thus, within a few tenths of a nanosecond U −iV →0 and radiation ceases.
The echo method consists of applying a second pulse to the collection of atoms after U and V have vanished, that is, at some time T . Each single atom with its detuning  , after the time interval T, still has (u −iv)T =ie−i T . Only the sum of these u and v values is zero due to their different   values. The torque vector describing the second pulse is Q , which can again be approximated by [−χ,  . The effect of the second pulse is again to rotate the Bloch vectors about the u axis. The ideal second pulse is a π pulse, in which case u →u,v → −v and w →−w, that is, a rotation by 180◦. Thus, for times t ≥ T after the π pulse the u −v components are
T)
,
where T fies the rotated coherence vector immediately following the π pulse at time T:
 iei T .
The remarkable feature of a π pulse is that it accomplishesaneffectivereversaloftime.FollowingittheBloch vectors do not continue to dephase, but begin to rephase:
(u − iv)t = −iei T e T)
	 .	(28)
Thus,attheexacttimet =2T,theindividualu’sandv’sall rephase perfectly: [u,v,w]=[0,1,0]. Their Bloch vectors are merely rotated 180◦ from their positions after the original π/2 pulse, and they again constitute a macroscopic dipole moment SN =[0, N,0], and therefore the collection will begin to radiate again.
Because of the timing of this radiation burst, exactly as long (T) after the π pulse as the π pulse was after the original π/2 pulse, it is natural to call the signal a photon echo. Because of the separation by the intervals T and 2T from the π and π/2 excitation pulses, the observation of an echo can be in practice an observation that is very noisefree.Followingtheechopulse,thecoherencevectors again immediately begin to dephase, but they can again be rephasedusingthesamemethod,andasequenceofechoes can be arranged.
Because of collisions with other atoms, the individual u and v values will actually get smaller during the course of an echo experiment, independent of their   values. Thus, the rephased Bloch vector is not quite as large as the original one. One of the possible uses of an echo experiment is to measure the rate of collisional decay of u and v, say as a function of gas pressure, by measuring the echo intensity in a sequence of experiments with different values of T since the echo intensities will get smaller as collisions reduce the length of the rephased Bloch vector. The way in which Eq. (23) is rewritten to account for collisions is taken up in Section II.D.
C. Self-Induced Transparency and Short Pulse Propagation
The polarization of a dielectric medium of two-level atoms,suchasanyatomicvaporexcitedneartoresonance, is linearly related to the incident electric field strength 0 at low-light intensities but becomes nonlinear in the strong-field, short-pulse regime. This is most evident in Eq. (18), where the sine and cosine functions contain all powersof .Thesenonlinearitieshavestriking consequences for optical pulse propagation.
If a 2π pulse is injected into a collection of on-resonant two-levelatoms,itcannotgiveanyenergytothembecause after its passage the atoms have been dynamically forced back into their initial state. Thus, a 2π pulse has a certain energy stability and so does a 4π pulse and every 2nπ pulse for the same reason. However, all other pulses are obviously not stable since they must give up some energy to the atoms if they do not rotate the atomic choherence vectors all the way back to their initial positions.
The effect on the injected pulse due to atomic absorptions is given by the Maxwell equation (21). When there is a broad distribution g( ) of detunings among the atoms, then Eq. (21) leads to a so-called area theorem, a nonlinear propagation equation for a pulse of area φ:
	d .	(29)
Here φ(z) means the total pulse area , where the integral extends over the duration of the pulse. The solution is tan φ(z)/2=e−αz/2, and the attenuation coefficient is α = Nσ, where N is the density of atoms and σ is the inhomogeneous absorption cross section:
	 ,	(30)
where  ) is the single-atom cross section (see Section II.E). For very weak pusles with  , one can replace sin φ(z) by φ(z) and recover from Eq. (29) the usual linearlawforpulsepropagation:dφ(z)/dz =−(α/2)φ(z), which predicts exponential attenuation of the pulse: φ(z)=φ(0)exp[−αz/2]. The factor of   arises because φ is proportional to the electric field amplitude, not the intensity.
Remarkably, one of the “magic” pulses with φ =2πn, which does not lose energy while propagating, also preserves its shape. This is the 2π pulse, for which there is a constant-shape solution of the reduced Maxwell–Bloch equations:
	χ(z,t) = (2/τp)sech[(t − z/V)/τp].	(31)
That is, the entire pulse moves at the constant velocity
V, which can be several orders of magnitude slower than the normal light velocity in the medium. In ordinary light propagation this would correspond to an index of refraction n ≈1000. All of these remarkable features were discovered by McCall and Hahn in the 1960s and labeled by the term self-induced transparency to indicate that a light pulse could manipulate the atoms in a dielectric in such a way that the atoms cannot absorb any of the light.
Self-induced transparency is an example of soliton behavior. The nonlinearity of the coupled Maxwell–Bloch equations opposes the dispersive character of normal light transmission in a polarizable medium to permit a steady nondispersing solitary wave (or soliton) [Eq. (31)] to propagate unchanged. This happens only for fields sufficiently strong that the 2π pusle condition can be met. The Maxwell–Bloch equations can in many cases be shown to be equivalent to the sine–Gordon soliton equation or generalizations of it.
D. Relaxation
Both photon echoes and self-induced transparency demonstrate the existence of optical phenomena dependingonχ ≈,andnoton2,thatis,ontheMaxwell–Bloch equations and not on the Einstein rate equations. How are these two approaches to light–matter interactions connected? To answer this question it is necessary to extend the scope of the Bloch equations and include the effects of line-broadening and relaxation processes.
Theupperlevelsofanysystemhaveafinitelifetime,and so |a2|2 cannot oscillate indefinitely as Eq. (14b) implies, but must relax to zero. This is most fundamentally due to the possibility of spontaneous emission of a photon, accompanied by a transition in the system to the lower level. Such transitions occur at the rate A, as in Einstein’s equation (1b).
Other relaxation processes also occur. For example, collisions with other atoms cause unpredictable changes in the state of a given two-level atom. These collisional changes typically affect the dipole coherence of the twolevel atom instead of the level probabilities, that is, they affect u and v instead of w. We suppose that the rate of such processes is γ. Although γ does not appear in Einstein’s rate equations, its existence is implied. This will be clarified later.
The fundamental equations of optical resonance, Eqs. (19), can be rewritten to include these relaxations as follows:
du/dt  u (32a) dv/dt  v (32b)
	dw/dt = −χv − A(w + 1).	(32c)
In the absence of relaxation (γ = A =0), the solutions of Eqs. (32) are purely oscillatory [recall Eq. (18)] and are said to be coherent. In the absence of the radiation field (χ =0), the on-resonance solutions are completely nonoscillatory: u = u0e−(γ+A/2)t v = v0e−(γ+A/2)t
w = −1 + (w0 + 1)e−At, all for χ = 0.
Thesesolutionsaresaidtobeincoherent.Ineachcase“coherence” refers to the existence of oscillations with a welldefined period and phase. In Bloch’s notation, the relaxation rates are written γ + A/2=1/T2, where A =1/T1, and T1 and T2 are called the “longitudinal” and “transverse” rates of relaxation.
Relaxation theory is a part of statistical physics, and in quantum theory statistical properties of atoms and fields are usually discussed with the aid of the quantum mechanical density matrix ρ. The density matrix for a two-level atom has four elements, ρ11,ρ12,ρ21, and ρ22. These are related to u,v, and w by the equations u =ρ12 +ρ21,v =−i(ρ12 −ρ21), and w =ρ22 −ρ11, which have the inverse forms:
	 	(33a)
	 	(33b)
	 	(33c)
	 .	(33d)
Here the brackets  are understood to refer to an average over an ensemble of parameters and variables inaccessibletodirectanddeterministicevaluation,suchastheinitial positions and velocities of all the atoms in a collection that may collide with and disturb a typical two-level atom. TheequationsgiveninEqs.(19)foru,v,andw canalso be obtained from ρ via the Liouville equation of quantum statistical mechanics: ihdρ/dt = [H,ρ]. The equations for the density matrix elements [Eqs. (33)] are d 
	)	(34a)
d
	)	(34b)
dρ11/dt = Aρ22 − (iχ/2)(ρ12 − ρ21)	(34c) dρ22/dt = −Aρ22 + (iχ/2)(ρ12 − ρ21). (34d)
WenowdemonstratetheconnectionbetweenEinstein’s equations and the quantum optical Eqs. (34). Consider the weak-fieldlimit i |.Inthislimittherate of change of the “off-diagonal” density matrix elements ρ21 and ρ12 is dominated by the first factor −(γ + A/2  ), and both ρ21 and ρ12 decay rapidly. If in addition
A , then ρ22 and ρ11 change relatively slowly, and so ρ21 and ρ12 rapidly adjust themselves to the small quasi-steady values:
 
These solutions show that the off-diagonal elements of the densitymatrixcanbedeterminedfromconstantnumerical factors and combinations of the diagonal density matrix elements. They can then be eliminated from Eqs. (34c and d).
This procedure is referred to as adiabatic elimination of off-diagonal coherence because the remaining equations for ρ11 and ρ22 no longer exhibit coherence. That is, they no longer have oscillatory solutions. The term adiabatic is appropriate in the sense that ρ21 and ρ12 are entrained by the slower ρ11 and ρ22. The reverse procedure, the eliminationofρ11 andρ22 infavorofρ21 andρ12,isnotpossible because the reverse inequality A is not possible.
These adiabatic off-diagonal solutions, once inserted into Eqs. (34) lead to an equation for the slowly changing ρ22 as follows:  d
Recall ρ22 =|a2|2 is the probability that the atom is in its upper state, and thus plays the same role as Pn in the Einstein equation (2a). Similarly ρ11 plays the role here of Pm there. By comparing Eqs. (2a) and (36) one sees that they are identical in form and content if one identifies the coefficient of ρ11 in Eq. (36) with the coefficient of Pm in Eq. (2a). In other words, the density matrix equations [Eqs. (34a–d)] of quantum optics contain Einstein’s equation in the weak-field and adiabatic limits   | and A .
The B coefficient can be derived in this limit (see
Section II.E) if one properly interprets the factor
 
Relaxation processes affect the Maxwell field as well as theBlochvariables.Todeterminetheformofrelaxationto assign to Maxwell equation (21) it is sufficient to consider the conservation of energy. From Eqs. (21) and (19c) it follows that
 ,
which is equivalent to an equation for photon flux and level probability
	 t,	(37a)
since hω  and w =2P2 −1.
Equation (37a) is Poynting’s theorem for a “onedimensional” medium. It expresses the conservation of photonfluxintermsofatomicexcitations.However,inthe absenceoftheresonanttwo-levelatoms(N =0),Eqs.(37) predicts (z−ct),whichmeansthatthephoton flux has the constant value (z0) at every point z = z0 +ct thattravelswiththepulse.Thisiscontradictorytoordinary experience in two respects. The medium that is host to the two-level atoms (e.g., other gas atoms, a solvent, or a crystal lattice) always causes both dispersion and absorption. They can be taken into account by modifying Eq. (37) slightly:
	 t,	(37b)
where vg is the group velocity for light pulses in the medium and κ its linear attenuation coefficient.
This form of the flux equation implies a similar alteration of Maxwell’s equation (21):
 (Ndω/4ε0c)[u −iv]. (38)
This form of Maxwell’s equation is useful in describing the elements of laser theory (see Section II.G).
E. Cross Section and the B Coefficient
How does one use quantum optical expressions to obtain basic spectroscopic formulas, such as for the absorption cross section and B coefficient? That is, given expressions derived from Eqs. (34), which are based on the Rabi frequency χ instead of the more familiar radiation intensity I or spectral energy density u(ω), how does one recover a cross section, for example? Consider the quantum optical derivation of the Einstein formula in Eq. (36). The transition rate (absorption rate or stimulated emission rate) can be identified readily. With the abbreviation β =γ + A/2, one obtains:
	abs. rate .	(39a)
2  2 + β2
The absorption rate is a peaked function of   whose value drops to   of the maximum value at  = ±β. Thus, β is called the halfwidth at halfmaximum (HWHM) of the absorption lineshape. This shows that relaxation leads to line broadening, and since β applies equally and individually to every atom, it is an example of a homogeneous linewidth.Recall(SectionI.B)thatinhomogeneousbroadening is not a characteristic of individual atoms but of a collection of them. From expression (39a) at exact resonance one obtains the relationship:
resonant transition rate=χ2/full linewidth.
This is the single most concise relationship between the parameters of incoherent optical physics (transition rate and linewidth) and the central parameter of coherence (Rabi frequency). It holds in situations much more general than the present example and allows rapid and accurate translation of formulas from one domain to the other.
With the use of   and I , Eq. (39a)
becomes
D2I	β abs. rate . (39b)
The introduction of the new dipole parameter D here is based on the assumption that all orientations of the atomic dipole matrix element d21 are possible (in case, e.g., all magnetic sublevels of the main levels 1 and 2 are degenerate). Then d2 ≡ |e·d21|2 must be replaced by its spherical average, that is, by D2/3, where D2 =|d21 ·d12|. We assume this is appropriate in the remainder of Section II.
The atomic absorption cross section σa is, by definition, the ratio of the rate of energy absorption, hω21 ×(abs. rate), to the energy flux (intensity) I of the photons being absorbed. From Eq. (39b) this ratio is
	D2ω	β
	 ,	(40)
where γ =β − A/2 is the specifically collisional contribution to the halfwidth. Formula (40) shows that a quantum optical approach to light absorption through the weak field limit of Eqs. (34) gives conventional results of atomic spectroscopy. If Doppler broadening is present, then Eq. (40) must be integrated over the Doppler distribution of detunings Eq. (26) as was done in Eq. (30).
Lineshape plays a key role in understanding the relationship of Eqs. (39) to the Einstein expression (1a) relating absorption rate to the B coefficient. The absorption cross section can be written σa = σtSa(ω; ω21), where σt is the total frequency-integrated cross section:
	 hc	(41a)
and Sa is the atomic lineshape
β/π
	Sa ,	(41b)
which is normalized according to  1, and in this case has a Lorentzian shape. A lineshape also exists for the radiation field and is expressed by u(ω), the spectral energy density function. One connects u(ω) with I by the frequency integral c I. In the monochromatic case cu ) takes the idealized singular form cu ), and Eq. (39b) is the result for the absorption rate.
In the general nonmonochromatic case, the expression for absorption rate involves the integrated overlap of u(ω) and the atomic lineshape function:
c 
	abs. rate .	(42)
This has the desired limiting form, involving u(ω), and not I , if the spectral width δωL of u(ω) is very broad in comparison to the width β of the absorption lineshape Sa. In this limit, which is implicit in Einstein’s discussion, Sa acts in Eq. (42) like a δ-function peaked at
 , and u(ω) is evaluated at ω=ω21. From Eq. (42) one can then extract the Einstein B coefficient:
	B .	(43)
A simple relation obviously exists between B and σt, namely hω21 B =cσt.
Another quantity of interest is σa(0), the on-resonance or peak cross section:
D2ω21
	σ  (0) =	.	(44)
By definition, σa(0)=σa(ω=ω21); or, conversely, σa(ω; ω21)=πβσa(0)Sa(ω; ω21). Representative values of σa(0) for an optical resonance transition lie in the range σa(0)≈10−13 to 10−17 cm2 for absorption linewidths in the range β ≈108 to 1011 s−1.
F. Strong Field Criterion and Saturation
The inequality  , on which the absorption rate formula (39) and thus the Einstein B coefficient is based, is important in quantum optics and radiation physics generally because it provides a criterion for distinguishing weak radiation fields from strong radiation fields. The inequality implies that there is a critical value cr for field strength that gives a universal meaning to the terms weak field and strong field, namely 0 cr and 0 cr, respectively, where:
cr
(45)
However,sincetheparametersγ, A,d,and mayvary by many orders of magnitude from case to case, the numerical value of cr may fall anywhere in an extremely wide range. Thus, it is possible that in one experiment a laser with the power level 1020 W/m2 must be designated “weak,” while another laser in a different experiment with the power level 1 W/m2 must be considered “strong.” This factor of 1020 is one indication of the great extent of the domain of quantum optics.
In conventional spectroscopy one sometimes encounters saturation effects. These are of course strongest in the strong field regime and are of interest in quantum optics.
There are two distinct time regimes of saturation phenomena. If  , then there is a range of times t   that can still contain many Rabi oscillations since  . During the time 0t δT, the fully coherent undamped formula (14b) can be used for the upper state probability. On average, during this time the probability that the atom is in its upper level is
	P ]	(short time average),	(46a)
which is a Lorentzian function of  =ω21 −ω with the power-broadening halfwidth δωp =χ. Power broadening is a saturation effect, because if   , then P  on average, which is obviously saturated, that is, unchanged if χ is made still larger.
Another saturation regime exists for long times, t  δT ≈ β−1. The solution of Eqs. (24) for P2 =ρ22 in this
limit is
	P .	(46b)
 β/A
Inthiscaseχ beginstodominatethewidththenχ2 > βA, which defines the saturation value of χ:
	 .	(47)
The power-broadening part of the width of Eq. (46b) is different than in Eq. (46a), namely  ). Depending on the value of γ ≡ β − A/2, the power width√ here can be anything between a minimum of χ/ 2, if γ =0, and a maximum of  A. This distinctionbetweenthesaturatedpower-broadened linewidth δωp predictedbyEq.(46a)forshorttimesandbyEq.(46b) for asymptotically long times has caused some confusion in the past. Further study indicates that Eq. (46b) breaks down for sufficiently large χ, basically because Blochtype relaxation, such as assumed in Eqs. (32), becomes invalid.Thefirstexperimentalreportsofthisregimeofoptical resonance were made by Brewer, De Voe, Mossberg, and others in the early 1980s.
In the case of asymptotically long times the expression for P2 can be written in several ways, using Eqs. (47) or (40):
 
where = I/hω21 and we have introduced the saturation flux required for saturation of the transition sat = A/σa (or =1/T1σa in Bloch’s notation, which is more appropriate if there are other contributions than spontaneous emission rate A to the level lifetimes). Figure 3 shows the effect of both power broadening and saturation on the steady-state probability P2.
 
Quantum Optics 
 
FIGURE 3 Population saturation for different values of x /xsat.
In common with all two-level saturation formulas, Eq. (48) and Fig. 3 predict P  at most. However, this prediction is valid only for weak fields or for long times. As the solutions in Eq. (14) and in Fig. 2 show, strong monochromatic resonance radiation can repeatedly transfer the electron to the upper level with P2 ≈1 for times
 . Experiments that show P2 >  have been practical only with lasers. Laser pulses are both short and intense, allowing   as well as t .
G. Semiclassical Laser Theory
The coupled Maxwell–Bloch equations can be used as the basis for laser theory. It is a semiclassical theory, but still adequate to illustrate the most important results, such as the roles of inversion and feedback, the existence of threshold,andthepresenceoffrequencypullinginsteadystate operation. A fully detailed semiclassical theory of laser operation was already given by Lamb in 1964.
The density matrix equations (24) must be modified to allow for pumping of the upper laser level and to allow the lower level to decay to a still lower level labeled 0 and not previously needed. The rates of these new processes are denoted R and,respectively.Thisisbasicallythescheme of a so-called three-level laser, as sketched in Fig. 4. The diagonal equations change to d  dρ22/dt = −Aρ22 − (i/2)χm(ρ12 − ρ21) + R. (50)
Here the index m or χm shows that we are dealing with the electric field of the mth mode of the laser cavity. The laser is easy to operate only if   A because only then can
 
FIGURE 4 Schematic diagram of three-level laser system.
a large positive inversion be maintained between the two levels with a value of R that is not too high and without seriously depleting the population of level 0. Under other conditions,theequationforthedensitymatrixelementρ00 would also have to be included. The off-diagonal density matrixequations(24aandb)arebasicallyunchangedifwe interpret γ as including another contribution /2, where  is the decay rate of the lower level probability to level
0 in Fig. 4.
The reduced Maxwell equation (28) is now useful. We will ignore the difference between vg and c, and write Eq.(38)intermsofχ insteadof,anduse  to find
 
Note that in a cavity κ can arise principally from mirror losses and not from absorption in the cavity volume. Thesameadiabaticeliminationofdipolecoherenceundertaken in Eqs. (35) provides the value for ρ21 to insert into Eq. (51), which in steady state (∂χm/∂t =0) becomes:
	 ,	(52)
where
	g	 )]	(53)
and now	 2. By using Eq. (40) one can
obtain
	g wss	(54a)
	cδκ = −(gc/β)(ω21 − ω),	(54b)
where Eq. (54a) has been used to simplify Eq. (54b). Here wss denotes the inversion ρ22 −ρ11 in steady state.
It is clear that g is the intensity gain coefficient, since if g >κ, Eq. (52) would predict exponential growth, |χm|2 ≈ exp[(g −κ)z], in an open-ended medium such as a laser amplifier. It is thus clear that g =κ is the threshold condition for amplification or laser operation. Also obviously, g is not positive unless wss is positive. Recall that in an ordinary noninverted medium w =−1, and in this case g =−Nσa =−α, where α is the ordinary absorption coefficient.
Rather than growing indefinitely, the field in a laser cavity must conform to the spatial period determined by the mirrors. Thus, at steady state χm(z)≈χ0 exp[i kmz], where the phase  kmz is the difference between the actual phase of steady-state laser operation kmz and the phase kz =ωz/c that was assumed initially in defining the field carrier wave and envelope functions in Eq. (20). Since χm does not depend on the transverse coordinates x and y, this theory cannot describe transverse mode structure, and km =mπ/L, where L is the cavity length and m is the longitudinal mode number. Operating values could be m ≈106 and L ≈10 cm, in which case the laser would run at a frequency near to mπc/L ≈3×1015 s−1 ≈5×1014 Hz.
In laser operation ∂/∂z can be replaced in Eq. (52) by i km and the imaginary part of Eq. (52) becomes  km  , which leads directly to a condition for the operating frequency ω:
	ωm − ω = −(κc/2β)(ω21 − ω).	(55)
This requires ω to lie somewhere between the empty cavity frequency ωm =mπc/L and the natural transition frequency ω21 of the atom, and it is said that the two-level laser medium “pulls” the operating frequency away from the cavity frequency mπc/L. The solution of Eq. (55) for ω is
	 .	(56)
H. Optical Bistability
The input–output relationships between light beams injected into and transmitted through an empty optical cavityarelinearrelationships.However,thesituationchanges dramatically if the cavity contains atoms. This is obvious in the case of laser action. However, even if the atoms are not pumped, their nonlinearities can be significant.
Consider a laser beam injected into an optical cavity filled with two-level atoms. For simplicity we consider the case where the frequencies of the atoms, the cavity, and the injected laser light are all equal: ω=ωc =ω21. Only the u − w Bloch equation are needed then:
	dv/dt = −βv + (χm + χ0)w	(57a)
	dw/dt = −A(1 + w) − (χm + χ0)v.	(57b)
Here χ0 and χm are the Rabi frequencies associated with the injected field strength and the cavity mode field generated by the atoms, and β =γ + A/2. The Maxwell equation for the internally generated χm is
	 v.	(58)
Note that there is no term i κm from ∂/∂z, as there is in the discussion of laser operation, only because of the three-way resonance assumption.
The question is, how does the presence of the atoms in thecavityaffectthetransmittedsignal?Sincethetransmitted signal differs only by a factor of mirror transmissivity from the total field in the cavity χt =χm +χ0, we ask for the relation between χ0 and χt. The dynamical evolution of the system is complicated. Early attention was given to this situation in the 1970s by Szoke, Bonifacio, Lugiato,¨ McCall, and others.
As with the laser, steady state is sufficiently interesting, so we put dv/dt =dw/dt =dχ/dt =0 and solve for χ0 or χt. They obey a simple but nonlinear relation:
	 ,	(59)
 
FIGURE 5 Bistable input–output curves for different values of C =a/2k.
where α is the (on-resonance) two-level medium’s absorption coefficient, α = ND2ω/3ε0hcβ, and  , the saturation parameter identified in Eq. (47). If both χ0 and χt are normalized with respect to χsat by defining ξ =χ0/χsat and η=χt/χsat then one finds the dimensionless relation:
	ξ = η + (α/κ)[η/(1 + η2)].	(60)
Of course the inverse relation η=η(ξ), that is, the total field strength as a function of the input field strength, is more interesting. Figure 5 shows the important features of thisrelation.Itdemonstratesthatthetotalfieldη isdoublevalued as a function of input field ξ if α/κ is larger than a certain critical value. In this simple model the critical value is α/κ =8, and the vertical segment in the central curve is an indication of this. The double-valued nature of the curves for α/κ>8 is termed optical bistability. In the bistable region of the third curve hysteresis can occur, and a hysteresis loop is shown.
The elements of a primitive optical switch are evident in the bistable behavior shown here. If the input field is held near to the lower turning point, then a very small increase in ξ can lead to a very large jump in η, the transmitted field. The possibility of optical logic circuits and eventually optical computers is clearly suggested even by the simple model described here, and efforts being made aroundtheworldtorealizethesepossibilitiesinapractical way have already achieved limited success.
III. RADIATION COHERENCE AND STATISTICS
A. Coherence of Light
In quantum optics the coherence of light is treated statistically.Theneedforastatisticaldescriptionoflight,whether quantized or classical, is practically universal since all light beams, even those from well-stabilized lasers, have certain residual random properties that are not uniquely determined by known parameters. These random properties lead to fluctuations of light. A satisfactory description can be based on a scalar electric field:
	E(r,t) = E(+)(r,t) + E(−)(r,t),	(61a)
where E(+) is the positive frequency part of E. That is, E(+) is the inverse Fourier transform of the positive frequency half of the Fourier transform of E. From this definition,onehas[E(−)(r,t)]∗ ≡ E(+)(r,t).Thesplit-upinto positive and negative frequency parts E(±)(r,t) is motivated by the great significance of quasi-monochromatic fields, for which one can write
	E t	(61b)
	E .	(61c)
The term quasi-monochromatic means that (r,t) is only slowly time dependent, that is, |d/dt .
Theintensityofthelightbeamassociatedwiththiselectric field is given by:
I 
where c.c. means complex conjugate. In principle I is rapidly time dependent, but the factors e±2iωt oscillate too rapidly to be observed by any realistic detector. That is, a photodetector can respond only to the average of Eq. (62) over a finite interval, say of length T beginning at t, where T π/ω. The e±2iωt terms average to zero and one obtains:
 
The overbar thus denotes a coarse-grained average value that is not sensitive to variations on the scale of a few optical periods. We have dropped the r dependence as a simplification. If the beam is steady and the averaging interval T is long enough, then both the length T and the beginning value I(t) are unimportant, and I¯T (t) is also independent of t. This is the property of a class of fields called stationary. Obviously even nonstationary fields can be considered stationary in the sense of a long T average, and we will adopt stationarity as a simplification of our discussion and write I¯T (t) simply as I¯.
Consider now the operation of a Michelson interferometer (Fig. 6). An incident beam is split into two beams a and b, and after traveling different path lengths, say and +δ, the beams are recombined and the beam intensity Ia+b =cε0[Ea(t)+ Eb(t)]2 is measured. If the beam splitter sends equal beams with field strength E(t) and intensity I¯ into each path and there is no absorption during the propagation, then one measures
 
FIGURE 6 Sketch of Michelson interferometer.
T
c 2dt
T c 
= I¯ + I¯ + 4cε0
	 ,	(64)
where Re means “real part” and the angular brackets indicate the time average. If δ =0, then I¯a+b =4I¯, because the two beams interfere fully constructively. The quantity
 iωδ/c is called the mutual coherence function of the electric field, and the appearance of fringes at the output plane of the interferometer is due to the variation of  with δ. From the factor e−iωδ/c it is clear that a fringe shift (a shift from one maximum of I¯a+b to the next) corresponds to a shift of δ by 2πc/ω=λ.
The mutual coherence function is conveniently normalized to its maximum value which occurs when δ =0, and the normalized function γ(δ/c) is called the complex degree of coherence. That is,
 
and the output intensity can be written:
	I¯a+b = 2I¯[1 + Reγ(δ/c)],	(66)
where Re γ must satisfy −1Re γ1.
It is common experience that if the path difference δ is made too great in the interferometer, the fringes are lost andtheoutputintensityissimplythesumoftheintensities inthetwobeams.Thiscanbeaccountedforbyintroducing a coherence time τ for the light by writing γ(δ/c) = γ(0)e−|δ|/cτe+iωδ/c. (67)
This representation for γ has the correct behavior since it vanishes whenever δ is large enough, specifically whenever  . For obvious reasons, cτ is called the coherence length of the light. This does not explain the fundamental origin of the coherence time τ, but the lack of such a deep understanding of the light beam can be one reason that a statistical description is necessary in the first place. Typically one adopts Eq. (67) as a convenient empirical relation and interprets τ from it.
The fringe visibility is usually the important quantity that describes an interference pattern, not the absolute level of intensity. The visibility is defined by V =(I¯max − I¯min)/(I¯max + I¯min), and this is directly related to the complex degree of coherence. Since
Reγ = |γ(0)|e−|δ|/cτcos(ωδ/c + φ) one has
	V  .	(68)
Thus, the magnitude of the complex degree of coherence is a directly measurable quantity.
One of the foundations of quantum optics was established by Wolf and others in classical coherence theory when it became understood in the 1950s how to describe optical interference effects in terms of measurable autocorrelation functions such as γ. In a sense, the first example of this was provided much earlier by Wiener in 1930 when he showed that the spectrum S(ω) of a stationary light field is given essentially by the Fourier transform of γ, considered as a function of a time difference τ rather than a path difference δ:
	S .	(69)
As a specific example, suppose a light beam with carrier frequency ωL has a Gaussian degree of coherence, with coherence time τ, that is,  
 ]. This is another example, similar to the exponential γ(δ/c) given above, in which a simple analytic function is used to model the normal fact that correlation functions have finite coherence, that is, that γ(τ)→0 as τ →∞. In this example the spectrum is
Gaussian:
S 
Theeffectivebandwidthisthefrequencyrangeoverwhich
S(ω) is an appreciable fraction of its peak value. In this casethespectrumiscenteredatω=ωL,andthebandwidth is given by  ω=2π ν =1/τ.
This is an example of the general rule that the bandwidth is the inverse of the coherence time. A laser beam with bandwidth  ν =100 MHz has a coherence time τ =1.6 ns and a coherence length  δ =cτ =0.5 m, while sunlightwithabandwidthsixordersofmagnitudebroader   Hz) has a coherence time τ =1.6×10−3 ps =1.6 fs and a coherence length cτ =0.5µm that are six ordersofmagnitudesmaller.Inthelattercase, ν ≈ν,and cτ ≈λ,sosunlightcannotbecalledquasi-monochromatic in any sense.
A hierarchy of correlation functions can be defined for statistical fields. One denotes by the degree of first-order coherence the normalized first-order correlation of positive and negative frequency parts of the field:
	g ,	(71)
where x  ) for short. In the case of a quasimonochro  matic field g(1) is just the same as γ defined above. The terms “first-order coherent,” “partially coherent,” and “incoherent” refer to light with |g(1)| equal to 1, between 1 and 0, and 0, respectively.
Definition (71) and other average values can be interpreted in an ensemble sense, as well as in a time average sense. In the ensemble interpretation the angular brackets   are associated with an average over “realizations,” that is, over possible values of the fields at given points x, weighted by appropriate probabilities. Two important examples are (1) so-called chaotic fields, fields that are stationary complex Gaussian random processes, and (2) constant intensity fields. The chaotic distribution is characteristicofordinary(thermal)lightsuchasomittedbythe sun, flames, light bulbs, etc. The constant intensity distribution is an idealization associated with highly stabilized single-mode laser (coherent) light. The ergodic assumption that time and ensemble averages are equal is usually made. We will write  interchangeably.
If p[,t]d2 is the probability that the complex field amplitude has the value  within d  in the complex  plane, then the thermal (chaotic) distribution for the complex amplitude (t) is a Gaussian function:
	pth 	(thermal)
(72a)
and the coherent distributions is a delta function:
pcoh )	(coherent)	(72b)
The spatial and temporal coherence properties of radiation, measured via γ or g(1) or S(ω), determine the degree to which the fields at two points in space and time are able to interfere. By the use of pinholes, lenses, and filters any sample of ordinary light can be made equally monochromatic and directional as laser light. Its spatial and temporal coherence properties can be made equal to those of any laser beam. If the laser light is then suitably attenuated so that it has the same low intensity as the ordinary light, one may ask whether any important differences can remain between the ordinary light and the laser light.
Surprisingly, the answer to this fundamental question is yes. The differences can be found in higher order correlationfunctions,involving∗topowershigherthan the first, such as  . These can be referred to as intensity correlations. The first measurements of optical intensity correlation functions were made on thermal light by Brown and Twiss in the 1950s before lasers were available.
Discussions of intensity correlations are typically made with the aid of a quantity called the degree of secondorder coherence and denoted g(2). Higher order degrees of coherence are also defined. If the fields are stationary only the time delays between the measurement points are significant, and one has:
g  g 
and so on. Because of stationarity we can put t =0 everywhere.Wewilldealmostlynowwith g(2) andnoconfusion should occur if we omit the index (2) whenever we have a single delay time τ. The assumption that the light is stationary gives g(τ)= g(−τ). Since I is an intrinsically positive quantity, it is clear that g(τ) is positive. There is no upper limit, so g satisfies  0. In addition, for any distribution of I one has , so obviously g(0) ≥ 1; and one can also show that g(0) ≥ g(τ).
With the aid of the thermal and coherent probability distributions given above, several higher order coherence functions can be calculated immediately. For example, if τ1 =τ2 = ... =0, the nth order moments of the intensity are simply :
	 	(thermal)	(74a)
	 	(coherent).	(74b)
For large values of n these are obviously quite different, even if I¯ is the same for two light beams, one thermal and the other coherent. The difference plays a role in multiphoton ionization experiments with n =2 and larger. This is one example of a fundamental difference between ordinary light and ideal single-mode laser light.
It should be clear that in addition to thermal light and laserlighttheremaybestillotherformsoflight,characterizedbydistributionsotherthanthoseinEq.(72).Quantum theory also predicts that there can even be kinds of light beams for which the underlying probability distribution does not exist in a classical sense, for example, it may be negative over portions of the range of definition. Generalized phase space functions that play the quantum role of classical probability densities were developed by Glauber and Sudarshan in the 1960s. These are still a principal theoretical tool in studies of photon counting.
 
FIGURE 7 Ideal Poisson photocount distribution. [Adapted with permission from Loudan, R. (1983). “The Quantum Theory of Light,” 2nd ed. Oxford Univ. Press, Oxford, UK. Copyright 1983 Oxford University Press.]
B. Photon Counting
In photon counting experiments the arrival of an individual photon is registered at a photodetector, which is essentially just a specially designed phototube that gives a signal when an arriving photon ionizes an atom at the phototube surface. A typical experiment consists of many runs of the same length T in each of which the number of photons registered by the photodetector is counted. The counts can be organized into a histogram (Fig. 7), which is interpreted as giving the probability Pn(T) for counting n photons during an interval of length T.
An expression for Pn(T) follows from a consideration of the photodetection process, which begins with the ionization of a single atom by a single photon at the surface of the phototube. In any event, the rate of counting is proportional to the intensity of the light beam, so one writes αI(t)dt for the probability of counting a photon at the time t in the interval dt. The factor α takes account of the atomic variables governing the ionization process as well as the geometry of the phototube. It was first shown by Mandel in the 1950s that Pn(T) is then given by
Pn , (75)
where the average is over the variations in intensity during the (relatively long) counting intervals. Alternatively, it can be considered an average over an ensemble of identically prepared runs in which the value of I¯ is statistically distributed in some way.
The simplest example occurs if the light intensity does not fluctuate at all, which is characteristic of an ideal single-mode laser (coherent) light beam. In this case Eq. (75) is independent of the t average and, with n¯ =αIT¯ .
	Pn = e−n(n¯)n/n!	(coherent),	(76)
which is the well-known Poisson distribution. It is easily verified that  ). That is, as its form indicates, n¯ is the average number of photons counted in time T. It is a feature of the Poisson distribution that its dispersion is equal to its mean:
 	(Poisson).	(77) AplotofanidealPoissonphotocountdistributionisshown in Fig. 7. The Poisson distribution is also called the coherent or coherent-state distribution because it is predicted by the quantum theory of light to be applicable to a radiation field in a so-called coherent state (see Section III.C). A well-stabilized single-mode laser gives the best realization of a coherent state in practice.
It should be obvious that the same Poisson law will be found even if   is not constant, so long as T is made great enough that all fluctuations associated with a particular interval are averaged out. The counting fluctuations associated with steady   are due to the discrete single-photon character of the atomic ionization event that initiates the count and are called particle fluctuations.
AlthoughthePoissondistributionistheresultfor Pn(T) inthesimplestcase,constant ,itisnotthecorrectresult for ordinary thermal light unless T is very long, in fact 2π νT 1 is necessary. We have posed a question at the endofthelastsectionaboutdifferencesbetweenlaserlight and thermal light with equal (very narrow) bandwidths. In that case  ν is very small, so we cannot automatically assume 2π νT 1. In fact it illustrates the point to assume the reverse. If 2π νT 1, we can assume  is constant over such a short time T. However,  can still fluctuate with t, that is, from run to run. To evaluate the average over t, which is now essentially an average over runs, we use the thermal distribution Eq. (72a) for , which is equivalent to the normalized exponential distribution for I p(I) = (1/I¯)e−I/I¯ (thermal), (78)
since I . Then Eq. (75) gives
	Pn(T) = (n¯)n/(1 + n¯)1+n	(thermal),	(79)
which is variously called the thermal, chaotic, or Bose– Einstein distribution, and n¯ is defined as before, n¯ =αIT¯ , with the understanding that here I¯ means the average over many runs, all shorter than 1/2π ν. The difference between the photocount distributions for thermal light under the two extreme conditions 2π νT  1 and 2π νT  1 is shown in Fig. 8. The nature of the difference between thethermalandcoherentprobabilitydistributions(76)and (77), and thus of the fundamental difference between natural light and single-mode laser (coherent) light, can show updirectlyintherecordofphotocountmeasurements,asis clearbyinspectingFigs.7and8.Otherphotoncountdistributions than these two correspond to lightthatis somehow different from both laser light and thermal light. In quantum optics the most interesting examples are examples of purely quantum mechanical light beams.
 
FIGURE 8 Thermal photocount records for 2p T n 1 and 2p T n 1. [Adapted with permission from Loudon, R. (1983). “The Quantum Theory of Light,” 2nd ed. Oxford Univ. Press, Oxford, UK. Copyright 1983 Oxford University Press.]
C. Quantum Mechanical States of Light
The quantum theory of light assigns operators in a Hilbert space to the fields of electromagnetism. Any field F(r), quantum or classical, can be written as a sum of plane waves (as a three-dimensional Fourier series or integral):
F ik·r]
k
 ik·r]
k
	+ f−k exp[−ik·r]}, k 0	(80)
and f−k = fk∗ if F(r) is a real function. If F is operatorvalued real (i.e., hermitean), then the expansion coefficients fk are operators and one writes f−k = fk†, where the dagger denotes hermitean adjoint in the usual way. In the case of electromagnetic radiation a given plane wave mode has the transverse electric field
Ek ,	(81) where Nk is an appropriate normalization constant. The full field is obtained by summing over k: E(r)=
 
Because ak and ak† are operators rather than numbers, ak†ak = akak†. This is expressed by saying that they obey the “canonical” commutation relations:
[ak,ak†] = 1,	(82) where	the	square	bracket	means	the	difference akak† −ak†ak, as is usual in quantum mechanics. All other commutators among a’s and a†’s for this mode, and all commutators of ak or ak† with operators of all other modes vanish, for example, [ak,al]=0. The time dependences of these operators, and thus of the electric and magnetic fields, are determined dynamically from Maxwell’s equations,whichremainexactlyvalidinquantumtheory.Inthe absence of charges and currents the time dependences are
ak(t) = ake−iωkt and ak† = ak†eiωkt, (83) where ωk =kc.
The hermitean operator a†a (we drop the mode index k temporarily) has integer eigenvalues and is called the photon number operator:
	a ,...,	(84)
and the eigenstate |n is called a Fock state or photon number state. The operators a† and a are called the photon creation operator and destruction operator because of their effect on photon number states:
a ,
and	(85)
a .
That is, a† and a respectively increase and decrease by 1 the number of photons in the field state. The photon number states are mutually orthonormal:  mn, and they form a complete set for the mode, and all other states can be expressed in terms of them. They have very attractive simple properties. For example, the photon number is exactly determined, that is, the dispersion of the photon number operator a†a is zero in the state  for any n:
 
= n2 − n2 = 0.
However,thenicepropertiesofthe|nstatesareinsome respects not well suited to the most common situations in quantum optics. For example, loosely speaking, their phase is completely undefined because their photon number is exactly determined. As a consequence, the expected value of the mode field is exactly zero in a photon number state. That is n  0, because Eq. (85) and the orthogonalitypropertytogethergive 
In most laser fields there are so many photons per mode that it is difficult to imagine an experiment to count the exact number of them. Thus, a different kind of state, called a coherent state, is usually more appropriate to describe laser fields than the photon number states. These states  are right eigenstates of the photon destruction operator a:
	a .	(86)
They are normalized so that  1. Since a is not hermitean, its eigenvalue α is generally complex. The expected number of photons in the mode in a coherent state is  . Thus, α can be interpreted loosely as , the square root of the mean number of photons in the mode. The number of photons in the mode is not exactly determined in the state . This can be seen by computing the dispersion in the number:
Thus, the dispersion is equal to the mean number, a property already noticed for the Poisson distribution (77). If
 1, then the relative dispersion  is very small, and the number of photons in the state is well determined in a relative sense. At the same time, a relatively well-defined phase can also be associated with the state.
The clearest interpretation of the amplitude and phase associated with a coherent state |α is obtained by computing the expected value of E in the state  . Since  , one easily determines that
	Nk  ,	(88)
where V is the mode volume, and then Nk can be interpreted loosely as the electric field amplitude associated
 
with one photon. This shows that Nkα =√(hωk/2ε0V)α is the mean amplitude of the expected electric field, or whatissometimescalledtheclassicalfieldamplitude.The phase of α thus determines the phase of the field described by the state .
The coherent states can be expressed in terms of the photon number states:
	 	,	(89)
m
where the sum runs over all integers m 0. From Eq. (89) one can compute the probability pn(α) that a given coherent state   contains exactly n photons. According to the principles of quantum theory this is given by , and we find:
	pn !,	(90)
which is exactly the “purely random” Poisson probability distribution shown in Fig. 7. This is interpreted as meaning that photon-counting measurements of a radiation field in the coherent state  would find exactly n photons with probability (90).
The photon creation and destruction operators are not hermitean and are generally considered not observable, but their real and imaginary parts (essentially the electric and magnetic field strengths, or in other terms, the inphase and quadrature components of the optical signal) are in principle observable. Thus, one can introduce the definitions
	a , a )	(91)
and their inverses
	a1 = a + a†, a2 = i(a − a†).	(92)
and a2? They must, uncertainty relation
, whereindicates
expectation value in any given quantum state, and
What are the quantum limitations on measurement  a .	Since	[a,a†]=1,	it	follows	from
Eq. (91) that [a1,a2]=−2i, so the Heisenberg relation for a1 and a2 is:
	 .	(93)
A coherent state  can be shown to produce the minimum simultaneous uncertainty in a1 and a2. That is,
 1 and  1. Both a1 and a2 are therefore said to reach the quantum limit of uncertainty in a coherent state.
However, it is only the product of the operator dispersions that is constrained by the Heisenberg uncertainty relation, and there is no fundamental reason why either a1 anda2 could not have a dispersion equal to, µ1, so long as the other had a dispersion at least as large as 1/µ1. A quantum state of the radiation field that permits one of the components of the destruction operator to have a dispersion smaller than the quantum limit is said to be a squeezed state. Squeezed states could in principle provide the ability to make ultraprecise measurements such as are projected for gravity wave detection. A squeezed state of radiation was first generated and measured by Slusher and others in 1985.
IV. QUANTUM INTERACTIONS AND CORRELATIONS
It should be remembered that the highly successful semiclassical version of the quantum theory of light (Sections I and II) does not ignore quantum principles, or put h →0, but it does ignore quantum fluctuations and correlations. It is a theory of coupled quantum expectation values.
In the following sections of a number phenomena depending directly on quantum fluctuations and correlations aredescribed.Noneofthemhavebeensuccessfullytreated by the semiclassical theory or by any other theory than the generally accepted and fully quantized version of the quantum theory of light. For this reason the observation of these and similar quantum optical effects can offer a means of testing the accepted theory.
Such tests are of great interest for two related reasons. Because the quantum theory of light (or quantum electrodynamics) is the most carefully studied quantum theory, and because it serves as a fundamental guide to all field theories, it plays a key role in our present understanding of quantum principles and should be tested as rigorously as possible. Moreover, tests of the effects described below play a special role because they bear on the theory in a different way compared with traditional tests, such as high-precision measurements of the Lamb shift, the fine structure constant, the Rydberg, and the electron’s anomalous moment.
A. Fully Quantized Interactions
The electric field is mainly responsible for optical interactions of light with matter, and the magnetic field plays a subsidiary role, becoming significant only in situations involvingmagneticmomentsorrelativisticvelocities.The most important light–matter interactions is the direct coupling of electric dipoles to the radiation field through the interaction energy −d·E.
A systematic description of the fully quantized interactions of quantum optics begins with the total energy of the atom HA and the radiation HR and their energy of interaction:
	H = HA + HR −d·E.	(94)
In the quantum theory the atomic, radiation, and interaction energies are given by the Hamiltonian operators
	HA j|	(95a)
j
	HR ak	(95b)
k  d·E 
	i	j	k
Here E j and are the quantized energies and eigenstates of the atom including level-shifting and level-splitting due to static fields that give rise to Zeeman and Stark effects, etc.Thedipolecouplingconstantish fijk = Nkeˆ ·dij,inthe notation of Eqs. (9) and (39). Also, ak† and ak are the photon creation and destruction operators introduced in Section III.C.
The two-level version of this Hamiltonian is the most used in quantum optics. It is obtained by restricting the sums over i and j to the values 1 and 2. It is not necessary that  be the two lowest energy levels. In photoionization, which is the physical process underlying the operation of photon counters, the upper state is not even a discreate state but lies in the continuum of energies above theionizationthreshold(seeSectionIV.B).Initstwo-level version H becomes
H kak†ak
k
	 ,	(96)
k
where  , and f12k has been taken to be real for simplicity. Note that σ has the effect of a lowering transition when it acts on the two-level atomic
state . That is,	 
takes the amplitude C2 of the upper state and assigns it to the lower state  . By the same argument σ† causes a raising transition.
Thetermak†σ† inEq.(96)isdifficulttointerpretbecause it has σ† raising the atom into its upper state together with ak† creatingaphoton.Oneexpectsphotoncreationtobeassociatedonlywithaloweringoftheatomicstate.Theterm akσ presentssimilardifficulties.Itcanbeshown,however, that these two terms are the source of the very rapid oscillations exp[±2iωt] which were discussed above Eq. (12) and were eliminated by the rotating wave approximation (RWA). The adoption of the RWA eliminates them here also. With the RWA and the convenient convention that E1 =0 (and therefore that E2 =hω21), the working twolevel Hamiltonian is
H  kakak†
k
	  .	(97)
k
The operators σ,σ†, and σz are closely related to the 2×2 Pauli spin matrices:
 
 
One can easily confirm that the matrix representation of σ is a “lowering” operator in the two-dimensional space with basis vectors
	 	and	 	(98d)
and σ† is represented by the corresponding “raising” operator. The σ’s obey the commutator relations:
[σ,σz] = 2σ, [σ†,σz] = −2σ†, [σ†,σ] = σz. (99)
Changes in the radiation field occur as a result of emission and absorption of photons during transitions in the atom. One consequence is that ak obeys an equation obtained from the Heisenberg equation ih∂O/∂t =[O, H] that is valid for all operators O:
	∂ak/∂t = −iωkak + i fkσ.	(100)
Here we have simplified the notation, rewriting f12k as fk. The solution, of Eq. (100) is:
ak(t) = ak(0)e−iωkt + ifk	 )	
The first term represents photons that are present in the mode k but not associated with the two-level atoms (e.g., from a distant laser), and the second term represents the photons associated with a transition in the two-level atom.
The σ operators also change in time in the course of emission and absorption processes. Their time dependence is also determined by Heisenberg’s equation and one finds the equations:
	dσ/dt z	(102a)
k
	d z	(102b)
k
	dσz/dt ak − ak†σ).	(102c)
k
These are the operator equations underlying the semiclassical equations for the Bloch vector components given in Eq. (19).
The correspondence between the quantum and semiclassical sets of variables is
t
(103a)
t
(103b)
	σz → w.	(103c)
This identification is precise if the radiation field is both intense and classical enough. This means that one retains only one mode and replaces ak and ak† by their coherent state expectation values α =α0 e−iφ and  . Then Eqs. (102) are identical with Eq. (19) under the previous assumptions, that is, the field is quasi-monochromatic so φ =ωt, and Nkα is the slowly varying electric field expectation value, which is interpreted as the classical field amplitude. Thus, one has
	 	(104)
The part of ak that depends on σ in Eq. (100) acts as a radiation reaction field when substituted into Eq. (102). It causes damping and a small frequency shift in the atomic operator equations even if there are no external photons present and thus is associated with spontaneous emission. The damping constant is exactly the correct Einstein A coefficient for the transition, because the A coefficient is a two-level parameter.
The frequency shift is only a primitive two-level version of a more general many level radiative correction such as the Lamb shift. One observes here a natural limitation of any two-level model. It is intrinsically incapable of dealing with any precision with effects, such as radiative level shifts, that depend strongly on the contributions of many levels. However, in the cases of interest described in the remainder of Section IV, the effects of other levels are negligible and the numerical value of the frequency shift is irrelevant. It can be assumed to be included in the definition of ω21.
B. Quantum Light Detection and Statistics
The quantum theory of light detection is based on the quantum theory of photoionization because photon counters are triggered by an ionizing absorption of a photon. Photoionization is a weak field phenomenon because the effective γ is so large [recall Eq. (45)]. Thus, perturbative methods are adequate and one computes the absolute square of the ionization matrix element, in this case given by er , where |I  are the initial and finalstatesofthephotoionization.Theinitialstateconsists of an atom in its ground state, described by the electronic orbital function φ0(r), and the initial state of the radiation field . The final state consists of the atom in an ionized state described by an electronic orbital functionφ f (r) appropriate to a free electron with energy above the ionization threshold, and another state of the radiation field  . Then the matrix element becomes
 d3r
	 ,	(105)
k
where d f 0 is the so-called dipole matrix element for the 0→ f transition in the atom. We have also made the “dipole” approximation, in which exp[ik·r]≈exp[i0]≈
1 over the entire effective range of the matrix element integral [recall the discussion following Eq. (9)].
Only the part of E that lowers the photon number of the field, namely the “a” part, is effective in ionization, essentiallybecauseionizationisaphoton-absorptionprocess.In addition we can take a single k value if the incident light is monochromatic. Thus, the ionization rate depends on fk  , where fk =|d f 0 ·eˆk|Nk. The actual final states of the atom and of the field are never completely observed, and all the unobserved features must be allowed for, that is, included by summation:
rate 
!
 ,
since	 1 for a complete set of final states.
In this expression for the ionization rate we write “≈” instead of “=” because we are really interested here only in the effects of field quantization on the rate, not the exact numericalvalueoftherate.Iftheradiationfieldisquantum mechanical we do not know perfectly the properties of the incident light, and these properties must be averaged. This average over the properties of the incident light is the same average discussed from a classical standpoint in Sections III.A and III.B. Thus, we finally have
	rate ,	(106)
where the angular brackets now mean an average over the initial field, that is, the quantum mechanical expectation value in state  .
The significance of Eq. (106) is in the ordering of the field operators. The nature of the photoionization process mandates that they be in the given order and not the reverse. Since a†a is not equal to aa† for a quantum field, the order makes a difference. The order given, in which the destruction operator is to the right, is called normal order. Photoionization is a normally ordered process by its nature, and therefore so is photodetection and photon counting. This has fundamental consequences for quantum statistical measurements, as we now explain.
Let us consider the degree of second-order coherence g(2) in quantum theory. This was written in Eq. (73a) as an intensity correlation: g . Because of the normally ordered character of photoionization, if g(2) is measured with photodetectors as usual, its correct definition according to the quantum theory of ionization is normally ordered:
g .
(107)
If photon fields were really classical, and these quantum mechanical fine points were unnecessary, then the ordering would make no difference, since the fields E(±) would be numbers, not operators, and the original expression for g(2) would be recovered. However, we now exhibit the effects of these quantum differences in a few specific cases.
In the case of a single-mode field, there are no time dependences and g(2)(τ)= g(2)(0) simplifies to
	g ,	(108)
which we evaluate in Table II. Among these examples the Fock state is special because its g(2) violates the condition g(2)(0) ≥ 1,whichisoneoftheclassicalinequalitiesgiven below Eqs. (73). The Fock state is therefore an example of a state of the radiation field for which the quantum and classical theories make strikingly different predictions. It has not yet been possible to study a pure Fock state of more than one photon in the laboratory.
Photon bunching is a term that refers to the fact that photon beams exist in which photons are counted with statistical fluctuations greater than would be expected on the basis of purely random (that is, Poisson) statistics. In
TABLE II Second-Order Degree of Coherence for Single-Mode Quantum Mechanical Fields in Different States
Quantum field state	Value of g(2)(0)
Vacuum state 
Fock state  	 
 /n,	if n ≥ 2
Coherent state
Thermal state	2
fact, almost any ordinary beam (thermal light) will have this property, and this is reflected in that g(2) >1 for thermallight.PhotonbunchingthereforearisesfromtheBose– Einstein distribution [Eq. (39)]. A coherent state with its Poisson statistics is purely random and does not exhibit bunching.
A qualitative classical explanation of photon bunching is sometimes made by saying that light from any natural source arises from broadband multimode photon emission by many independent atoms. There are naturally random periods of constructive and destructive interference amongthemodes,givingrisetolargeintensity“spikes,”or “bunches” of photons, in the light beam. Unbunched light comes from a coherently regulated collection of atoms, such as from a well-stabilized single-mode laser. From this point of view, unbunched coherent light is optimally ordered.
However,photonantibunchingcanalsooccur.Thereare “antibunched” light beams in which photons arrive with lower statistical fluctuations than predicted from a purely coherent beam with Poisson statistics. Antibunched light beamshavevaluesofg(2) <1,incommonwithapureFock state beam, and are therefore automatically nonclassical light beams.
The first observation of an antibunched beam with g(2) <1 was accomplished by Mandel and others in 1977 in an experiment with two-level atoms undergoing resonance fluorescence. Antibunching occurs in such light for a very simple reason. A two-level atom “regulates” the occurrence of pairs of emitted photons very severely, even more so than the photons are regulated in a singlemode laser. A second fluorescent photon cannot be emitted by the same two-level atom until it has been reexcited to its upper level by the absorption of a photon from the main radiation mode. Thus, a high Rabi frequency χ permits the degree of second-order coherence g  to be nonzero after a relatively short value of the time delay τ, but g(2) is strictly zero for τ = 0. A graph showing the experimental observation is given in Fig. 9.
The significance of photon statistics and photon counting techniques in quantum optics and in physics is clear.
 
FIGURE 9 Curves of the second-order degree of coherence, showing photon antibunching. [Reprinted with permission from Dagenais, M., and Mandel, L. (1978). Investigation of two-time correlations in photon emission from a single atom. Phys. Rev. A 18, 2217–2228.]
They permits a direct examination of some of the fundamental distinctions between the quantum mechanical and classical concepts of radiation.
C. Superradiance
Nonclassicalphotoncountingstatisticsarisefromthemultiphoton correlations inherent in specific states of the light field. Similarly, multiatom quantum correlations can give rise to unusual behavior by systems of radiating atoms, as was pointed out by Dicke in 1954. The most dramatic behavior of this kind is called Dicke superradiance or superfluorescence.
Multiatom correlations can exist in N-atom systems even if N is as small as N =2. A pair of two-level atoms labeled a and b can have quantum states made of linear combinations of the elementary two-atom states
(109a)
(109b)
(109c)
	.	(109d)
Here the sign ∗ indicates a tensor product of the vector spaces of the two atoms, and + and − designate the upper and lower energy levels, with energies E2 and E1, in each of the identical atoms. The two middle states Eq. (109b and c) are degenerate, with total energy E1 + E2 = E2 + E1. It is useful to define the “singlet” and “triplet” states   that are linear combinations of the degenerate states as follows:
 
in analogy to singlet and triplet combinations of two spin   states.
The two-atom interaction with the radiation field is through d·E as in the one-atom case [recall Eq. (95)], and here both atoms contribute a dipole moment:
eˆ  
	 ,	(111)
where we have taken equal matrix elements: eˆ ·(d21)a = eˆ ·(d21)b =d.
The main features of superradiance lie in the fact that thetwo-atomdipoleinteractioncausestransitionsbetween the various states of the system at different rates, and the reason for the difference is the existence of greater internal two-atom coherence in the case of the triplet state. Suppose that the two-atom system is fully excited into the state , which has energy 2E2, and then emits one photon. The system must drop into a state with energy E2 + E1. From this state it can decay further by emission of a second photon to the ground state  which has energy 2E1.
According to the Fermi Golden Rule, the rate of these transitions depends on the square of the interaction matrix element between initial and final states, F|d·E , summed over all possible final states. We consider the second transition, so there is only one possible final atomic state, namely . The matrix elements factor into an atomic part and a radiation part. We can use Eq. (81) in the dipole approximation to write
 d eˆk .
k
Since superradiance deals only with spontaneous emission, the initial radiation state is the empty or vacuum state. Thus, the field contribution to the matrix element comes just from ak† and is the same in all cases and not interesting.
The various possible atomic matrix elements are
 d	(112a)  d	(112b) 0	(112c)
	d,	(112d)
so their squares have the relative values 1:1:0:2. That is, the triplet initial state can radiate twice as strongly as either of the original degenerate states, and the singlet statecannotradiateatall.Boththetripletandsingletstates are said to be two-body “cooperative” states because they cannot be factored into one-atom states.
It is tempting to interpret these results by saying that the triplet state radiates more rapidly because it has a larger dipole moment than the others and that the singlet state has no dipole moment. Such an interpretation is in the spirit of semiclassical radiation theory, as described in Section I.C, where the expectation values of quantum operators are treated as if they are classical variables. This interpretation has a number of useful features, but must also contain serious flaws, because the observation that it is based on is not true. A calculation of the dipole expectation value shows  0, where  can be any of the two-atom states above, including the rapidly radiating triplet state.
A state with a large dipole moment expectation does exist, namely the factored state
 
This state is actually an eigenstate of the total dipole operator:
eˆ  
 
soonehas d.Thisstateisalsopredicted to radiate strongly.
The extrapolation of these predictions to an N-atom system leads to the prediction of a very large N-atom emission intensity IN . Related predictions are that the Natom cooperative process begins with a relatively slow buildup. After a delay of average length δτN , an ultrashort burst of radiation of duration τN occurs. In the ideal case one predicts
	IN  	(114a)
τN ≈ τ1/N	(114b)
δτN ≈ τ1 ln(N),	(114c)
where τ1 is the single-atom radiative lifetime: 1/τ1 ≡ A.
If one imagines even small collections of atoms with
N ≈1012, then N2 is impressively very much bigger than
N and the term superradiance is indeed apt. If A ≈108 s−1 is taken as typical for 2 eV optical transitions, then N ≈1012 suggests that 2×1012 eV of energy can be expected at the rate 1020 s−1 for a purely spontaneous power output of 2×1032 eV s−1 ≈3×1011 W.
Other aspects of superradiance are equally interesting on fundamental grounds. For example, which of the two large dipole states,  , is actually responsible for superradiance? They both predict IN ≈ N2hω21, but their correlation properties are completely different, in somewhat the same way that a photon number state |n and a coherent state   have very different correlation properties even if they predict the same mode energy |α|2hω=nhω. Consider only the fluctuations in d itself for the two states. If one calculates the expectation of the dispersion of  d , one finds:
	 0	(115)
	 .	(116)
One can infer that radiation from the state  can be expected to exhibit strong fluctuations of a kind completely absent in radiation from the state  .
The fluctuations predicted from the state  are consistent with the fact that it is exactly the state connected directly to the initial fully excited state by the total dipole operator d. That is, eˆ . The fluctuations can be associated with the quantum uncertaintyintheemissiontimeofthefirstphoton.Suchfluctuationswillinfluenceallsubsequentevolution,andif N 1, they can be regarded as an example of a macroscopic quantum fluctuation, that is, a fluctuation with quantum mechanical origins that achieves direct macroscopic observability.
For a period of years, superradiance was a controversial and unobserved phenomenon. The intense and highly directional light beam predicted for the effect suggests that eachemittedphotoncontributestoaspontaneousradiation field, which helps to stimulate the emission of further photons. Such a self-reactive process would provide a feedback analogous to that provided by mirror reflections in a laser cavity. It has been suggested that the physical origins of superradiance and laser emission are in fact the same thing. Important differences exist, however. During laser action, the dipole coherence of an individual atom is interrupted by collisions extremely frequently. The incoherent adiabatic solution for ρ21 is a quite satisfactory element of all laser theories (recall Section II.G). By contrast, in ideal Dicke superradiance all N-atom dipole coherence is fully preserved during the entire radiation process.
Theexperimentalobservationofsuperradiancewasfirst achievedinthe1970sbyFeld,Haroche,Gibbs,andothers. Agreement has been found with the correlated state predictions,particularlywiththestatisticalnatureofthedelay time fluctuations, and there is no longer any controversy over its existence. However, important questions about quantum and propagation effects on the spatial coherence properties of superradiance remain open.
D. Two-Level Single-Mode Interaction
WehaveemphasizedthatbeginningwithEinstein’sreconsideration of Planck’s radiation law, the most fundamental interacting system in quantum optics is a single two-level atom coupled to a single mode of the radiation field. This interaction was described semiclassically in Section II.A, and the quantum mechanical origin of the semiclassical equations was explained in Section IV.A. Fully quantum mechanicalstudiesofthequantumcoherencepropertiesof this simplest interacting system were initiated by Jaynes in the 1950s. Some of the differences between general quantum and semiclassical theories have been clarified in this context.
When only one mode is significant the Hamiltonian [Eq. (97)] can be reduced to:
HJC a†a
	+hλ(a†σ + σ†a).	(117)
Here λ= f12k , which is assumed real for simplicity. Remarkably, the effective Hamiltonian [Eq. (117)] for such a truncated version of quantum electrodynamics (the socalled Jaynes–Cummings model) has a number of important properties, and experimental studies by Haroche and Walther and others were begun in the early 1980s. Exact expressions are known for the eigenvalues and eigenvectors of HJC. With h =1 for simplicity and  =ω21 −ω, the eigenvalues are
	En, ,	(118a)
where we have reinserted E  0 for the lower level energy, and the corresponding eigenvectors are given by
 
where	cos 
 . Here the use of n for √4λ2n +δ2 is a deliberate reminder of  defined following Eqs. (12) because they play the same roles in their respective quantum and semiclassical theories. Similarly, one writes χ(n) as a reminder of χ for the same reason, that is,
 
χ(n)=2λ√n istheQEDequivalentoftheRabifrequency
  [and not to be confused with the χm of Eqs. (49) and (50)].
One of the observable quantities of the Jaynes– Cummings model is the atomic energy. Its expectation value can be calculated exactly, without approximation:
	 	(quantum).	(119a)
n
Here pn is the probability that the single mode has exactly n photons. This result can be contrasted with Eq. (18c) in
 
FIGURE 10 Quantum collapse and revival of atomic inversion.
the same limit  =0 and under the same circumstances, namely, with the field intensity I ≈χ2 distributed with some probability p(I) over a range of values:
	w t dI	(semiclassical).
(119b)
The apparent similarity of these results disguises fundamental differences in dynamical behavior between Eqs. (119a and b). These differences arise from the discreteness of the allowed photon numbers in Eq. (119a), which are discrete precisely because the field is quantized, that is, because the mode contains only whole photons and never fractional units of the energy hω. By contrast, in the semiclassical theory (recall Section I.C) the intensity I and Rabi frequency χ can have any values.
For the quantum photon distribution associated with a coherent state, for which pn is given by Eq. (90), a plot of  is shown in Fig. 10. The nearly immediate disappearance “collapse” of the signal shortly after t =0 can be explained on the basis of the interference of many frequencies χ(n) in the quantum sum of Eq. (119a). Such a collapse can be expected for any broad distribution pn and would be predicted by the semiclassical Eq. (119b) as well, if p(I) is a broad distribution function. However, the predicted reappearances or “revivals” of the signal are a sign that the field is quantized. They occur, and at regular intervals, only because pn is a discrete distribution. The semiclassical expression (119b) leads inevitably to an irreversible collapse. Only quantum theory can provide the stepwise discontinuous photon number distribution that is the basis for the revivals.
The revivals and other quantum mechanical predictions implied by the truncated Hamiltonian [Eq. (117)] are of interest because this Hamiltonian is simple enough to permit exact calculations, without further approximations of the kind familiar in most of radiation theory. For example, the expression for quantum inversion in Eq. (119a) has the following unusual properties:
1.	it is not restricted to any finite range of t values;
2.	it holds for all values of the coupling constant λ, which is contained in χ(n)=2λ√n;
3.	it is completely free of decorrelations, such as the
commonly used approximation ;
4.	it is finite even at exact resonance (ω21 =ω) without the aid of ad hoc complex energies;
5.	it is fully quantum mechanical with nontrivialcommutators preserved: [a,a†]=1,[σ,σ†]=2σz, etc; and
6.	it is realistically nonlinear (it saturates because theatomic energy cannot exceed E2).
This combination of properties is unique in atomic radiation theory. They indicate, for example, that a system obeying Hamiltonian [Eq. (117)] would permit some fundamental questions in quantum electrodynamics to be studied independently of the restrictions of the usual perturbation methods that are based on short-time expansions and a small coupling constant. Experimental realization of the model is unlikely in the optical frequency range because of the restriction to a single radiation mode. However, quantum optical techniques, including the detection of single photons, are rapidly being extended to much lower frequencies, where single-mode cavities can be built. Observation of the Jaynes–Cummings model is expected to play a guiding role in microwave single-mode experiments with Rydberg atoms.
E. AC Stark Effect and Resonance Fluorescence
Just as the Bloch vector provides a powerful descriptive framework for a wide variety of quantum optical phenomena, so does the Jaynes–Cummings model. The Hamiltonian [Eq. (117)] can be regarded as a zero-order approximation to a “true” Hamiltonian, in which the atom is allowed more than two levels or the field has more than one mode. It is an unsual zero-order approximation because it includes the interacting Hamiltonian as well as the noninteracting atomic and radiation Hamiltonians.
If the atom interacts resonantly with a single strong mode of the field, then its interactions with other modes, perhaps involving other levels of the atom, can be treated approximately. The energy spectrum of the Jaynes– Cummings Hamiltonian makes it clear how this can be done. In Fig. 11 the RWA energy spectrum is shown in the absence of a strong resonant interaction (i.e., with λ=0), and also with  0. The spectrum shows that the state |n , which corresponds to the atom in its lower level and n photons in the mode when λ=0, is pushed down to become the state  when  0. That is, for
Eq. (118a) we obtain
	En, .	(120)
Since n  , the lower level is pushed down. Similarly, the corresponding upper state  is pushed up by the sameamount.ThisshiftiscalledtheACStarkshiftbecause
 
Quantum Optics 
it is due to the interaction with an oscillating (alternating) electric field. The size of the AC Stark shift δAC varies as a function of   in the range
	   	(121)
depending on whether the atom and the field mode are near to or far from resonance.
An external probe of the coupled two-level plus singlemode system can reveal these details of its spectrum.
For example, the two nearly degenerate states   and   are split by twice the AC Stark shift. This splitting can be observed by absorption spectroscopy if a weak secondradiationfieldisallowedtoinducetransitionstoathird level in the atom. This was first described and observed in 1955 by Autler and Townes.
A different kind of probe is provided by resonance fluorescence, that is, by spontaneous emission into modes other than the main mode. In this case a strong laser field provides the main mode radiation. Dipole selection rules determine that from the same nearly degenerate states   and   spontaneous transitions can be made only to the next lower pair of nearly degenerate states,
n   1,−. There are four separate emission lines predicted, as shown in Fig. 11. The strengths of the four lines are all equal on resonance, but since two of them have the same transition frequency only three lines are actually expected. They have the intensity ratio 1:2:1, but the side peaks have different widths than the center peak, and the peak height ratio is 1:3:1. This fluorescence triplet was predicted in the late 1960s, and after a period of controversy about the exact line structure, the predictions mentioned here were verified experimentally in the mid-1970s by Stroud, Walther, Ezekiel, and others. It should be clear from Fig. 11 that the resonance flu-
 
FIGURE 11 Jaynes–Cummings RWA energy spectrum.
 
FIGURE 12 Resonance fluorescence spectra in the presence of AC Stark splitting. [Reprinted with permission from Hartig, W., Rasmussen, W., Schieder, R., and Walther, H. (1976). Study of the frequency distribution of the fluorescent light induced by monochromatic radiation. Zeitschrift fu¨r Physik A278, 205–210.]
orescence peak separation is equal to the Autler–Townes splitting,whichisjustthequantumRabifrequencyχ(n)at resonance. The sequence of spectra shown in Fig. 12 illustrates the increased peak separation that accompanies an increased Rabi frequency when the main mode intensity is increased.
F. Tests of Quantum Theory
It has long been recognized that quantum theory stands in conflict with naive notions that “physical reality” can be independent of observation. As is well known, the Heisenberg uncertainty principle mandates a limit on the mutual precision with which two noncommuting variables may be observed. This curious feature was put into sharp focus by Einstein, Podolsky, and Rosen in 1935, but for nearly half a century it remained mainly of philosophical interest, as experimental tests were difficult to conceive or implement. The situation changed dramatically during the 1970s when it was realized that quantumopticalexperimentscouldtestdifferentconceptionsof
“reality.”
Einstein, Podolsky, and Rosen (EPR) gave a precise meaning to the concept of reality in this context: “If, without in any way disturbing a system, we can predict with certainty [i.e., with probability equal to unity] the value of aphysicalquantity,thenthereexistsanelementofphysical reality corresponding to this physical quantity.” It was of primary concern to EPR whether quantum theory can be considered to be a “complete” theory. A necessary conditionforcompletenessofatheory,accordingtoEPR,isthat “every element of the physical reality must have a counterpart in the physical theory.” Using these definitions of reality and completeness, and the properties of correlated quantum states, EPR concluded that quantum theory does not provide a complete description of physical reality.
An illuminating example due to Bohm is provided by the singlet state of two spin  particles:
 ,
(122)
where |a  is the state for which particle a has spin up (+) or down (−) in the direction nˆ. The unit vector nˆ can point in any direction. In light of the EPR argument, one notes that the spin of particle b in, say, the xˆ direction, can be predicted with certainty from a measurement of the spin of particle a in that direction. If the spin of particle a is found to be up, then the spin of particle b must, for the singlet state, be down, and vice versa. Thus, the spin of particle b in the xˆ direction can be predicted with certainty “without in any way disturbing” that particle. According to EPR, therefore, the xˆ component of the spin of particle b is an element of physical reality.
Of course, one may choose instead to measure the yˆ component of the spin of particle a, in which case the yˆ component of particle b can be predicted with certainty. It follows therefore that both the xˆ and yˆ components of the spin of particle b (and, of course, particle a) are elements of physical reality. However, according to quantum mechanics, the xˆ and yˆ components of spin cannot have simultaneously predetermined values, because the associated spin operators do not commute. Therefore, quantum theory does not account for these elements of physical reality, and so, according to EPR, it is not a complete theory.
The EPR experiment can be criticized on the ground that “the system” must be understood in its totality and cannot refer to just one of the particles, for instance, of a correlated two-particle system. In the Bohm gedanken experimentjustconsidered,ameasurementonparticleadoes disturb the complete (two-particle) system because the quantum mechanical description of the system is changed by the measurement. One cannot consistently associate an element of physical reality with each spin component of particle b, even though the particles may be arbitrarily far apart and not interacting in any way.
Motivated by the EPR argument, one may ask whether it is possible to formulate a theory in which physical quantities do have objectively real values “out there,” independently of whether any measurements are made. Theseobjectivelyrealvaluesmaybeimaginedtobedetermined by certain hidden variables which may themselves be stochastic. One can ask, is it possible, in principle, to construct a hidden variable theory in full agreement with the statistical predictions of quantum mechanics, but which allows for an objective reality in the EPR sense?
In the early 1960s Bell considered the most palatable class of hidden variable theories, the so-called local theories. He demonstrated that such theories cannot fully agree with quantum mechanics. In particular, certain Bell inequalities distinguish any local hidden variable theory from quantum mechanics. Another way of stating “Bell’s theorem” is that no local realistic theory can be in full agreement with the predictions of quantum theory.
Bell inequalities are not difficult to derive for the Bohm thought experiment. A local hidden variable theory is postulatedtogive  foreachspincomponent,asdetermined by the hidden variables. The theory is also supposed to account for the spin correlations: if one is up the other must be down. The difference between such a theory and quantum mechanics is that the spins are predetermined (by the hiddenvariables)beforeanymeasurement,thatis,theyare objectively real. The condition of locality enters through the additional assumption that a measurement of the spin of each particle is not affected by the direction in which the spin of the other particle is measured. This is certainly reasonable if all the spin components are predetermined, since the two particles may be very far apart when a measurement is made.
The question now is whether any measurements can distinguish such a theory from quantum mechanics. Bell considered E(mˆ ,nˆ), the expectation value of the product of the spin components of particles a and b in the mˆ and nˆ directions, respectively. He obtained the inequality
	 ,	(123)
which must be satisfied by the entire class of local hidden variable theories. This inequality is violated by quantum theory, as can be seen from the quantum mechanical prediction E(mˆ ,nˆ) mˆ ·nˆ. It is therefore possible to test experimentally the predictions of quantum theory vis-a`vis the whole class of plausible “realistic” theories.
Although Bell’s theorem promoted philosophical questions about hidden variables to the level of experimental verifiability, it remained difficult to conceive of specific experiments that could be undertaken. In 1969, however, Clauser and co-workers suggested that Bell inequalities
Quantum Optics
could be tested by measuring photon polarization correlations if certain additional but reasonable assumptions about the measurement process were made. The spin considered by Bell is replaced by photon polarization, another two-state phenomenon. Correlated two-photon polarizationstatesareproducedinatomiccascadeemissions, and efficient polarizers and detectors are available for optical photons.
Consider a J =0 → 1 → 0 atomic cascade decay, with polarizer–detector systems on the ±z axes. Linear polarization filters may be employed to distinguish the photons by their energy so that each polarizer–detector system records photons of one frequency but not the other. Itmaybeshownthatthetwo-photonprolarizationstatehas the form
 
where  is the single-photon state in which photon a is linearly polarized along the xˆ direction, etc. A similar form applies if a circular polarization basis is used.
The correlated photon state of Eq. (124) is obviously analogous to the spin-  correlated state of Eq. (122). A hidden variable theory of such polarization correlations leads to a Bell inequality analogous to Eq. (123):
	|E(α,β) − E(α,γ)| ≤ 1 − E(β,γ),	(125)
where E(α,β) now refers to photon polarization components and α and β are the filter orientations with respect to some reference axis. The differences between Eqs. (125) and (123) arise because we are now dealing with spin-one particles and because Eq. (124) describes a positive correlation. The quantum mechanical prediction for E(α,β) is simply cos 2(α −β), and Eq. (125) becomes
 ,
(126)
which, in fact, is not satisfied for all angles α, β, and γ. Such violations of Bell inequalities have been observed in independent experiments led by Clauser, Fry, and Aspect. The results of such experiments are in agreement with quantum theory, and appear to rule out any local hidden variable theory. There are possible loopholes in the interpretation of the experiments, but at the present time none of them seem very plausible. According to Clauser and Shimony, “The conclusions are philosophically unsettling: Either one most totally abandon the realistic philosophy of most working scientists, or dramatically revise our present concept of space–time.”
From the viewpoint of quantum optics, the photon polarizationcorrelationexperimentsmeasureasecond-order field correlation function. Such a correlation function not only distinguishes between classical and quantum radiation theories, but also between quantum theory and local realistic theories. In quantum optics it is often possible to address such questions from essentially first principles and to carry out accurate tests of theory in the laboratory.
V. RECENT DEVELOPMENTS
A. Substantial Squeezing
In Section III.B the first observation of a squeezed state of light was mentioned. Since then, considerably greater degrees of squeezing have been reported. As much as a 60%noisereductionhasbeenobservedusingathree-wave parametric down-conversion technique, in which a photon of frequency ω is converted into two photons of frequency ω/2 in a crystal.
B. Two-Photon Correlated Quantum States
Studies of photon coherence and interference have entered a new domain with experiments being undertaken on new types of two-photon quantum states, going beyond thedetectionoftwo-photonpolarizationcorrelationsmentioned in Section IV.F. For example, quantum beats have been observed in the joint probability of two-photon detection as a function of the path difference and frequency difference of two photons produced by parametric down conversion.
C. Cavity QED in the Optical Domain
Despite our prediction to the contrary at the end of Section IV.D, experimental observations of effects associated with the single-atom single-mode Jaynes–Cummings quantum model have been successful in the optical domain, as well as at microwave frequencies. Collapse and revival signals (see Fig. 10) have been reported in experiments using rubidium atoms traversing a microwave cavity, and optical observations of line-narrowing below the free-space limit and cavity line-spilitting have been reported.
D. Two-Photon Laser
After more than two decades of theoretical interest, substantial experimental progress toward the realization of a two-photon laser is occurring. A two-photon laser has many fundamental differences with the conventional onephoton laser, including special noise properties, multistability, and a different phase transition at threshold. An important step has been the successful operation of a quantum oscillator working on a microwave two-photon Rydberg transition in rubidium.
E. Strong-Field Quantum Optics and Atomic Continuum States
According to the considerations of Section II.F, ionizing transitions should be immune to saturation. Since the continuumofstatesabovetheionizationthresholdisinfinitely broad (β → ∞), no finite χ should satisfy Eq. (47). This has turned out not to be true. New laser systems which deliver 0.01–1.0 terawatts (1 terawatt =1012 W) in 1 ps (or shorter) pulses have been used in multiphoton atomic ionizationexperimentsthathaverevealednewphenomena for which saturation and other quantum optical concepts seen unexpectedly appropriate. These phenomena include equallyspacedmultiple-peakedphotoelectronspectraand anomalously strong very high-order harmonic generation (above 30th order).
F. Cooling below the Doppler Limit
Resonant excitation of two-level atoms can give rise to center of mass motion as well as internal transitions, and various schemes for trapping and cooling collections of atoms by laser light are based on this. The spontaneous line-width  of the transition places a so-called Doppler limit kT =h/2 on the lowest temperature T that can be reached. However, it has been realized that multilevel atoms allow this limit to be evaded, and much lower temperatures, in the neighborhood of 50 µK (0.000050 degrees absolute) have now been recorded.
G. Teleportation
One key consequence of the violation of the Bell inequality is to establish the nonlocality of quantum mechanics. Modern quantum optical techniques permit nonlocality to be exploited when one “teleports” a quantum state, and teleportation has been demonstrated in several laboratories. Teleportation here means to send an ideally exact copy of a quantum state localized at the sender (familiarly called Alice) to a remote site (where the operator is known as Bob). Teleportation is not in conflict with the “no cloning” theorem because the original state to be teleported is lost in the process, so twins are never created.
We will discuss teleportation of the polarization state of a photon labeled 1 in Alice’s control. We write the photon state as:
 , where|a|2 + |b|2 = 1,
where H and V refer to horizontal and vertical polarization, respectively (or any pair of crossed polarization directions). Two more photons, labeled 2 and 3, are used to teleport this state. They need to be arranged in a Bellcorrelated state, for example
 ,
as described in Section IV.F. Photons 2 and 3 are “shared” inthesensethat2isdirectedtoAliceand3toBob,butBob and Alice know only that they are sharing a Bell pair and nothing about its specific nature. Thus this illustration of teleportation starts with a three-photon quantum system, whose state  is the tensor product of the state to be teleported and the Bell state:  .
The process of teleportation is easily unraveled in the Bell basis of entangled two-photon states. The Bell basis for the product space of particles 1 and 2 is the following four states labeled A, B,C, D:
 ,
 ,
 ,
 .
It is not hard to check that our three-photon state , can be written:
 .
Alice starts the process by performing what is called a Bell measurement on the two photons available to her (1 and 2). In doing this Alice collapses the three-photon jointly held state  to one of the Bell components. Next Alice calls Bob on the telephone to tell him which component. This signals Bob to make not a measurement but a unitary transformation on the state of the photon he has received, photon 3. The transformation he makes is determined universally by the following teleportation table:
Alice’s Bell-state projection	Bob’s unitary operation needed
 
	 	i 
 
This table is constructed so that, after Bob performs the indicated unitary transformation, particle 3 is in the state
Quantum Optics
. Note that this is the same as the original state of particle 1, and the teleportation is complete. The reader can check this by choosing the state 3 partner of any one of the Bell components in  and performing the rotation indicated by the table.
At this point Bob has the original state while Alice has the entangled Bell pair resulting from her Bell projection, but nothing of her original state of photon 1. The original state is destroyed in the process of teleporting it. Alice’s inability to know in advance which entangled Bell state will result from her Bell measurement is mirrored in Bob’s uncertainty about the unitary operation (polarization basis rotation) required of him before receiving Alice’sphonecall.Thisuncertaintynecessitatesthephone call, and this eliminates any imagined superluminal aspect of the process. The locations of Alice and Bob are irreleventtotheprocessandtheymaybeseparatedbyagreat distance.
SEE ALSO THE FOLLOWING ARTICLES
ATOMIC AND MOLECULAR COLLISIONS • ELECTROMAG-
NETICS • LASERS • NONLINEAR OPTICAL PROCESSES •
OPTICAL INTERFEROMETRY • QUANTUM THEORY
BIBLIOGRAPHY
Allen, L., and Eberly, J. H. (1975). “Optical Resonance and Two-Level Atoms,” Wiley, New York, reprinted by Dover (1987).
Bennett, C. H., Brassard, G., Crepeau, C., Jozsa, R., Peres, A., and Wooters, W. K. (1993). Phys. Rev. Lett. 70, 1895.
Boschi,D.,Branca,S.,DeMartini,F.,Hardy,L.,andPopescu,S.(1997). Phys. Rev. Lett. 80, 1121.
Bouwmeester, B., Pan, J. W., Mattle, K., Eibl, M., Weinfurter, H., and Zeilinger, A. (1997). Nature 390, 575.
Delone,N.B.,andKrainov,V.P.(1985).“AtomsinStrongLightFields.” Springer-Verlag, Berlin.
Fontana, P. (1982). “Atomic Radiative Processes,” Academic Press, San Diego.
Furusawa, A., Sorenson, J., Braunstein, S. L., Fuchs, C. A., Kimble, H. J., and Polzik, E. S. (1998). Science 282, 706. Knight, P. L., and Allen, L. (1983). “Concepts of Quantum Optics,” Pergamon, Oxford.
Knight, P. L., and Milonni, P. W. (1980). The Rabi frequency in optical spectra. In “Physics Reports,” Vol. 66, pp. 21–107. North-Holland, Amsterdam.
Loudon, R. (1983). “The Quantum Theory of Light,” 2nd ed. Oxford Univ. Press, Oxford, UK.
Mandel, L. (1976). The case for and against semiclassical radiation theory. In “Progress in Optics” (E. Wolf, ed.), Vol. XIII. North-Holland, Amsterdam.
Milonni, P. W. (1976). Semiclassical and quantum-electrodynamical approaches in nonrelativistic radiation theory. In “Physics Reports,” Vol. 25, pp. 1–81. North-Holland, Amsterdam.
Perina, J. (1984). “Quantum Statistics of Linear and Nonlinear Phenomena,” D. Reidel, Dordrecht.
Rosen, H. J., and Gustafson, T. K. (eds.) (1989). Quantum electronic applications and optical studies of high-Tc superconductors. Quantum Electron 25(11), 2357–2409.
Stenholm, S. (1984). “Foundations of Laser Spectroscopy,” Wiley, New York.
Yoo, H. I., and Eberly, J. H. (1985). Dynamical theory of an atom with two or three levels interacting with quantized cavity fields. In “Physics Reports,” Vol. 118, pp. 239–337. North-Holland, Amsterdam.
 
 
Quantum Theory
David W. Cohen
 
Smith College
I.	The Classical Setting
II.	Blackbody Radiation: The Birthof Quantum Theory
III.	Early Evolution
IV.	The Bohr Atom
V.	Transition to Quantum Mechanics
VI.	After Quantum Mechanics: ModernDevelopments in Foundations of Quantum Physics
VII.	An Advantage of Uncertainty: Quantum
Computing
GLOSSARY
Continuous Pertaining to a variable that can assume all values from a specified continuum.
Continuum Interval of real numbers, possibly unbounded.
Discrete Pertaining to a set of numbers in which every member is isolated from the others in the set by an open interval. Also pertaining to a variable that can assume only values from a specified discrete set of numbers.
Macroscopic Pertaining to physical phenomena occurring on a scale large enough to be observed without the aid of a microscope.
Quantum Quantity of energy.
A QUANTUM THEORY is a system of explanations of physical phenomena based on the assumption that certain quantities can assume only a discrete set of numerical values. The first formulation of a quantum theory was presented in 1900 by Max Planck to explain results of experiments that measured light radiating from a heated body. Planck broke a tradition of classical physics by assuming that energy was a discrete variable in one situation in which it had always been considered continuous. He introduced two other ideas that also may be considered hallmarks of a quantum theory. One was the hypothesis that discrete quantities of energy (energy quanta) can be treated as objects, like particles, subject to statistical laws of distribution—a foreshadowing of the merger of wave theory and particle theory. The second was the introduction of a new constant to the general laws of physics.
 	441
Between 1900 and 1925 there emerged the quantum theories of blackbody radiation, light, specific heat, and atomic energy, among others. This is the body of physics commonly called the quantum theory. Beginning in 1925 all of these theories, as well as the formulation of the philosophical questions behind them, were merged into one mathematical formalism called quantum mechanics.
Our discussion of the quantum theory will trace the mainideasinchronologicalorderfromtheclassicalsetting in the 19th century through the birth of quantum mechanics in 1925. Then we will look at some of the controversy surrounding the modern theoretical foundations of quantum mechanics. And finally we will look at an example of how the probabilistic view of nature arising from quantum theory might actually be used to advantage to build highspeed quantum computers. In our discussions we won’t hesitate to paraphrase original ideas and substitute modern notation when it’s necessary for clear understanding.
I. THE CLASSICAL SETTING
Inthissectionwereviewtheclassicalphysicsthatweshall need for our discussion of quantum theory.
A. Physical Laws and Variables
One of Sir Isaac Newton’s key contributions to science in the 17th century was the concept of the physical law. He codified events, like the fall of an apple, into a system of words and mathematical expressions that brought such order, clarity, and economy to thought that he was able to reveal hidden relationships among the events. In fact, Newton’s laws provided experimenters with the means to predict with uncanny certainty how some events would affect the future.
The success of the predictive value of Newton’s laws was so great that it became a universally accepted principle of science that it is possible, in theory, to determine simultaneously the values of all physical quantities associated with a given physical event and with those values predict, with 100% certainty, all future events caused by thefirst.Weshallseelaterhowquantumtheorychallenged this principle, but first let us examine the law of Newtonian mechanics that we shall need for our discussion. We use modern terminology.
Let us call a physical quantity fundamental if its values are determined by comparing measurements of the quantity against some arbitrarily selected standard. Examples of such quantities are periods of time (measured in seconds, perhaps) and length (measured in meters, feet, etc.). Weshallcallderivedquantitiesthoseobtainedfromfundamentalquantitiesbymathematicalcalculations.Examples of these are instantaneous velocity and acceleration.
One fundamental quantity defined by Newton is the mass of an object. Mass measures the resistance of objects to acceleration. An object used to determine a standard valueofmass,1kg,iskeptinavaultinParis.Wecandefine a derived quantity, force, by setting particles of known massintomotion.Whenanobjectofmassm isaccelerated fromrest,alongastraightline,toanaccelerationa,wesay the force F causing the acceleration acts in the direction of the motion and is given by
	F = ma.	(1)
Noticethatforce,likeacceleration,isdescribedintermsof direction, and so it is a vector quantity. The magnitude of force necessary to accelerate 1 kg of mass to a magnitude of 1 m sec−2 is called 1 newton (N). Equation (1) is a formulation of Newton’s second principle of motion.
Let us look more closely at the meaning of Eq. (1). We think of the letters in the equation as place holders for numbers.Thatis,ifweassignnumberstotwooftheletters, we can manipulate the equation to compute the number that must be assigned to the third letter, if the equation is to be true. So we call the letters variables. A variable in an equation is called continuous if the numbers that can be assigned to it comprise an open (possibly unbounded) interval. For example, if we assume that we can accelerate an object of given mass to any magnitude of acceleration between values −x and x, then the variable a in Eq. (1) is continuous with domain of assignability (−x, x).
Some variables, however, can be assigned values only from a discrete set of numbers. A set of numbers S is called discrete if every number in S belongs to an open interval that contains no other members of S. The set of integers, for example, is a discrete set of numbers. In the equation cos2Nπ =1, the set of values for N for which the equation is true can come only from the set of integers. Thus, N is a discrete variable in that equation.
The word discrete, as we have defined it, is relatively modern. Physicists traditionally have used the word discontinuous instead. One of the revolutionary ideas of quantum theory was the assumption of the discontinuity of some variables that had always been considered continuous in classical physics.
B. Mechanical Energy
Energyisthecapacitytodowork.Wepresenthere,briefly, the classical definitions of potential and kinetic energy for a particle moving in a field of force.
Let R denote a region of three-dimensional space and suppose that at every point p in R there is a threedimensional vector F(p) assigned to that point. We call F avectorfield.Supposealsothat f isareal-valuedfunction on R, that ∇f is its gradient, and that
	F(p) = −∇f (p)	(2)
foreverypoint p of R.Anyfunction f thatsatisfiesEq.(2) is called a potential function for F. If F(p) represents a force at every point p, we call F a force field.
If γ is any differentiable path in R from point p =γ(a) to point q =γ(b), and if f is a potential function for force field F, then we define the work done by moving a particle along γ through force field F by the line integral
	W .	(3)
The work depends only on the end points of the path, and not on γ itself. We can express this by the equations
	 ,	(4)
which can be proved using Eq. (2).
We have, then, that f (q)− f (p) is the work done if we move a particle through force field F from point p to point q. Since any two potential functions for F must differ only by a constant, that amount of work can be calculated from Eq. (4) using any potential function for F. We call that amount of work the potential energy difference between point p and point q.
Itispossibletodefineanabsolutepotentialenergyfunction PE by selecting any point s in R and deciding what the potential energy P is to be at the point. Then for any potential function f for F, we can define the potential energy at every point p to be
	PE(p) = P + f (p) − f (s).	(5)
This function PE differs from f by a constant, so it is a potentialfunctionfor F,anditsdefinitiondoesnotdepend on the choice for f .
An example of a potential energy function arises when a particle moves about R, all of three-dimensional space, in a field of a force of attraction between the particle and the point O at the origin of R. The potential energy can be negative at every point p, with large negative values near O andthepotentialenergyapproachingzeroatpointsvery far from O. Then to move the particle from a distant point p along a straight line toward O to a point s closer to O
requiresnegativework,becauseitismovementinthesame direction as the force exerted by the field. This results in a change of potential energy from one negative value to a more negative value, which is considered a decrease in potential energy. As we shall see, an electron in an atom is subject to a potential energy function of this type.
Now let us consider kinetic energy. A force field F that satisfies Eq. (2) for some potential function f is called a conservative force field. A particle placed in a conservative force field and allowed to react solely to the force exerted by the field will move from point to point, always in the direction of decreasing potential energy. During the motion, we ascribe to the particle at each point p a kinetic energy defined by
	KE(p) = mv(p)2/2,	(6)
wherem isthemassoftheparticleandv(p)themagnitude of the velocity of the particle when it is at point p. The kinetic energy is equal to the amount of work that must be done to accelerate the particle from a state of rest to a state of motion with velocity of magnitude v(p).
The law of conservation of energy states that, throughout the motion of the particle, the total energy
	E(p) = PE(p) + KE(p)	(7)
has the same value for every point p.
A useful example is that of the kinetic energy of a particle of mass m rotating at constant speed in a circular orbit of radius r. Suppose that at every point the particle is subject to a force toward the center of the orbit of magnitude F and that its velocity at every point has magnitude v. It follows from some routine calculations that at each point the particle is subject to an acceleration toward the center of the orbit of magnitude a =v2/r. Then we have from Eq. (1) that F =ma =mv2/r, so that we can obtain the kinetic energy of the particle at every point in its orbit as
	KE .	(8)
Later, we shall make use of this equation.
C. Electromagnetic Energy
In the late 19th century James Clerk Maxwell combined theories of electricity and magnetism into a theory of electromagneticfields.Suchafieldisaregionofspaceatevery pointofwhichisavectorofelectromagneticforcethatacts on any charged particle placed at the point. The work done as the force moves the particle is a measure of the electromagnetic energy of the field. Such fields surround every charged particle, and if a charged particle is accelerated, some of the field surrounding it leaves the vicinity of the particle and travels off into space. We call this traveling field a wave of electromagnetic radiation. We can measure the energy of the radiation by measuring the work the wave can perform in moving a charged particle placed in its path.
It will not be necessary for our discussion of quantum theory to examine the quantitative relationships involved with electromagnetic theory, but it is important to know that these relationships, known as Maxwell’s equations,requirefieldsofelectromagneticforcetobecontinuous vector fields. Electromagnetic energy calculated from Maxwell’s equations is necessarily a continuous variable.
D. Entropy
Entropy was originally defined as a measure of the relationship between temperature and energy. The total mechanical energy due to the motion of the molecules in a given substance is called the thermal energy of the substance. Some of this thermal energy can be made to do work if the substance is allowed to cool.
In the early part of the 19th century Sadi Carnot provided a theoretical model of an engine that transforms a fall in temperature of a substance into mechanical energy. Some years later Rudolf Clausius and William Thomson (Lord Kelvin) observed the following about Carnot’s engine: Of the total difference in thermal energy resulting from a drop in temperature from T1 (degrees Kelvin) to T2 in a Carnot engine, only the fractional portion 1−T2/T1 can be transformed into mechanical energy to do work, even under the most ideal theoretical conditions. The remaining portion of energy is redistributed in the substance oftheengine.Notethatnoworkcanbeobtainedfromthermal energy without a strict decrease in temperature.
The principle of Carnot’s engine applies to a gas at temperature T1 occupying a volume V1 and exerting pressure P1 on the walls of its container. Let us say that this gas is in amacroscopicstatew1 =(P1, V1,T1).Supposewewishto change the state of the gas to w2 =(P2, V2,T2). We could, if we wished, change states without changing temperature by allowing the gas to expand slowly against one movable side of its container, decreasing pressure and increasing volume. Since work, or mechanical energy, is obtained from this process (assuming the side resists movement), we can add thermal energy to the gas to counteract the temperature drop necessary to supply the work. On the other hand, we could, at least theoretically, allow the gas to expand in a vacuum, increasing volume without changing pressure. In this case, no work is done and temperature canremainconstantwithoutanadditionofthermalenergy. The first type of change from w1 to w2, requiring an addition (or subtraction) of thermal energy, if temperature is to remain constant, is called a reversible change of state.
Now suppose we wish to pass in tiny reversible incremental steps w1,w2,...,wn from some initial state w1 to some final state wn. Denote by	Ek the change in thermal energy for the gas as it goes from state wk to wk+1. Now consider the number
n
	Ek
	S(w1,wn) =	 .	(9)
Tk
k=1
Clausius proved that for reversible changes of state, the sum of Eq. (9) depends only on w1 and wn and is independent of the sequence used in changing from the initial tothefinalstate.Hecalledthisintrinsicdifferencebetween the two states a difference in the entropy of the gas. Notice that,aswithpotentialenergy,wedonothaveavalueforthe absolute entropy until we assign a value to one state.
The theory of entropy was eventually extended to physical systems other than fixed amounts of gas. A physical system can consist of a mixture of gases or particles of different kinds, or a region of space containing items of unknown nature. Even the entire universe can be considered a giant physical system. Extending the theory of entropy was not easy. Among the most difficult tasks was assigning meaning to the notion of the “state” of various physical systems. We shall return to that problem later, but let us continue our discussion of entropy supposing that “states” have been defined.
Asinthetheoryofgases,changesinthestateofaphysical system can be classified as reversible or nonreversible. If we consider a sequence w1,w2,...,wn of reversible changes in state for a system at absolute temperature T, as we did to obtain Eq. (9), then the incremental change in entropy from state wk to wk+1 is denoted
		Sk =	Ek/T,	(10)
where	Ek is the incremental change in the total energy of the system.
We examine our next step carefully. It reveals an assumption taken so much for granted in the physics of the 19th century that it was seldom, if ever, explicitly discussed then. The challenge to that assumption was at the very heart of quantum theory in the early 20th century.
We have in Eq. (10) a relationship between differences in entropy and differences in energy. For a gas in a controlledexperiment,precisevaluesforthesedifferencescan be measured. If we assign a particular value of entropy to a particular value of energy in an experiment, it is possible to use Eq. (10) to write an explicit relationship between absolute entropy and energy at temperature T for states w1,w2,...,wn:
	Sk = Ek/T.	(11)
Next comes the assumption. We assume that the states w1,w2,...,wn were chosen from a continuum of states so that Eq. (11) provides a discrete set of values in what is really a continuous, in fact, differentiable function of entropy in terms of energy. Time and again physicists identified one physical quantity as a function of another one, and assumed that the functional relationship was continuous and that the ability to measure arbitrarily small differ-
ences in the quantities was limited only by the ability to build arbitrarily precise and accurate measuring devices. Although this assumption will be reexamined in our discussion of quantum theory, it allows us to take our next step to obtain an expression involving entropy that we shall need in the sequel.
We rewrite Eq. (10) as	Sk/	Ek =1/T and use our assumption to pass to infinitesimally small incremental changes to obtain an expression for the derivative of entropy with respect to energy:
	dS/dE = 1/T.	(12)
This equation was a basic building block in the original construction of the quantum theory.
E. Specific Heat
As we mentioned in the preceding section, the thermal energy of a substance is transformed into mechanical energy when the substance undergoes a drop in temperature. Conversely, energy supplied to a substance can raise its temperature. Let us consider cases in which a substance does not change pressure (if it is a gas) or volume while it undergoes changes in temperature.
Throughout the 19th century experiments were performed to determine the amount of energy required to raise fixed amounts of various substances one degree on a temperature scale. It was discovered that the relation between the amount of energy added to a substance and the resulting rise in temperature depends not only on the material of the substance but also on the temperature of the material during the addition of energy.
Let us consider a fixed substance. Consider a sequence
T1,...,Tn of temperatures. Denote by	Tk the change in temperature from Tk to Tk+1, and by	Ek the corresponding change in thermal energy of the substance. Now we define the heat capacity of the substance at temperature Tk as
	C(Tk) =	Ek/	Tk.	(13)
Usingtheassumptionofdifferentiabilitymentionedinour discussion of entropy, we can then pass to infinitesimally small increments in Eq. (13) to arrive at the definition for the heat capacity of the substance at temperature T as
	C(T) = dE(T)/dT.	(14)
The specific heat of a substance at temperature T is definedasitsheatcapacityperunitmass.Thus,asubstance of mass m has specific heat at temperature T given by
	c(T) = C(T)/m.	(15)
Although we have defined heat capacity and specific heat as functions of temperature, one often hears a phrase such as “the specific heat of copper” without mention of temperature.Thatisbecausethevaluesoftheheatcapacity of most substances are nearly constant over a range of room temperatures, and it is this constant value that is often called the heat capacity of the substance.
F. Boltzmann Statistics
In the late 19th century Ludwig Boltzmann undertook the task of providing a more precise relationship between changes in mechanical motions of molecules and changes in entropy. His theory rested on notions of distributing numbers according to laws of probability, and this notion was a key inspiration to the developers of quantum theory. Let us consider a gas in a closed container and the macroscopic states of the gas defined as w =(P, V,T) when the gas is at pressure P, volume V, and temperature T. We shall restrict our attention to changes in macroscopic state due solely to changes in temperature, leaving pressure and volume fixed. Consider one macroscopic state w, and suppose that the gas consists of N molecules, each with a specific energy, and that in state w the total thermal energy of the gas is E.
Next we shall partition the real-number interval [0, E] into p subintervals J1,..., Jp, each of length ε = E/p. We then assign each of the N molecules to one subinterval according to the amount of energy it has. For a given assignment we consider a p-tuple of numbers (l1,...,lp), whereli isthenumberofmoleculesassignedtosubinterval Ji. We call such a p-tuple a microscopic state of the gas. For example, ifl1 = N andl2 =l3 = ··· =lp =0, then the gas is in microscopic state (N,0,...,0), and we can write the total energy of the gas as E = pε ≈ Nε =l1ε. The approximation follows since all N molecules have energy values in interval J1, which has the number ε as an end point. So each molecule has energy approximately equal to ε. For an arbitrary microscopic state (l1,...,lp), we have an approximation of E given by
p
	E  li xi,	(16)
i=1
where each xi is an arbitrary value in subinterval Ji.
It is assumed that the molecules are distinguishable, so that there are many ways a specific microscopic state can be achieved. In other words, interchanging one of the molecules in subinterval Jm with one in subinterval Jn does not change the microscopic state, which depends only on the p-tuple (l1,...,lp). It can be computed from standard methods in combinatorics that the total number of ways the molecules can be assigned among the subintervals to achieve a given microscopic state (l1,...,lp) is
	W(l1,...,lp) = N!/l1!l2!···lp!	(17)
Now if W(l1,...,lp) is a high number, many assignments of the molecules to the subintervals result in state (l1,...,lp). If it is a small number, few assignments result in that state. The common way to express this in physics is to say that W(l1,...,lp) is the probability for microscopic state (l1,...,lp) to occur. A state where W(l1,...,lp) achievesamaximumvalueisastate“mostlikelytooccur,” and that is called a state of statistical thermal equilibrium.
Another way to describe W is to call it a measure of the “disorder” of the molecules. States highly likely to occur are those having coordinates nearly equal. They are said to be in a state of high disorder. That is why it is often said that entropy is a measure of the disorder of the universe.
Now if we have two systems that we combine into one (e.g., two gases in the same vessel), then an increase in entropy S1 and S2 of the systems individually must result in an increase S1 + S2 of the entropy of the combined system. On the other hand, if W1 is the probability for a given state for one system with entropy S1 to occur, and W2 is the probability for a given state for the other system with entropy S2 to occur, then the probability for the combined system to be in both states simultaneously is the product W1W2. So the relationship between entropy S and the probability W of a microscopic state of a system must be the one that relates multiplication to addition,
	S = k ln W,	(18)
where k is a constant. This is Boltzmann’s key entropy equation,althoughheneverwroteitthisway.Theconstant k, now known as Boltzmann’s constant, was the subject of much research at the beginning of the 20th century.
Observe that, at thermal statistical equilibrium for a given energy, W is a maximum and hence S is also. A macroscopicstateofstatisticalthermalequilibrium,therefore, is a state of maximum entropy for a given energy, and that macroscopic state can occur for many different microscopic states.
Let us conclude our introduction to Boltzmann statistics by mentioning a step that Boltzmann took whenever he applied his calculations. By using the assumption of continuity we discussed in Section I.D, he let the number of subintervals of the energy interval go to infinity and the size of each subinterval go to zero. As we shall see, the success of quantum theory rested on not taking that step.
II. BLACKBODY RADIATION: THE BIRTH OF QUANTUM THEORY
A. The Blackbody Furnace
Particlesabsorbandradiateelectromagneticenergy.Some absorb very little incident radiation (reflectors), and others a great deal (absorbers). Objects can be made to radiate electromagnetic energy when they are heated. We see this when we watch glowing coals in a dying fire, for light is a form of electromagnetic radiation. The most intense energy is radiated by objects that are the best absorbers. A perfect absorber is called a blackbody.
Physicists can simulate a blackbody by building a box and placing a tiny hole in one side of the box. The hole is the blackbody, because nearly all electromagnetic energy falling on the hole will enter into the box and not emerge again. We shall call such a box a blackbody furnace.
Suppose we build such a furnace and heat the interior of it and hold it at constant temperature T (degrees Kelvin). Theparticlesinthefurnace,dust,forexample,andtheparticles making up the walls of the furnace will absorb and radiate electromagnetic energy until the interior reaches a state of equilibrium. That is when each particle is absorbing exactly the same amount of energy it is radiating. In reality, if a tiny bit of radiation energy escapes through the hole, more energy is being emitted than absorbed by some particles, but we can ignore that tiny difference and consider the electromagnetic energy in the furnace to be a field of electromagnetic energy in a state of equilibrium.
We now wish to measure the intensity per unit volume of the electromagnetic energy in the furnace. In practice we can do this by letting a small amount of electromagnetic energy radiate from the box through the hole. When this was done in the late 19th century, it was found that the intensity varied with the temperature T and the frequency ν of the radiation. This can be observed, for example, by shining the light from the furnace through a prism and measuring the intensity of the light at different frequencies. Other variables were considered. For a given temperature and frequency the size and the shape of the furnace were varied. Furnaces were built from a variety of materials, and particles of different materials were placed in the furnaces. None of these changes affected the intensity of the electromagnetic energy, which appeared to depend only on frequency and temperature. Thus, it was hypothesized that there exists an expression I for the energy intensity in a unit volume in the furnace as a function of frequency ν and temperature T that is fundamental to blackbody radiation.
In the late 19th century there began an intense and frustrating search for the function I based on a sound theoreticalmodelandverifiedbyexperiment.Well-knownlawsof classical electromagnetic radiation, thermodynamics, and mechanics were blended together to give formulations for I thatwerepatentlyabsurd.Ontheotherhand,expressions for I extrapolated from experimental data were accurate to various extents but stood wholly without theoretical foundations. The search for an explanation of blackbody radiation led to the birth of quantum theory.
B. The Extrapolated Formulas
Let us begin the search for the function I in the same way it was begun by physicists around the turn of the century: byexaminingexperimentaldata.Forvarioustemperatures T1,...,Tn, we plot the observed values for I(ν,Tk) as a function of ν. Four such plots are illustrated in Fig. 1.
For a specific temperature T, if I(ν1,T) and I(ν2,T) are the energy intensity per unit volume at frequencies ν1 and ν2, respectively, then the total energy intensity in
 
FIGURE 1 Graphs of energy intensity per unit volume as a function of frequency for blackbody radiation in thermal equilibrium at four different temperatures.
a unit volume containing electromagnetic energy of all frequencies between ν1 and ν2 is
	E(T,ν 	(19)
Because the total energy over a range of frequencies (called a spectral range) is given by an integral, I is called a spectral density function. If all frequencies are present, the total energy in a unit volume is
	E dν,	(20)
a function of temperature only. It was an observation of Josef Stefan in 1879 that E(T) was proportional to the fourth power of T. This observation, as well as others gathered from empirical data, became guideposts in the search for a general theory of blackbody radiation, for no theory can gain wide acceptance if it cannot be shown to be in agreement with available experimental evidence.
Another observation we can make from Fig. 1 is that for any given temperature there is a single frequency of maximum intensity, and this frequency depends on the temperature. This characteristic of I(ν,T) is known as the displacementproperty,becauseanincreaseintemperature “displaces” the frequency of maximum intensity farther to the right on the ν axis. In 1894 Wilhelm Wien set down a displacement formula that was verified experimentally by Friedrich Paschen in 1899.
Wien also published an expression for I(ν,T) in 1896, whichagreedwithmuchoftheexperimentaldataavailable at the time. His formula was in the form
	I(ν,T) = aν3 exp(−bν/T),	(21)
where a and b are constants. Soon after it was published, Wien’s formula was found to be inaccurate for low values of ν/T.
Between 1897 and 1900 Max Planck worked on obtaining a better formula, one with a theoretical explanation based on classical principles of physics. No satisfactory explanation had accompanied Wien’s empirical formula [Eq. (21)], and as we shall see in the next section, it was Planck’s search for this explanation that led him to quantum theory.
C. Planck’s Empirical Law
A scientific theory sometimes seems to one who reads about it to be a stroke of genius, and often it is. What the reader does not know, however, is that often the author hadapeekatthe“rightanswer”beforedevelopingthetheory. Such was the case with Max Planck, who presented his theory of blackbody radiation to the Physikalische Gesellschaft in Berlin on December 14, 1900. That is the date often cited as the birthday of quantum theory. We begin our examination of Planck’s theory in the same way he developed it, by peeking at the “right” radiation law, which he himself had found.
Let us suppose that the walls of the blackbody furnace and the particles in the cavity are all composed of tiny linear harmonic oscillators (Planck originally called them resonators) that emit and absorb electromagnetic energy. Using classical laws of thermodynamics and electromagnetism, it can be shown that
	I (ν,T) = aν2E(ν,T),	(22)
where a is a constant and E(ν,T) is the average (over time) of the energy intensity of a typical oscillator vibrating at frequency ν. It would take us too far afield to follow the derivation of Eq. (22), but it is important to note here that the classical laws of electromagnetic energy on which it relies require that the amplitude and energy of the vibrations of a linear oscillator be continuously variable.
If we accept this model of linear oscillators, the search for I becomes a search for E to fit into Eq. (22). Planck used the second law of thermodynamics and a keen intuition for interpolation between formulas known to be successful in different portions of the temperature scale to arriveatanexpressionfor E.Theresult,Planck’sradiation law, is of the form
	E(ν,T) = hν/[exp(Bν/T) − 1],	(23)
where B and h are constants. This formula when placed intoEq.(22),givesexcellentagreementwithexperimentat a wide range of temperatures and frequencies. Convinced that he had the “right” radiation formula, Planck then set aboutfindingtheprecisemechanicalmodelforthefurnace and a theory about how it operated to yield this result.
D. The Quantum Theory of Blackbody Radiation
Ifourbasicassumptionisthatthefurnaceandtheparticles initarecomposedoflinearoscillators,twoquestionsarise immediately: How many oscillators are there, and how are the total radiant energy and total entropy of the furnace distributed among the oscillators?
We shall answer the first question, as did Planck, in the simplest way, by assuming that there are finitely many oscillators for each frequency ν, say Nν. If we write S(ν,T) for the entropy of a linear oscillator in thermal equilibrium at temperature T and frequency ν, and E(ν,T) for its average energy, then we have for the total entropy and total energy of all oscillators having frequency ν
	Stot,ν = NνS(ν,T)	and	Etot,ν = NνE(ν,T).	(24)
Our search for E continues on the basis of a relation between E and S.
IfwesolveEq.(23)for T anduseEq.(12),whichrelates energy to entropy, by writing dS(ν,T)/dE(ν,T)=1/T, we can perform an integration to obtain the entropy for a single oscillator,
	= h	[1 + E(ν,T)/hν]1+E(ν,T)/hν
S(ν,T)	  ln	D,
	B	[E(ν,T)/hν]E(ν,T)/hν
(25)
where D is a constant of integration. We shall return to this equation later.
The next step was described by Planck as “an act of desperation.” He had been a dedicated opponent of Boltzmann’s view that a total amount of energy in a gas was distributed among a finite number of molecules according to laws of probability and combinations. Laws of probability permit exceptions, and Planck thought that such laws had no place in a theory of thermodynamics, which he held to be valid without exceptions. Yet now he saw that such a view point could be taken to move him along toward a derivation of his own radiation law. With a flexibility that often distinguishes the creative genius from the pedant, Planck adopted ideas of Boltzmann that he had previously rejected. Let us continue following Planck’s reasoning.
To obtain discrete quantities of energy to distribute over our oscillators, we divide the total energy Etot,ν into p elements of size ε, so that
	Etot,ν = pε = NνE(ν,T).	(26)
To simplify notation we shall now drop the symbols ν and
T in what follows, bearing in mind that we have N oscillators, all at equilibrium at temperature T and vibrating with frequency ν.
According to Boltzmann’s theory, if a system is in a given microscopic state with probability W, then the total entropy S is proportional to ln W,
	S = k ln W,	(27)
where k is a constant. The task now is to calculate W for our system of oscillators. This will be the total number of ways the p energy elements can be distributed among the N oscillators.Notethat,althoughwearetakingacuefrom Boltzmann,ourapproachdiffersinthatour“states”reflect distributions of p numbers among N oscillators, whereas Boltzmann’s states reflect distributions of N molecules over p intervals of real numbers.
Let us count the possible distributions of energy elementsamongoscillators.Suppose,first,thatoneoscillator is assigned all p energy elements. There are N ways that this distribution could occur. That is each of the N oscillators in turn could be assigned all the energy. Another distribution might be to assign all but one energy unit to one oscillator and the remaining one to another. There are N(N −1) ways to achieve this distribution. It is a routine calculation in combinatorics to show that the total number of ways to achieve all possible distributions is
	W = (N + p − 1)!/p!(N − 1)!	(28)
Since N is very large for practical purposes, one can neglect the subtraction of 1 in Eq. (28) to obtain
	W = (N + p)!/p!N!	(29)
We simplify W further by using Stirling’s formula x!≈xx to obtain
	W = (N + p)N+p/N N pp.	(30)
Wenowhavetwoexpressionsforthetotalentropyofthe system. After an algebraic manipulation using Eq. (25), we obtain the total entropy (for frequency ν and temperature T):
Stot = NS
Nh
	=  	1	ln 1
	B	hν	hν
	 D.	(31)
At the same time we have directly from Eq. (27), using Eq. (30), a bit of algebraic manipulation, and the substitution p/N = E/ε from Eq. (26):
Stot = k ln W
= k[(N + p)ln(N + p) − N ln N − p ln p]
= kN 
 
= kN 
Both Eqs. (31) and (32) give the total entropy contributed by N oscillators. Dividing each by N gives two expressions for the entropy S of a single oscillator in terms of energy E and frequency ν, still at temperature T. How can we make both expressions for S equivalent? The answer is clear. Set h/B =k and set
	ε = hν.	(33)
This last equation provides the key that now allows us to construct a theory to derive Planck’s radiation formula (23). This is the quantum theory.
We begin with the supposition that the furnace is composed of linear oscillators and that, for a fixed frequency, the total entropy contributed by N oscillators in thermal equilibriumwiththatfrequencyisgivenbyEq.(27),where W isinterpretedaccordingtoourdiscussionfollowingthat equation. We then follow the manipulation of Eq. (27), which we used to derive Eq. (32). Setting ε =hν, designating ε as a “quantum” of energy, and then dividing Eq. (32) by N, we obtain the entropy S for a single oscillator in our theory. If we differentiate this expression for S with respect to E, and set the derivative equal to 1/T according to Eq. (12), we then can solve for E. This derivation yields the “correct” radiation law:
	E(ν,T) = hν/[exp(hν/kT) − 1].	(34)
Thus, the quantum theory was born.
When Planck put this formula into Eq. (22) and then integratedoverν toget E(T),heobtainedStephan’sfourth power law and verified Wien’s displacement law, each of which he wrote in terms of the new constant h. Knowing the experimental values for these laws, he was able to compute a value for h:
	h = 6.55 × 10−27 erg sec (energy times time).	(35)
This constant was to emerge at the very heart of many theories of physics throughout the 20th century and, in fact, was to play a crucial role in the fundamentals of quantum mechanics.
III. EARLY EVOLUTION
A. Difficulties with Planck’s Theory
Some of the difficulties with Planck’s theory of blackbody radiation were obvious immediately; others were quite subtle and were not discovered until several years after the presentation of the theory in 1900.
Consider, first, the fuzzy relationship between Planck’s use of probabilism and Boltzmann’s. As we mentioned in Section I.F, after Boltzmann partitioned the energy interval into finitely many subintervals, he later allowed the number of subintervals to approach infinity and the size of each subinterval to approach zero. That was required to apply the classical continuity assumptions he needed in applications of his theory. Planck carefully noted in his address to the Physikalische Gesellschaft in 1900 that his energy quanta ε =hν must not be allowed to tend toward zero. The finiteness of the number of oscillators Nν makes it essential to maintain the finiteness of the number of energy quanta in order to apply the combinatoric procedure associated with Eq. (27).
TherewasanotherdiscrepancybetweenPlanck’stheory and Boltzmann’s statistical mechanics. It had been a generally accepted principle of statistical mechanics that, in an aggregate of oscillators in thermal equilibrium, all with the same number of degrees of freedom, the toal energy of each oscillator must, on average (over time), be distributed equally among its degrees of freedom. This principle was a consequence of what was called the equipartition theorem. If Planck had applied the theorem to his oscillators, then instead of Eq. (34) he would have obtained E(ν,T)=kT and would have arrived at an incorrect radiation law. Planck’s theory violated the principle of equipartition. It is not completely clear whether Planck was even aware of this principle in 1900.
A more fundamental difficulty, a logical inconsistency, was recognized by Albert Einstein in 1905. Planck had originally thought of his partitioning of the total energy into discrete quantities as a mathematical device to obtain numbers to treat with probabilistic arguments. He did not realize until it was pointed out by Einstein that, for his derivation to be consistent, each of his oscillators had to be assumed to be able to absorb and emit energy only over a discrete range of values. On the other hand, Planck’s derivation of Eq. (22) requires that the oscillators be able to absorb and emit energy over a continuum of values. It is therefore inconsistent to put Eq. (32) together with Eq. (22) to arrive at a radiation law.
Despite the difficulties, Planck’s theory of radiation was acknowledged for the accuracy of the formula resulting from it, and history shows that the theory itself revolutionized physics. The “discontinuity” (more accurately, the “discreteness”) of the energy variable and the statistical nature of the behavior of discrete energy quanta were ideas that were to become the foundations of a new and controversial view of the universe.
Albert Einstein, of course, was as important to quantum theory as he was to nearly every other development of physics in the early 20th century. Sometimes a friend and sometimesafoeoftherapidlyevolvingquantumtheory,he made important contributions to it and, merely by paying attention to it, helped to spur the interest of the scientific community. Let us now discuss two ideas of Einstein that were instrumental in placing the “quantum” in the forefront of physics.
B. Einstein’s Theory of Light Quanta
Einstein set forth his theory of light in one of three papers published in 1905. He won the Nobel prize for that paper, and although it is commonly referred to as his paper on the “photoelectric effect,” it really was much more.
Einstein was disturbed by the dualism in physics between particle mechanics and the electromagnetic wave theory of Maxwell. The fundamental difference was the discrete nature of the former as opposed to the continuous nature of the latter. The continuous wave theory of light wasinadequatetoexplainsomeexperimentalphenomena. For example, it was known that ultraviolet light incident on a piece of metal causes electrons to be emitted from the metal. Contrary to electromagnetic wave theory, however, the velocity of an emitted electron does not depend on the intensity (wave energy determined by amplitude) of the
incident light, but instead is a function of its frequency. This phenomenon is known as the photoelectric effect.
One of Einstein’s motives for investigating light was to explain this effect, although his bold explanation was such a violent departure from accepted theory of the wave nature of light that it had implications far beyond consideration of the photoelectric effect. In particular, it had a profound influence on the development of quantum theory, although, ironically, Planck rejected Einstein’s theory of light.
We begin our development of the theory of light by returning to light radiation in the cavity of a blackbody furnace in thermal equilibrium at temperature T. As before, consider the spectral density function I(ν,T), which gives the energy intensity per unit volume in the cavity due to the portion of radiation having frequency ν.
Let us write S(I,ν) for an entropy density function, which gives the entropy per unit volume as a function of energy intensity and frequency ν, and consider that our first task is to find the correct expression for S(I,ν) in termsof I andν.Ournotationisabitredundant,since I isa function of ν, but it will make our subsequent calculations easier to follow.
We shall follow Einstein and use Wien’s expression for I,
	I(ν,T) = aν3 exp(−bν/T)	(21)
instead of Planck’s, even though it was well known that Wien’slawwasvalidonlyforlargevaluesofν/T.Solving Eq. (21) for 1/T, we obtain
	1/T = −ln[I(ν,T)/aν3]/bν.	(36)
Then, using the fact that the derivative of entropy with respect to energy is equal to 1/T, we get
	∂S(I,ν)/∂I = 1/T.	(37)
We then substitute Eq. (36) into Eq. (37) and integrate with respect to I to obtain the entropy function
= −I(ν,T)[ln(I(ν,T)/aν3) − 1]
S(I,ν)	 .	(38) bν
Nowconsideravolume V inthecavity,andsupposethat the radiation is nearly monochromatic, say of frequency ν. The radiation energy in volume V for frequency ν is given by another spectral density function,
	E(ν,T) = VI(ν,T).	(39)
The entropy in volume V for frequency ν is then found by solving Eq. (39) for I(ν,T) and substituting into Eq. (38):
S(E,ν) = VS (I,ν)
−E(ν,T)[ln(E(ν,T)/Vaν3) − 1]
	=  .	(40)
bν
Next we recalculate a new entropy for a volume V  smaller than V. For the same energy E(ν,T), substitute V  intoEq.(40)tocalculate S.Thentheentropydecreases by an amount
	S .	(41)
Now we relate Eq. (41) to the key relation of Boltzmann statistics, S =k ln W, which applies to an ideal gas in a closed container. (Einstein used this equation in his paper of 1905 but did not express it using the letter k.) For a change of the gas from one state W to a state W, the corresponding change in entropy is
	S  ,	(42)
where W is interpreted as the “probability” or likelihood for the given state to occur.
Boltzmann statistics applies to a finite number of molecules in a gas. We are not considering a gas in blackbody radiation, nor are we explicitly using Planck’s model of finitely many “oscillators.” What then shall we consider as the meaning of a “state” in our context? Returning to our derivation of Eq. (42) in terms of a change in volume from V to V , let us recall that, if N particles (of anything) are allowed to travel freely in a vessel of volume V, then the probability of finding, at any given instant, all N particles in a portion of the vessel having volume V  < V is
	 .	(43)
The corresponding decrease in entropy of the system of particles from the state of random distribution to the state of all particles in the smaller portion is thus
S  N
	 .	(44)
Now we argue backward from Eqs. (41) and (44). If we take the view that Eq. (41) gives the change in entropy accompanying a decrease in the volume of the blackbody cavity from V to V , and we assume that the radiation energy E(ν,T) is distributed among N independent particles of some sort, which are allowed to move freely in the cavity, then the right side of Eq. (41) must equal the right side of Eq. (45). We then conclude that
	Nk = E(ν,T)/bν	or	E(ν,T) = Nkbν.	(45)
That is, monochromatic radiant energy behaves as if it were composed of independent energy “quanta” of magnitude kbν.
Einsteinimmediatelysuggestedthatthesamereasoning could be applied to the radiation of light and thus fired another shot in the 20th century revolution in physics by proposing a return to the particle theory of light: a view considered dead nearly a century. This proposal was so radical that even Planck, who never considered himself a revolutionary anyway, rejected it.
Let us see how Einstein’s theory of light quanta provided an explanation of the photoelectric effect. If an electron in a metal strip is set free by the energy of a quantum of light incident on the metal, then the kinetic energy of the electron is equal to at most the energy of the incident quantum, which is proportional to the frequency of the light. This kinetic energy is less than the energy of the incident light quantum, according to the amount of work required to overcome the forces tending to keep the electron bound to the metal. Moreover, increasing light intensity increases the number of light quanta incident on the metal and hence increases the number of electrons freed; but the energy of the freed electrons is dependent solely on the frequency of the light.
Einstein was careful to point out that his light quantum hypothesis, which was motivated in part by Wien’s radiation law, was limited to the range of frequencies and temperatures for which Wien’s law was valid.
Einstein’s approach to quantization differed from Planck’s in a fundamental way. Planck assumed the quantization of energy to derive his radiation law, therefore showing that the quantum hypothesis was sufficient to obtain the law. Einstein, on the other hand, started with Wien’s radiation law and showed that one of its necessary consequences was the quantization of monochromatic radiant energy.
It is also worth mentioning the advantage Einstein’s theory had over Planck’s in that it did not involve oscillators and so did not directly contradict the equipartition theorem.
Let us now look briefly at the data predicted by Einstein’s theory and verified to a high degree of accuracy by R. A. Millikan in 1916, about 10 years after Einstein published his paper. We shall denote the maximum kinetic energy of an electron emitted by a light quantum of frequency ν as
	KE ,	(46)
where E is the amount of energy necessary to remove the electron from the metal. Note that this kinetic energy is a linear function of ν. When accurate date are plotted as a linear graph of KE versus ν, we can measure the slope of the line, which turns out to be Planck’s constant h. Since the nature of the metal affects the kinetic energy of the electron only in the additive constant E, the slope h appears to be a universal constant. In other words, kb=h in Eq.(46),sothattheenergyofalightquantumoffrequency ν is hν.
AlthoughEinsteinandPlanckwereatoddsoverthefundamentals of each other’s work, this constant h provided an undeniable link between their theories and a powerful motivating force for further investigations into its role in nature.
C. The Quantum Theory of Specific Heat
At the same time Einstein put forth his theory of light he also proposed a theory of specific heat of solids that was to becomeanotherpillarofquantumtheory.Hisworkfurther widened the range of applicability of quantum concepts. Let us return to Planck’s radiation law,
	E(ν,T) = hν/[exp(hν/kT) − 1]	(34)
for the average (over time) energy of an oscillator of frequency ν in a blackbody furnace in equilibrium at temperature T. Recall that a consequence of Planck’s derivation of his radiation law is that the oscillators in the radiation field can have energy values only in the discrete range0,hν,2hν,...,forthesearethevaluesoftheenergy elements he uses to distribute over the oscillators to make his statistical calculations. Einstein understood that this implied a revolutionary principle that in turn implied a modificationofalltheoriesofphysicalphenomenadealing with exchanges of energy between radiation and matter. In particular, the theory of heat, based on the equipartition law, was at odds with experimental evidence on the specific heat of solids. He sought a new theory of specific heat without the equipartition law, similar to the way Planck had disregarded equipartition in his theory leading to Eq. (34).
AlthoughEinsteinusedEq.(34)inhistheoryofspecific heat,itisimportanttonotethatheprovidedhisownderivation of it. To get at the heart of Einstein’s derivation, let us consider a vibrating physical system (e.g., a linear oscillator) that can exist in various states of thermodynamic equilibrium, while vibrating at frequency ν. Let us denote by φ(E,ν) the energy density function, which, when integrated between limits E1 and E2, gives the number of states that have energy between those limits. Let P be a probability density function: P(E, T) is the probability that the system is in a state of energy E when at equilibrium at temperature T. Then the energy of the system is given by the expected value
 (E, T)φ(E,ν)dE
0
E(ν, T) =.	(47) ∞	(E, T)φ(E,ν)dE
WenowarriveatEinstein’scharacterizationofφ,which defines a principle applicable to all systems involving interaction between vibrating matter and electromagnetic radiation.
There exists a positive number r, very small compared with hν (h is Planck’s constant), and a sequence of intervals of numbers In =[nhν,nhν +r] such that:
1.	 0onlyforvaluesof E lyingintheintervals
I0, I1,....
2.	 In dE is equal to the same constant for all integers n =0,1,2,....
Figure 2 shows intervals In for n =0,1,2,3.
From this formulation of φ and the use of expression P(E)= exp(−E/kT) (from statistical mechanics) in Eq. (47), Einstein was able to derive Eq. (34).
What is accomplished by this formulation of φ is the restriction of nonzero energy values to a set of small intervals: again, almost a “quantization” of energy. Much more isalsoaccomplished,however.First,thevaluehν emerges
FIGURE 2 Intervals of nonzero values of energy density
as a key energy value with an existence not immediately tied to linear oscillators. Second, as we shall see later, this generalized derivation of Eq. (34) enabled Peter Debye to use it as a point of departure to obtain Planck’s radiation law without the fundamental inconsistencies contained in Planck’sderivation.Finally,theformulationofφ asaprincipleapplyingtoallsystemsinvolvinginteractionbetween matter and radiation elevated the status of quantum theory from an ad hoc assumption about oscillators to a scientific principle.
Let us apply Eq. (34) to vibrating atoms, which determine the heat capacity of a solid. If an atom has three independent vibrational degrees of freedom, all vibrating with the same frequency ν, then it can be considered to be three independent vibrating systems, and so the energy of each atom is calculated from Eq. (34):
E(ν, T) = 3hν/[exp(hν/kT) − 1]. The energy of 1 g-atom of the solid is therefore	(48)
E(ν, T) = 3Nhν/[exp(hν/kT) − 1],	(49)
where N, known as Avogadro’s number, is the number of atoms in 1 g-atom of the solid in question. From Eq. (14), the heat capacity of the solid is then dEtot(ν, T) 3Nk(hν/kT)2 exp(hν/kT)
	 =	−	.	(50)
	dT	[exp(hν/kT)	1]2
The formula for the specific heat of the solid then follows by dividing Eq. (50) by the mass of the solid. This result was recognized by Einstein as subject to correction because it rested on serveral simplification assumptions.
In spite of its need for correction, Eq. (50) represents the first application of quantum theory to solids. What is more important, historically, is that it established that the principle of quantum theory reached beyond one or two specificphysicalphenomena.ThiswastheviewofWalther Nernst, who obtained solid evidence of Einstein’s formula for specific heat and whose eloquent praise of quantum theory around 1910 was instrumental in the organization ofthefirstSolvayCongressin1911.Thatwasaconference of distinguished physicists gathered together in Brussels for the purpose of discussing the “new” quantum theory.
D. Debye’s Derivation of Planck’s Radiation Law
As we have noted, Planck’s theory leading to his radiation law contains a fundamental inconsistency made clear by Einstein: the requirement that oscillator energy by
φ(E,ν) in Einstein’s derivation of the law of blackbody radiation.
continuously variable for the formula I(ν, T)= aν2E(ν, T) and that it be discontinuously variable for the formula E(ν, T)=hν/[exp(hν/kT)−1]. Nevertheless, the unqualified success of the radiation formula itself in matching experimental results, together with the successful application of the fundamental idea of quantization to other realms of physics, prompted great efforts to remove the inconsistency. This was finally accomplished by Peter Debye in 1910. Let us trace Debye’s argument.
The key to our success will be the elimination altogether of the need for oscillators. Instead, we consider the cavity of a blackbody furnace to be a resonating chamber and draw an analogy between the radiation waves in the electromagnetic field in the cavity and the vibrations of an elastic fluid in an enclosed container. This idea was, in fact, proposed in 1900 by J. W. Strutt, better known as Lord Rayleigh, who was an expert in sound and likened blackbody radiation to sound waves.
It is known from the theory of sound that a cubic box of volume L3 supports standing sound waves of vibration only in modes of wavelength
	 ,	(51)
where k, l, and m are positive integers.
Let R3 standforthree-dimensionalspace.Foreachpositive number r, consider the sphere of radius r centered at the origin and let Sr denote the segment of the sphere in thefirstoctant.Nowifamodeofvibrationinthecubicbox with wavelength λ given by Eq. (51) is associated with a
 
point (k,l,m) in R3 of distance r =√k2 + l2 + m2 from the origin, we have from Eq. (51) that
	λ = 2L/r.	(52)
In terms of frequency ν =c/λ (c is the speed of light, the speed at which we assume electromagnetic waves propagate), we can rewrite Eq. (52) as
	r = 2Lν/c.	(53)
Let us now consider an interval of numbers [r,r ], and ask how many points (k,l,m) with integer coordinates lie in the region Q(r,	r) between Sr and Sr+	r. If r is very large, which it is for the very short wavelengths in blackbody radiation, then this number of points can be approximated reasonably by the volume of Q(r,	r). To see this, imagine a large region of space filled with unit cubes centered at the points in the region with integer coordinates. These cubes fill space and each contains exactly one point with integer coordinates. The larger the region, the better we can approximate its volume with such unit cubes. In other words, points with integer coordinates occupy space with a density of one per unit volume.
Now the volume of Q(r,	r) can be approximated by the surface area of Sr times the thickness of Q(r,	r). So we can write that the number of integer points (k,l,m) in Q(r,	r) (one-eighth of a spherical shell) is
	Nr = 4πr2	r/8.	(54)
Each point with integer coordinates determines a mode of vibration of a particular wavelength, although it is clear from Eq. (51) that several points (modes) can correspond to the same wavelength. In addition, in electromagnetic radiation each mode can be polarized in one of two ways, so that we must double the right-hand side of Eq. (54) to account for all possible modes of vibration corresponding to Q(r,	r). Now let us use Eq. (53) to rewrite Eq. (54) in terms of frequency, replacing	r with (2L/c)	ν, to obtain
	Nν = 8πv2L3	ν/c3.	(55)
Finally, we allow	ν to become infinitesimally small and divide by L3 to obtain a density function giving the density of modes of vibration of the electromagnetic field per unit volume in the blackbody cavity as a function of frequency:
	φ(ν) = 8πν2/c3.	(56)
The next step is to consider a unit volume of the cavity in thermal equilibrium at temperature T and the total electromagnetic energy I(ν, T) due to radiation of frequency ν. Then we partition this total energy into discrete packets of value E(ν, T) and distribute these packets among the modes associated with ν according to Eq. (56) to obtain a
spectral density function for energy:
	I(ν, T) = φ(ν)E(ν, T) = 8πν2E(ν, T)/c3.	(57)
Thus, we arrive once again at Eq. (22), this time without recourse to classical theory of linear oscillators. To be sure, this step is no less bold than Planck’s original “act of desperation” cited in Section III.D. Debye was encouraged to use this assumption of quantized energy by the derivation of Eq. (34) in Einstein’s theory of specific heat. To obtain Planck’s radiation law it is now necessary only to consider each mode of vibration to contribute the quantized value E(ν, T)=hν/[exp(hν/kT −1].
As we mentioned above, Debye’s derivation of the radiation law is fundamentally more attractive than Planck’s because, by avoiding arguments based on classical harmonic oscillators, it is possible to avoid the inconsistency in Planck’s theory cited by Einstein. By the same token, this derivation is noteworthy for its lack of any mechnical model to account for the radiation. It is necessary in Debye’s approach only to break up the variable, energy, into discrete quantum values and distribute those values over modes of vibration of a “vibrating” electromagnetic field.Thequantumtheory,theassumptionthatthephysical quantity, energy, is a discontinuous variable, appears here as a fundamental law of nature, and the role of the classical mechanical model as nature’s fundamental building block is thereby diminished.
Debye’s work is noteworthy for another reason. It outlines the basic pattern that characterizes all applications of what we have called the quantum theory. That is, to apply the quantum theory to a physical phenomenon, first find a description of the phenomenon that involves both energy E and frequency ν. Second, set energy proportional to frequency, E =hν, where h is Planck’s constant. All applications of early-20th-century quantum theory are variations on this theme. If E =mc2 has become the internationally recognized equation symbolizing the theory of relativity, then E =hν might well deserve the same status as the symbol of quantum theory.
IV. THE BOHR ATOM
A. The Planetary Atom
Between 1910 and 1913 an important development in physics was reported from Manchester, England. Ernest Rutherford had studied the results of bombarding a thin metallic foil with particles emitted by a radioactive substance. By observing how these particles were scattered aftertheyhitthefoil,Rutherfordwasabletoproposeamechanical model of the atoms in the foil that could account for the scattering effect.
Rutherford’s atom consists of a nucleus at the center of an electric field and a system of electrons that rotate about thenucleusinregularorbits,likeplanetsaroundasun.The electrons have small mass compared with the nucleus, and each one carries a negative electric charge e, today considered to have a value of about −1.6×10−19 coulomb (C). Since the atom is electrically neutral, the nucleus carries a positive charge Z|e|, where Z is the number of electrons in orbit. We call Z the atomic number of the atom.
This planetary model was considered quite a success, although it contained a fatal flaw, recognized even by Rutherford himself. The flaw is easy to see. A particle rotating in an orbit must have an acceleration toward the nucleus at every instant, or else it must fly off in a straight line. According to classical laws of accelerating charged particles, therefore, rotating electrons must constantly radiate energy in the form of electromagnetic radiation, as we mentioned in Section I.C. This loss of energy must result in a decrease in the orbital radius of the electron at such a rate that the electron must very quickly fall into the nucleus.
Thus, Rutherford’s model is untenable, at least for atoms having only one electron, such as hydrogen. Atoms withmanyelectronsmightavoidcollapsebecauseofcomplicated interaction among the orbiting electrons, but no such escape clause can exist in Rutherford’s theory for the hydrogen atom.
Niels Bohr, a Danish physicist who had visited
Rutherford’slaboratoryinManchesterin1912,appliedthe quantumtheorytotheplanetarymodeloftheatom.Bohr’s theory can be conveniently outlined in four postulates. Like Planck’s postulate about harmonic oscillators, some of Bohr’s postulate were controversial because they were ad hoc, without explanation based on classical physics. Like Planck’s postulate, however, they resulted in experimentally verifiable calculations, and so they were difficult to ignore. Furthermore, his postulates not only addressed the question of why atoms do not collapse but also introduced new mixtures of ideas relating waves to particles that were to become general principles of physics. Let us now examine Bohr’s theory of the atom by paraphrasing his postulates.
B. Bohr’s Postulates
1.	Postulate I
Atoms exist in states of equilibrium, with electrons rotating in prescribed orbits about the nucleus, but, contrary to classical laws of electrodynamics, they do not radiate energy while in these orbits. The orbiting electrons are subject to classical laws of mechanics while in these states, however, so each possesses a mechanical energy (potential plus kinetic) E, determined by laws of orbiting bodies. These states of equilibrium, or nonradiation, are called “stationary states” of the atom.
2.	Postulate II
Atoms can be made to change stationary states discontinuously in violation of classical laws of mechanics.
3.	Postulate III
During transition from one stationary state to another, atoms emit or absorb quantities of energy (energy quanta) in “bundles” characterized by frequency. The frequency ν of a quantum of radiant energy emitted or absorbed in a change from one stationary state of mechanical energy E1 to an adjacent state of energy E2 is related to Planck’s constant h by
	ν = (E1 − E2)/h.	(58)
Notethepattern:energy=hν,nowbecomingthehallmark of quantum theory.
 
FIGURE 3 Emission spectrum of iron gas.
Let us pause here to note one idea in this third postulate that foreshadows quantum mechanics. We can imagine a bundle of radiant energy emitted from an atom, racing throughspacewithmanyotherbundlesinawavelikebeam of radiation, and each bundle carries a message about the frequency of the beam according to Eq. (58). This idea was already well known for Einstein’s light quanta, of course, but now it appears again in another context. The generalization of the idea of these “wave–particles” is one of the cornerstones of quantum mechanics.
Bohr’s fourth postulate is directly related to the application of Rutherford’s model to the study of atomic spectra: radiation emitted from an electrically charged gas. When an electric charge is passed through a gas, neon, for example, the gas emits electromagnetic radiation, predominantly red light in the case of neon. The radiation emitted covers a continuous set of frequencies, but it is much stronger at a certain discrete set of frequencies than it is at others, giving rise to the terms continuous and discontinuous spectra, the latter being the set of frequency values at which radiation is very strong. We shall again use the more traditional word discontinuous in place of discrete. If we pass the beam of radiation from a glowing gas through a prism that separates the waves according to frequency,wecanobservepartofthespectrum,thevisible part, as in Fig. 3. The light lines indicate intense light at frequencies in the discontinuous part of the spectrum.
Thespectrallinesweretheobjectofmuchresearchnear the end of the 19th century. This research resulted in empirical formulas relating the frequencies of the discontinuous spectra to sets of positive integers. One such formula, developed by a Swiss schoolteacher, Johann Balmer, and reformulated by JanneRydberg in 1890 (Rydberg claimed originality) can be written
	ν = R(1/n2 − 1/m2),	(59)
where R is a constant, known as Rydberg’s constant, n and m are positive integers (with m >n), and ν is the frequency of a line in the discontinuous spectrum. For n =2 and m =3,4,5,..., frequencies given by Eq. (59) had been observed for the spectrum of hydrogen gas.
Let us now move to Bohr’s fourth postulate and see how it leads to an explanation of empirical formula (59). Consideranelectronincircularorbitofradiusr inanatom of atomic number Z. At each point in the orbit the force on the electron due to the attraction of the nucleus is
	F = Ze2/r2.	(60)
We then apply classical laws of mechanics [Eq. (8)] to arrive at the kinetic energy of the electron:
	KE = Ze2/2r.	(61)
The potential energy of the electron at every point in the orbit due to the attraction of the nucleus is
	PE = −Ze2/r.	(62)
This is the negative of the amount of work required to remove the electron from its orbit to a theoretical infinite distance from the nucleus. Thus, the total mechanical energy is
	E = KE + PE = −Ze2/2r.	(63)
The absolute value of E is the (positive) amount of energy requiredtobindanelectroninitsorbit,andweshalldenote it, as is customary, by W. We then observe that the value of W equals the kinetic energy of the electron given by Eq. (61). Then, writing that kinetic energy in its classical form in terms of the rotational frequency ω of a particle of mass m moving in circular orbit of radius r, we have
	W = |E| = KE = 2π2mr2ω2.	(64)
This formula for binding energy was adjusted by Bohr to account for noncircular orbits and rotating nuclei, but our simplified form is sufficient to continue with our story of the Bohr atom.
The next step is based on the pattern characteristic of applications of quantum theory mentioned at the end of Section III. We seek a relation between energy W and orbital frequency ω and Planck’s constant h. Bohr actually provided several plausibility arguments leading to the fourth postulate, some more convincing than others. We shall follow two of those arguments, one because it is simple, the other because it is based on an important philosophical principle. Remember, however, that these are just heuristic arguments. All of Bohr’s postulates are ad hoc assumptions.
We begin the first heuristic argument by establishing a relation between orbital frequency ω and the frequency ν of radiation emitted during a change between stationary orbits.Assumethatintheprocessofbindingafreeelectron to the nucleus a binding energy quantum of frequency ν is required. If the orbital frequency resulting from the binding process is ω, then ν should be the average of ω for the orbiting electron and zero for the free electron. Thus,
	ν = ω/2.	(65)
Now we can state Bohr’s fourth postulate.
4. Postulate IV
An atom with one electron can exist in stationary states of equilibrium indexed by natural numbers n =1,2,3,.... In the state associated with number n, the electron orbits about the nucleus and the mean value of its kinetic energy in that orbit is given by
	KE = nhω/2,	(66)
where ω is its orbital frequency and h is Planck’s constant. Note that this postulate is again a variation on the theme
E =hν.
C. The Correspondence Principle
Next we shall examine a second argument leading to Eq. (66) based on what is now called the correspondence principle. We begin by assuming that the energy W for binding an electron into stationary orbit of frequency ω is proportional to hω. We then suppose that there is an orbit of lowest binding energy W =αhω, where α is a proportionality constant, and that all other orbits have binding energies W1, W2,... given by
	Wn = nαhω,	(67)
where n is a natural number called the quantum number for the stationary state. The state with n =1 is called the ground state of the atom.
Let us solve Eq. (64) for ω2 to obtain
	ω2 = W/2π2mr2	(68)
and replace r2 using Eq. (61) and the fact that W = KE to obtain
	ω2 = 2W 3/π2me4 Z2.	(69)
Now if we index each orbit by its quantum number n to rewrite Eq. (69) using ωn and Wn in place of ω and W, we can substitute Eq. (67) into Eq. (69) and solve for ωn:
	ωn = π2me4 Z2/2α3n3h3	(70)
Using Eq. (67) once more, we obtain
	Wn = nαhωn = π2me4 Z2/2α2n2h2.	(71)
Now let us use postulate III and consider the quantum of radiation with frequency ν emitted during a change of statefromonewithquantumnumbern +1tothestatewith quantumnumbern.Thisisachangefromastateofsmaller binding energy Wn+1 to one of higher binding energy Wn (with smaller orbit), which corresponds to a decrease in mechanical energy from a negative value En+1 to a greater negative value En.
Then from Eq. (58) we have that ν = (En+1 − En)/h
	= (−Wn+1 + Wn)/h,	(72)
which from Eq. (71) gives us
	 	(73)
This brings us to the correspondence principle:
For very large quantum numbers n, the quantum theory frequency of radiation ν should correspond to the classical theory frequency ω of radiation from a charged particle in a circular orbit of orbital frequency ω.
In other words, the frequency ν given by Eq. (73) should equal the frequency ωn given by Eq. (70) for large values of n.
Now for large values of n,(2n +1)/n2(n +1)2 is approximately equal to 2/n3. If we therefore replace (2n +1)/n2(n +1)2 in Eq. (73) with 2/n3 and use the correspondence principle to set ν =ωn, we arrive at  . We now take another bold step by declaring that what is true for large n must be true for all n. This will complete our second heuristic argument leading to postulate IV, for if the kinetic energy KE of a rotating electron in an orbit of quantum number n is to equal the binding energy Wn, we have from Eq. (67) (recall that  ) that
	KE = nhω/2.	(74)
The correspondence principle has been generalized and restated many times since it was first applied by Bohr in 1913. A form of this principle is another one of the cornerstones of quantum mechanics. That is why we have traced this last argument leading to Eq. (74).
D. Consequences of Bohr’s Theory
First, note that we can rewrite Eq. (74) in terms of angular momentum l of an orbiting electron with kinetic energy KE. From Newtonian dynamics it can be shown that l =KE/πω for orbital frequency ω, and so from Eq. (74) we obtain
	l = nh/2π	(75)
for stationary orbit with quantum number n. In other words, the quantization of the kinetic energy is equivalent to the quantization of the angular momentum of the orbiting electron. Though it would be much easier to derive Eq. (74) by simply assuming the quantization of angular momentum, that derivation completely avoids the correspondence principle and obscures a major philosophical point about Bohr’s contribution to quantum theory.
Let us note also the close resemblance between Bohr’s formula (73) and Rydberg’s formula (59). As we mentioned, Bohr adjusted his value for mass m in Eq. (73) to account for the combined mass of nucleus and electron. Setting   in Eq. (73) gave Bohr an equation of the form of Eq. (59) from which he could calculate the value R =2π2me4 Z2/h3.
For hydrogen, where Z =1, this formula provided excellent agreement with the experimentally determined value for R, using the best-known value for h at the time. Another major victory had been scored for quantum theory.
V. TRANSITION TO QUANTUM MECHANICS
There were several important victories for quantum theory between 1913 and 1925. None of them, however, provided new fundamental principles. So it is at this point that we conclude our discussion of quantum theory with a brief look at some of the steps that were required to make the transition from quantum theory to quantum mechanics.
Recall that what we have been calling quantum theory is really a collection of theories applied to different phenomena by mixing variable amounts of classical physics and quantum hypotheses. The three themes of quantum theory—the quantization of energy and the probabilistic behavior of energy quanta, the wave–particle nature of some matter, and Planck’s constant—formed an interrelated set of ideas that lacked a universality and coherence necessary for them to constitute a scientific theory. Also lacking was a system of mathematical expressions common to all applications of quantum theory from which one could calculate the values of quantities observed in experiments.
Quantum mechanics, like Newtonian mechanics, was born of the necessity to bring mathematical clarity and ordertothechaosofobservationsofthephysicaluniverse. Although Newtonian mechanics brought order to a set of observations of the continuous, predictable macroscopic world,itwasinadequatetodealwiththenewchaoscreated by quantum theories of the discontinuous, unpredictable microscopic world.
One step in the transition from quantum theory to quantum mechanics was a philosophical one. Recall that in our discussion of Newton’s contributions to science (Section I) we cited, as one of the most important, the notion that explanations of hidden, unobserved events come from precise measurements of observed events. In fact, it is this deductive power that some people equate with science itself. Yet Werner Heisenberg in 1925 saw that it was theuniversalapplicationofthisnotionthatstymiedthedevelopment of a quantum mechanics. By first accepting the philosophicalviewpointthattheonlyquantitiesofphysics are the observable ones, he was able to produce his kinematics of quantum theory, a calculus of “observables.” We now call it matrix mechanics, although Heisenberg never used the word matrix to describe the rectangular arrays of numbers that appeared in his equations as the observables. One of the results of Heisenberg’s mechanics was a calculation that involved Planck’s constant in a profound way. With each observable Heisenberg defined a quantity called the uncertainty of the observable. He then showed that, for certain pairs of observables, the product of their uncertainties is at least as large as Planck’s constant. Two observables related in this way are called incompatible observables. A consequence of this “uncertainty principle” is that the reduction of the uncertainty in one of the observables necessarily implies an increase in the uncertainty of the other. Heisenberg took these uncertainties to be a fundamental fact of nature, not a consequence of the inaccuracy of the measuring devices of physicists. Thus, he took one step farther Planck’s reluctant acceptance of the fundamentally probabilistic behavior of oscillators and the implied uncertainty of that behavior. Heisenberg’s complete break with the classical Newtonian physics of certainty sparked years of research that continues to this day, not only in physics, but also in philosophy, logic, and mathematics.
Another step in the transition to quantum mechanics was the theory of wave mechanics developed by Erwin Schrodinger. Working at the same time as Heisenberg in¨ late1925,butcompletelyindependently,Schrodingerpro-¨ duced a parameterized set of partial differential equations that had solutions only for a discrete set of values of the parameter. The equations involved a differential operator, and Schrodinger was able to show that his equations could¨ be applied to any physical system by choosing appropriate differential operators. He then claimed that, after an operator was correctly chosen to represent a particular system, thediscreteparametervaluesforwhichtheresultingequation had solutions were all the possible values of energy for that system. Here, then, was a universally applicable mathematical formula that helped change quantum theory into quantum mechanics.
Although Schrodinger did not supply a convincing the-¨ oretical foundation for his equations, he was able to show in 1926 that his equations were mathematically equivalent to Heisenberg’s matrix mechanics. There was no doubt in anyone’s mind that the resulting combined theory, quantum mechanics, was a major scientific achievement. There was considerable doubt in the minds of some, however, Einstein most prominently, that the new mechanics, with its philosophical roots in the physics of uncertainty, was as universally applicable as its proponents claimed. Although controversy over its range of applicability persists to this day, quantum mechanics was the final step that brought Max Planck’s “desperate act” to explain blackbody radiation to the status of a full-fledged scientific theory.
VI. AFTER QUANTUM MECHANICS: MODERN DEVELOPMENTS IN FOUNDATIONS OF QUANTUM PHYSICS
The quantum mechanics developed by Schrodinger and¨ Heisenberg provided mathematical formulas with which to calculate physical values but lacked theoretical underpinnings. These were supplied by Max Born, Niels Bohr, andmanyothersinthelate1920sandearly1930s.Thetheories, however, were controversial, and remain so to this day.Whilequantummechanicshasbeensuccessfulinpredicting the outcomes of some delicate experiments with photons, electrons, and other nuclear particles, some crucial predictions have not been experimentally confirmed. These predictions lie at the heart of the quantum theory controversy that we will explore in this section.
The most famous criticism of the theoretical foundations of quantum mechanics was published in 1935 by Albert Einstein, Boris Podolsky, and Nathan Rosen in a paper now called the “EPR paper” after the names of its authors. The paper describes a “thought experiment”—an experiment using an apparatus which could not be built at the time but which could test the theoretical predictions of quantum mechanics. The authors argued that the theory of quantum mechanics was incomplete because it contained no counterpart for an “element of reality” present in the objects in their apparatus. They were quite precise in their definition of an “element of reality”:
If, without in any way disturbing a system, we can predict with certainty ... the value of a physical quantity, then there exists an element of physical reality corresponding to this physical quantity.
We shall describe a simplified version of the EPR thought experiment. Although our presentation is faithful to the ideas in the EPR paper, we have taken advantage of the 65 years scientists have had to study the paper to reframe the discussion for greater clarity.
Twoquantummechanicalobjects(photonsorelectrons, for example) are sent hurtling through space in opposite directions by a firing device. A certain measurement is performedonObject1(travelingtotheleftinthediagram) at collector A, and a similar measurement on Object 2 at collector B (see Fig. 4).
At each collector is a dial which can be set at any angle from 0 to 360 degrees. We shall explain the use for the dial later. The measurements are arranged so that for every setting of the dial, every time a pair of objects is fired, when an object reaches its collector one of two outcomes is recorded: “yes” or “no.”
It is theoretically possible to design the EPR apparatus using special pairs of objects so that the outcomes of the measurements at the two collectors are correlated if the predictions of quantum mechanics are correct. Specifically, quantum mechanics predicts the following correlation:
 
FIGURE 4 An EPR apparatus.
when the dials are set at the same angle, for each pair of objects fired, if a measurement on Object 1 at collector A registers “yes,” then one can predict with certainty that the measurement on Object 2 at B will also register “yes,” whether or not the measurement at B is actually made.
This implies that Object 2 has an “element of physical reality.” It is carrying a code of some sort that determines how the measurement at B will turn out before the measurement takes place. The roles of Objects 1 and 2 could have been interchanged in our description, so, if we conclude that Object 2 is carrying a code, it is safe to assume that both objects carry a code as they race toward their respective collectors.
Einstein, Podolsky, and Rosen cited a basic tenet of quantum mechanics, which asserts that the objects in the EPR apparatus cannot carry codes. The theory of quantum mechanics requires that these objects behave probabilistically, and that only a measurement can reduce the probabilism to a state of certainty. The assumption that the objects cannot carry outcome-determining codes before they are measured is crucial to the theory of quantum mechanics; without it the entire theory collapses.
We can see why the EPR authors called the theory of quantum mechanics “incomplete.” Because, after measuring Object 1, one can predict with certainty the value of the “yes–no” property of Object 2 without in any way disturbing it, this property has an element of physical reality which has no counterpart in the theory of quantum mechanics.
There was one response to the EPR paper which Einstein dismissed immediately, but which has lingered to this day as an intriguing possibility. Perhaps the objects in the EPR apparatus have no codes when they are fired, but by measuring Object 1 at A we somehow endow both objects with a code. This possibility is consistent with the theory of quantum mechanics, because it allows that the codes are produced by the act of a measurement. Einstein called this notion “spooky action at a distance.” This is because the apparatus could theoretically be arranged so that Object 2 was far away from Object 1 at the time of measurement at A, requiring a “spooky action” to carry a message about the measurement at A faster than the speed of light to Object 2 in time to be measured at B, contradicting the theory of relativity.
Einstein, Podolsky, and Rosen ended their paper by asserting that while they had shown the theory of quantum mechanics to be an incomplete description of physical reality, they believed that a complete, realistic theory could be found eventually.
Hundreds of books and papers have been written about the EPR dilemma, and for years theoreticians searched for the complete, realistic theory Einstein and others believed to exist. In 1964, however, nine years after Einstein’s death, a Scottish mathematician, J. S. Bell, poured cold water on the search. He showed that no “realistic, local” theory to explain the EPR experiment can exist that is consistent with the experimental outcomes predicted by quantum mechanics. A “realistic” theory asserts that the objects in the EPR apparatus carry codes which determine how the “yes–no” measurements at every angle setting of the dials will come out, whether or not the measurements are actually made. A “local” theory is one that prohibits a measurement at one collector from sending a signal across space at speeds greater than the speed of light to the other object.
We emphasize that the inconsistency demonstrated by Bell is not between realistic, local theories and the current theory of quantum mechanics, but rather between realistic theories and the experimental results predicted by the current theory of quantum mechanics. Thus, even if the currenttheoryofquantummechanicsisdiscarded,ifEPRtypeexperimentsresultinthecorrelationspredictedbythe current theory, then Bell’s proof shows that no realistic, local theory can be used to explain those correlations.
Bell’s result can be understood by considering the dials on the EPR apparatus. Suppose we assume that there is a realistic, local theory describing the behavior of the object pairs. By that we mean that for each pair fired an element of reality is accounted for by a code carried by the objects which determines for every setting of the dials which outcome (“yes” or “no”) each collector will record whentheobjectgetstoit.Letussetbothdialsat0degrees. We know that quantum mechanics predicts that with these settings the outcomes at the two collectors will be perfectly correlated: each firing will result either in “yes” at both collectors or “no” at both.
NowsupposewemovetheAdialtoasetting+n degrees for some small number n, say 2 or 3, and leave the B dial at 0. Then if 100 pairs of objects are fired, there might be a loss of correlation. Let us denote by M1 the number of mismatches (“yes” at A and “no” at B, or vice versa) in 100 firings. Next, let us leave the A dial at +n, and move the B dial to −n, (say 357 or 358 degrees), and fire another 100 pairs with exactly the same codes as the first 100 had. Bell’s results establish that as long as we assume that the objects are carrying codes, and that what is recorded at one collector cannot affect what is recorded at the other, then when the dials are set at −n and +n during 100 firings, the number of mismatches M2 in this new situation cannot exceed 2M1. That is M2 ≤2M1. The theory of quantum mechanics predicts, however, that the number of mismatches in the second set of firings will be more than twice the number of mismatches in the first set. That is, M2 >2M1. The predictions of quantum mechanics and realistic, local theories are then in irreconcilable conflict.
Much modern experimental research is devoted to turning the EPR-type thought experiments into real experiments to establish whether or not the predictions of quantum mechanics actually attain. One such series of experiments was performed by a team of scientists headed byAlainAspectatOrsay,France,between1982and1988. These experiments provide evidence that the results predicted by quantum mechanics do in fact attain in the physical world as we know it. The evidence, however, is not incontrovertible. The Aspect experiments used object detectors which are the best that can be built with modern technology, yet are only about 15% efficient. That is, only about 15% (or fewer) of the measurements at each collector can be guaranteed to be correct. To rule out the possibility that the results in the Aspect experiments were merely a coincidence produced by experimental error, we would have to build detectors that are at least 80% efficient. Most experimenters do not see the possibility of building such detectors in the foreseeable future.
We see then that 90 years after Max Planck put forth his “desperate” quantum hypothesis, the theory behind quantum behavior is still not fully formulated. Current formulations are fraught with ambiguities and counter-intuitive hypotheses. They are at odds with centuries of Western thought, including Platonism, classical physics, and most religions. It is understandable that many people are reluctant to throw out all of this tradition merely because one peculiar model for describing subatomic phenomena is enjoying high predictive value at the moment. It is little wonder that the theories of quantum physics are the object of such intense scrutiny and debate in the worlds of science, mathematics, and philosophy.
VII. AN ADVANTAGE OF UNCERTAINTY:
QUANTUM COMPUTING
Even though the problems with the quantum theory exposed by the EPR paper and Bell’s Theorem caused a great stir among philosophers and those fascinated by the foundations of science, they did not stop physicists from using quantum mechanics to make many important discoveries throughout the second half of the 20th century. As the century drew to a close, however, a troubling clash between quantum theory and high-speed computers suddenly turned into what promises to be an exciting marriage.
In the 1980s and 1990s high-speed computers became faster and faster, in part because their components became smaller and smaller. Computer “bits,” the devices used to store the “zero-one” information at the heart of all computations are becoming so small that they’re beginning to approach atomic scale. And on that scale the laws of quantum physics begin to apply.
The most troublesome quantum law facing computer designers is Heisenberg’s Uncertainty Principle. To say that a computer bit is “in a state 0 or state 1” is a classical notion—one which requires a realistic, local theory of the physicsgoverningthebit.AswesawinSectionsVandVI, however, realistic, local theories are at odds with quantum mechanics. Instead, on the quantum level it is essential to accept the fact that a computer bit exists in a probabilistic state. So the best we might be able to say is that a bit is “in a zero state with a given probability.” While this situation might seem to spell doom to the idea of building computers on the quantum level, it turns out instead to present a promising new direction for computing.
To see how uncertainty can be used to advantage let’s look at a geometrical conceptualization of the Uncertainty Principle. Recall from Section V that Heisenberg’s matrix mechanics identifies pairs of incompatible observables. Two observables are incompatible if at every instant the more certain we are about the value of one of them, the more uncertain we must be about the value of the other. To make precise this notion of uncertainty of values let’s consider a physical system (a spinning electron, for example) and an observable O1 which can take on two values a and b (say, “spin-up” and “spin-down” in a certain direction). We can represent the two values with a perpendicular set of axes. We say that at every instant in time the system “exists in a state ,” which we represent as a vector of length one on our axis system (see Fig. 5).
Thenwemakethestatementwhichliesattheheartofthe probabilistic description of quantum mechanics. We say that when the system is in state , then a measurement of observable O1 will yield the value a with probability |λ1|2, which is the square of the length of the projection of the state vector  onto the a axis. At the same time the measurement will yield value b with probability |λ2|2, which is the square ofthe length ofthe projection of the state vector  onto the b axis (see Fig. 6). (Note that |λ1|2 +|λ2|2 =1, because  has length one. So the probability that a measurement will yield “either a or b” is one.)
If  lies along the positive a axis, we’ll say that the system is in state a¯, and if it’s along the positive b axis,
 
FIGURE 5 Two axes, representing possible values a and b for observable O1, and a state vector .
 
FIGURE 6 The squares of the lengths of the projections of the state vector  give the respective probabilities that a measurement of observable O1 will yield value a or b when the system is in state .
we’ll say it’s in state b¯. If it’s not along either axis, we’ll say it’s in a “superposition” of states a¯ and b¯.
Pay close attention to our description. When a system is in a superposition state, we don’t say that it “has” the value a or the value b, and that we’re uncertain as to which one it has. Rather, we say that the system has both values in some sort of mixture, with perhaps a greater probability of yielding one of these values rather than the other, if we measure the observable while the system is in that state. If we don’t measure the observable, the system can continue toexistinthesuperpositionstate,andwhenwedomeasure it,thesystemjumpsimmediatelyintooneofitstwocertain states, either a¯ or b¯. Because we don’t say that the system “has”avalue,ourdescriptionisnotarealistic,localtheory, and we are sidestepping the EPR-Bell dilemma.
Now for the same physical system consider a second observable O2, which can also take on two values, say x and y, and is incompatible with O1 (for example, “spinup” or “spin-down” in a different direction). Let’s represent x and y with perpendicular axes rotated 45 degrees counter clockwise from those representing the values of O1 (see Fig. 7).
 
FIGURE 7 Two pairs of axes, representing possible values for twoincompatibleobservables,andastatevector onthepositive a-axis.
Now we can see a dramatic graphical representation of the Uncertainty Principle. Notice that if the state vector  lies along the positive a axis, then its projections onto the x and y axes have length  (see Fig. 7). Hence if  is a state for which O1 has value a with certainty, then in that state a measurement of O2 will result in x or y with probability of   for each, a state of maximal uncertainty!
Moreover, we can see the tradeoff between certainty for O1 and certainty for O2 as  assumes various positions. That is, the more closely  aligns itself with one of the lines—the x axis,forexample—givinggreaterprobability that a measurement of O2 will yield x, the larger will be the projections of  onto the a and b axes, increasing the uncertainty of O1 for that state. There is no way to put the system in a state of zero uncertainty for O1 and O2 at the same time. That’s what we mean when we say that O1 and O2 are incompatible observables.
ThisgraphicrepresentationoftheUncertaintyPrinciple is a bit oversimplified. In practice physicists use complex numbers to describe superposition. But we won’t need complex numbers to illustrate our example of a quantum computation.
Howdoesaquantumcomputertakeadvantageofuncertainty? The answer lies in our assumption that a quantum physical system can have both values of a binary observableatthesametime.We’llillustratethepowerofquantum computing with a very simple example.
Let’s consider a set of n objects S ={a1,a2,...,an}, wheren isanevennumber.Supposewe’regivenafunction f : S →{0,1}. That is, f assigns either 0 or 1 to each aj in S.We’retoldthat f iseither“constant”(i.e. f (aj)= f (ak) for all j and k), or “balanced” (i.e. f (aj)=0 for exactly half the aj’s). Our problem is to determine whether f is constant or balanced. To see how quantum theory can help us with this problem, first let’s look at it in the language of states and observables. To keep things simple we’ll let n =2.
At the heart of every classical computer is a binary bit, a physical device which can be in one of two states; magnitized or not, on or off, etc. Generally, the two states are labeled 0 and 1. Let’s consider a1 and a2 as two states of a binary bit, which we’ll depict as two perpendicular unit vectors
 
and
 
in two-dimensional space. Then we’ll represent our function f as a 2×2 matrix F with all off-diagonal entries
FIGURE8 Thefunctionevaluator F flipsstatea1onlyif f (a1)=1.
zero, and diagonal entries djj =(−1) f (aj ) for j =1,2. For example, if f (a1)=1 and f (a2)=0, then
F  ,
whereas if f (a1)= f (a2)=1, then
F  .
First, we’ll see how a classical computer can determine whether a given f is constant or balanced. We can feed the state vector a1 into F to see if F flips the state vector. If f (a1)=1, then
	1	−1
	Fa	,
soa¯1 is flipped (see Fig. 8a). If f (a1) = 0, then
	1	1
	Fa	¯ .
(See Fig. 8b.)
Similarly, if f (a2) = 1, then the function evaluator F flips a2, otherwise it does not (see Fig. 9).
Clearly, to determine whether f is constant or balanced we need to feed both a1 and a2 to F. Feeding only one will not give enough information. We need to see if F flips both, neither, or only one of the two input states.
Turning now to a quantum computer, we see at its heart a “q-bit,” a physical device which can be in one of two states (up or down, for example) or in a superposition of both states. Then we can prepare our input state in a superposition  ), and feed that to F. What we get out is another superposition state  with its a1 and a2 components flipped or not, depending on the values of f (a1) and f (a2). For example, if f is constantly
FIGURE 9 The function evaluator F flips state a2 only if f (a2)=1.
0 ( f (a1) = f (a2) = 0), we get F  ==. If f is constantly 1, then we get F  == − (see Fig. 10).
On the other hand, if f is balanced, then F is either  or −, as shown (see Fig. 11).
All that remains to do to determine whether f is constant or balanced is to measure the magnitude of the vector inner-product P =|  . If f is constant, then P =1, because   is balanced, then P =0, because
 is orthogonal to . The inner product can be measured physically. The important thing to notice is that we needed tousetheevaluator F onlyonce,nottwice.Thatisbecause
we were able to feed it both states a1 and a2 simultaneously in a quantum superposition. And we should point out too that “applying the matrix F” involves only one physical operation in a quantum computer. It might mean firing a pulse through an array of polarized lenses. Do not confuse this operation with computing a matrix product classically. That takes many computer steps.
FIGURE 10 The superposition state  goes to ± when f is constant.
 
FIGURE 11 When fed to the evaluator F the superposition state
 goes to  when f (a1)=0 and f (a2)=1, and to − when f (a1)=1 and f (a2)=0.
Using superposition to cut down evaluations of f from two to one might not seem like a revolutionary achievement. We can, however, apply the same principles to a set S with a very large (even) number n. Classically, we would need as many as  1 executions of the evaluator F to determine whether f is constant or balanced in a worst-case scenario. Of course, we could be lucky when we start evaluating f (a1) and f (a2), and get f (a1)=1 and f (a2)=0, and know immediately thatn f is balanced. But if we evaluate f (a1), f (a2),..., f (a 2 ) and find that they’re all equal, then still don’t know whether f is constant or balanced. That’s why we need  1 evaluations in a worst case. Using a generalization of the superposition technique we used for the case n =2, however, we can design a quantum computer to determine whether f is constant or balanced with only one evaluation of a matrix F, even if n =2N , where N is any natural number N. Cutting down the number of required evaluations of f from  1 to 1 is a valuable achievement.
While we’ve illustrated how quantum theory might bring important advances to computing, we’ve left much unsaid. As we enter the 21st century, quantum computers exist mostly in theory. Although rudimentary quantum computershavebeenbuilt,itisn’tclearifit’swithinhuman reach to build one capable of handling serious problems. For one thing, it’s very hard to create a superposition state in the physical world, and maintain it long enough to be of value before it breaks down, or is altered by spurious physicalevents.Further,physicaloperations,suchasmeasuringthevectorinnerproduct,requireinstrumentsofvery high reliability—much higher than we foresee in the near future. And finally, it is not yet known whether there exists a class of problems which are theoretically easier to solve with quantum algorithms than they are with classical algorithms. For example, the mathematician Peter Shor has invented a quantum algorithm which theoretically can be used to factor large numbers faster than all known classical algorithms. It has not been proved, however, that there does not exist a classical algorithm which can factor large numbers just as efficiently as the quantum algorithm. Factoring is a very important matter, because most computer security systems are based on the inability to factor large numbers quickly. Anyone who can build a high-powered factoring machine might be able to crack security systems around the world. That’s one reason quantum computing is currently of great interest to physicists, mathematicians, and computer scientists.
SEE ALSO THE FOLLOWING ARTICLES
ATOMIC PHYSICS • CELESTIAL MECHANICS • CHEM-
ICAL	THERMODYNAMICS	•	ELECTROMAGNETICS	•
MECHANICS, CLASSICAL • PHOTOCHEMISTRY, MOLECULAR • QUANTUM MECHANICS • RADIATION PHYSICS • STATISTICAL MECHANICS
BIBLIOGRAPHY
Bell, J. S. (1964). “On the Einstein Podolsky Rosen paradox.” Physics 1, 195–200.
Cohen, D. W. (1989). “An Introduction to Hilbert Space and Quantum Logic,” Springer-Verlag, New York.
Cropper, W. H. (1970). “The Quantum Physicists,” Oxford Univ. Press, New York.
Einstein, A., Podolsky, B., and Rosen, N. (1935). “Can quantum mechanical description of physical reality be considered complete?” Phys. Rev. 47, 777–780.
Hermann, A. (1971). “The Genesis of Quantum Theory,” MIT Press, Cambridge, MA.
Jammer, M. (1966). “The Conceptual Development of Quantum Mechanics,” McGraw-Hill, New York.
Kuhn, T. (1978). “Black-Body Theory and the Quantum Discontinuity,” Clarendon Press/Oxford Univ. Press, New York. Pais, A. (1982). “Subtle Is the Lord: The Science and Life of Albert Einstein,” Oxford Univ. Press, London and New York.
Wheeler, J., and Zurek, W. (1983). “Quantum Theory and Measurement,” Princeton University Press, Princeton, NJ. [This book contains reprints of the papers by Bell (1964) and Einstein, Podolsky, Rosen (1935).]
 
 
Relativity, General
James L. Anderson
 
Stevens Institute of Technology
I. Space–Time Theories of Physics II. Newtonian Mechanics
III.	Special Relativity
IV.	General Relativity
V.	Gravitational Fields
VI.	Observational Tests of General Relativity
VII.	Gravity and Quantum Mechanics
GLOSSARY
Absolute object An element of a physical theory that affects but is itself unaffected by the other elements of the theory.
Binarypulsar Double star system, one of whose components is a neutron star.
Black hole A concentration of mass whose gravitational field is so strong that an event horizon forms around it.
Dopplershift Fractionalchangeinfrequencyoflightdue to relative motion between source and observer.
Dynamicalobject Anelementofaphysicaltheorywhose behavior is affected by the other elements of the theory.
Electrodynamics Theory of electric and magnetic fields and of the interactions of the charged particles that produce them.
Event horizon Surface formed around a black hole through which nothing, including light, can penetrate from the inside. Any object that falls through such a surface is forever trapped inside it.
Free bodies Material objects that are not acted upon by external forces. Used in the construction of both Newtonian and special relativistic theories.
Galileanrelativity The invariance of the laws describing physical systems with respect to Galilean transformations between observers moving with uniform velocity relative to each other.
Hubble constant Ratio of velocity of recession to distance of galaxies.
Light cone The surface formed by the light rays emanating from and converging on a point in space–time. Used in the construction of special relativistic theories.
Manifold A continuum of points characterized only by its global or topological structure.
Mapping Association of points of a space–time manifold with other points of this manifold.
Newtonian mechanics The basis for the description of physical systems obeying Newton’s laws of motion.
Perihelion Point in the orbit of a planet when it is closest to the sun.
 	93
Planes of absolute simultaneity The collection of all point that are simultaneous with respect to one another. Used in the construction of Newtonian laws of motion.
Riemannian geometry Geometry in which the distance between neighboring points is defined by a metric and is quadratic in the coordinate differences between the points.
Space–time manifold Four dimensional manifold that underlies the construction of the various space–time descriptions of physical systems.
Space–time theories Physical theories that make use of the space–time manifold in the formulation.
Special relativity The invariance of the laws describing physical systems with respect to Lorentz transformations between observers moving with uniform velocity relative to each other.
THE GENERAL THEORY OF RELATIVITY is currently accepted as our best macroscopic description of the gravitationinteractionthatexistsbetweenallphysicalsystems. It is also universal in that all physical systems are held to interact gravitationally. The predictions of general relativity differ both quantitatively and qualitatively from those of the Newtonian theory of gravity. Although the quantitative differences between the two theories is for the most part small, so that general relativity contains Newtonian gravity as an approximation, these differences have been extensively tested in the solar system and other astrophysical systems. The agreement between observation and theory is better than 0.5%. However, the qualitative predictions of the theory are its most exciting and challenging feature. Among others, the theory predicts the existence of gravitational radiation. Although this radiation has not been directly observed, the effects of its emission have been observed in the binary pulsar PSR 1913 +16 and agree with the predictions of the theory to within 3%. The theory also predicts the phenomenon of gravitational collapse leading to the creation of black holes. There is strong observational evidence that such objects exist in the universe. And finally, the general theory serves as the basis for our best description of the universe as a whole, the so-called hot big-bang cosmology.
I. SPACE–TIME THEORIES OF PHYSICS
A. The Space–Time Manifold
To understand the revolution wrought by the general theory it is useful to set it in a framework that encompasses it as well as the other two major structures of physics, Newtonian mechanics and special relativity. Basic to each of these structures is the notion of the space–time manifoldconsistingofafour-dimensionalcontinuumofpoints. It is assumed only that any finite piece of this manifold can be mapped in a one-to-one manner onto a connected region of the four-dimensional Euclidean plane. Otherwise, these points are featureless and indistinguishable from each other, and the manifold as a whole is characterizedonlybyitstopologicalproperties.Whilethismanifold is not itself associated with any physical entity, it serves as the basis for the construction of the geometrical structures that are to be associated with such objects.
Since the points of the space–time manifold can be mapped onto the four-dimensional Euclidean plane, one can coordinatize the manifold by assigning to each point the coordinates of its image point in the Euclidean plane, xµ, where the index µ takes on the values 0, 1, 2, 3. Because the points of the manifold are assumed to be indistinguishable, this mapping is to a large extent arbitrary and hence the coordinatization is also arbitrary. Depending on the topological structure of the manifold, it may be necessary to cover it with several overlapping coordinate “patches” to avoid singularities in the coordinates. If, for example, the manifold has the topology of the surface of a ball, it is necessary to employ two such patches to avoid the coordinate singularity one encounters at the pole when using the customary polar coordinates.
If the manifold is coordinatized in two different ways, for example, by using Cartesian or spherical coordinates, the coordinates used for one such coordinatization must be functions of those used for the other and vice versa. This relation is called a coordinate transformation. In order to preserve the continuity and differentiability of the manifold it must be continuous, nonsingular, and differentiable.
B. Geometrical Structures
In space–time theories, physical entities are associated withgeometricalobjectsthatareconstructedonthespace– time manifold. These objects can be of many different types. A curve can be associated with the trajectory of a particle and is specified by designating the points of the manifold through which it passes. This can be done by giving the coordinates of these points as functions xµ(λ) of a monotonically varying parameter λ along the curve. Likewise, a two-dimensional surface could be specified by giving the coordinates of the surface as functions of two monotonic parameters, and similarly for three- and four-dimensional regions.
In addition to collections of points, one can introduce geometrical objects that consist of a set of numbers assigned to a point. These numbers are said to constitute the components of the geometrical object. The components of the velocity of a particle at a particular point in its trajectory would constitute such a collection. If the components are specified along a trajectory, a surface, or any other part of the space–time manifold, they are said to constitute a field. The temperature in a room can, for example, be associated with a one-component field. Likewise, the electromagnetic field surrounding a moving charge can be associated with a field consisting of six components.
The basic requirement that must be met in order that an object be geometrical is a consequence of the indistinguishability of the points of the space–time manifold. It is that under a coordinate transformation, the transformed components of the object must be functions solely of its original components and the coordinate transformation. This requirement is simply met in the case of curves, surfaces, and so forth; for example, given a curve, the transformed curve can be immediately calculated given the coordinate transformation.
An especially useful group of geometrical objects for associating with physical entities are those whose transformed components are linear, homogeneous functions of the original components. The simplest example is the single-component object called a scalar φ(x). Under a coordinate transformation, its transformed value is just equal to its original value. The other linear, homogeneous objects constitute the vectors, tensors, and pseudoscalars, pseudovectors, and pseudotensors. Vectors and pseudovectors are four-component objects (they come in two varieties called covectors and contravectors), while tensors and pseudotensors have larger numbers of components. There are also objects whose transformed components are linear but not homogeneous functions of the original components. Finally, there are objects whose transformed components are nonlinear functions of the original components, although such objects have not been used to any great extent. In all cases, however, the nature of the object is characterized by its transformation law.
It should be pointed out that not all objects one can construct are geometrical. The gradient of a scalar is a geometrical object while the gradients of vectors and tensors in general are not.
C. Laws of Motion
Thebasisforassociatinggeometricalobjectswithphysical entitiesispurelyutilitarian—thereisnogeneralprocedure for making this association. The numerical values that these objects can assume are taken to correspond to the observed values of the physical entities with which they are associated. Since not all such values can in general be observed, it is necessary to formulate a set of rules, called here laws of motion, that select from the totality of valuesagivensetofgeometricalobjectscanhave,asubset that corresponds to possible observed values. Thus, if it is decided to associate a curve with the trajectory of a planet, one would have to discover a system of equations such as those obtained from Newton’s laws of motion to select from the totality of all curves the subset that would correspond to actual planetary trajectories.
Onerequirementthatonewouldliketobefulfilledbyall lawsofmotionisthatofcompleteness—everysetofvalues allowed by them must, at least in principle, be observable. It is, after all, the purpose of the laws of motion to rule out unobservable sets of values. Nevertheless, there are problems associated with the imposition of such a requirement. There may, for example, be practical limitations on our ability to observe all the values allowed by a given set of laws. It is unlikely that we will ever be able to attain the energies needed to verify some of the predictions of the grand unified theories that are being considered today. However, if one of these theories correctly described all thatwecanobserveaboutelementaryparticleinteractions, we would not discard it because we could not directly observe its other predictions. More troubling, however, are limitations in principle on what we can observe. When applied to the universe as a whole, the general theory of relativity allows for many different possibilities, yet by its very nature we can observe only the universe in which we live. In the strict sense, then, the general theory should be considered incomplete. Nevertheless, it does correctly describe a vast range of phenomena, and so far there does not exist a more restrictive theory that does so. Therefore, probably, the best we can do is to require that a law not admit values that could be observed if they existed but do not.
D. Principle of General Covariance
However the laws of motion are formulated, they must be such as to be independent of a particular coordinatization of the space–time manifold. This requirement is called the principle of general covariance and was one of the basic principles employed by Einstein when he formulated the generaltheory.Fortheprincipletohold,thelawsofmotion for a given set of geometrical objects must be such that all of the transforms of a set of values of these objects that satisfy the laws of motion must also satisfy these laws.
The principle of general covariance is not, as has sometimes been suggested, an empty principle that can be satisfied by any set of physical laws. If, for example, the geometrical object chosen to be associated with a given physicalentityisascalarfieldφ(x),thentheonlygenerally covariant law that can be formulated involving only this object is the trivial equation
	φ(x) = const.	(1)
In order to formulate a nontrivial law of motion for φ it is necessary to introduce other geometrical objects in addition to the scalar field. One possibility is to introduce a symmetric tensor field gµν(x) and its inverse gµν(x), which are related by the equation
	gµρg ,	(2)
where δνµ is the Kronecker delta, with values given by
	 	µ = ν
(3)
	= 0	µ = ν
and where the appearance of a double index such as ρ implies a summation over its range of values. One can then take as the law of motion for φ the equation
	 ,	(4)
where g is the determinant of gµν and ,µ := ∂/∂xµ. The tensor field gµν cannot itself be given as a function of the coordinates directly since in that case Eq. (4) would not be generally covariant. Rather, it must in turn satisfy a law of motionthatisitselfgenerallycovariant.Ifonerequiresthat this law involve no higher than second derivatives of gµν, it can be shown that there are in fact only three essentially different such laws for this object. One can form laws of motion for φ other than Eq. (4), but in each case it is necessary to introduce other geometrical objects for the purpose and to formulate laws of motion for them. In the general theory, gµν is associated with the gravitational field and hence couples to all other physical quantities through their equations of motion.
E. Absolute and Dynamical Objects
To understand the revolutionary nature of the general theory it is necessary to distinguish between two essentially different types of objects that appear in the various space– time theories. We call them absolute and dynamical, respectively. If the totality of values allowed by the laws of motionforsomegeometricalobject,suchasthetensor gµν introduced above are such that they can all be transformed into each other by coordinate transformations, we say that that object is an absolute object in the theory. This can occur if the law of motion for the object does not involve any of the other objects in the theory. The remaining objects in the theory are called dynamical objects. The electric fields associated with different charge distributions, for example, cannot in general be transformed into one another and hence must be associated with a dynamical object.
Given a theory with absolute objects, it is possible to coordinatize the space–time manifold so that they take on a specific set of values. In the case of the tensor gµν, one of the three possible laws of motion mentioned above is such that every set of values allowed by it can be transformedsothat,foreverypointofthespace–timemanifold, gµν =diag(1,−1,−1,−1). If these values are substituted into the other laws of motion they will no longer be generallycovariant,butrathertheywillbecovariantwithrespect tosomesubgroupofcoordinatetransformations.Thissubgroupwillleaveinvariantthechosenvaluesofthegeometrical object (or objects) and will be called the invariance group of the theory. The structure of this group will be independent of which particular set of values allowed by the laws of motion is chosen for the absolute objects. If there are no absolute objects then the invariance group is just the group of all allowed coordinate transformations.
Absolute objects are seen to play a preferred role in a theory—their values are independent of the values of the dynamical objects of the theory while the converse is in general not the case. (If it is, the absolute objects become superfluous and can be ignored.) A theory with absolute objects thus violates a kind of general law of action and reaction. We will see that both Newtonian mechanics and special relativity contain absolute objects while the general theory does not.
II. NEWTONIAN MECHANICS
A. Absolute Time and Space
In his formulation of the laws of motion, Newton introduced a number of absolute objects, chief of which were his absolute space and absolute time. Absolute time corresponds to the foliation of the space–time manifold by a one-parameter family of nonintersecting threedimensional hypersurfaces, which we call planes of absolute simultaneity. All of the points in a given plane are taken to be simultaneous with respect to each other. Furthermore, these planes are such that the curves associated with the trajectories of particles intersect each plane once and only once. The “time” at which such an intersection takes place is characterized by the value of the parameter associated with the plane being intersected. These planes are absolute in that their existence and structure are assumed to be independent of the existence or behavior of any other physical system in the space–time.
In Newtonian mechanics the interaction of particles is assumed to be instantaneous as in Newton’s action-at-adistancetheoryofgravity.Consequently,suchinteractions take place between the points on the trajectories that lie in thesameplaneofabsolutesimultaneity.Asaconsequence, these planes can be observed by giving an impulse to one member of a group of charged particles and noting where, on the trajectories of the other particles, the transmitted impulse acts.
Newton’s absolute space corresponds to a unique threeparameter congruence of nonintersecting curves that fill the space–time manifold; that is, through each point of the manifold there passes one and only one such curve. Furthermore, each curve passes through one and only one pointofeachplaneofabsolutesimultaneity.Theexistence of such a congruence would therefore imply that there exists a unique one-to-one relation between the points in any two planes of absolute simultaneity. The “location” of a space–time point would be characterized by the parameters associated with the curve of the congruence passing through it.
The notion of absolute space brings with it the notion of absolute rest: a particle is absolutely at rest if its trajectory can be associated with one of the curves of the congruence. However, unlike the planes of absolute simultaneity that are needed in the formulation of the laws of motion of material particles, these laws do not require the existence of the space–time congruence of curves that constitute Newton’s absolute space, nor do they afford any way of detecting a state of absolute rest. This property of the Newtonian laws of motion is known as the principle of Galilean relativity. Furthermore, since the congruence is not needed in the formulation of these laws, we can dispense with it and hence with Newton’s absolute space altogether as an unobservable element of the theory.
B. Free Bodies
In his setting down of the three laws of motion, Newton was careful to give the first law, “Every body continues in its state of rest, or of uniform motion in a right line, unless it is compelled to change that state by forces impressed upon it,” as separate and distinct from the second law. He clearly did not consider it, as it is sometimes taken to be, a special case of the second law. In effect, the first law supposes a class of curves, the straight (right) lines, to exist in the space–time manifold. Furthermore, these curves correspond to the trajectories of a class of objects on which no forces act, namely, free bodies. As a consequence, these curves are absolute objects of the theory. Furthermore, they, like the planes of absolute simultaneity, are needed to formulate the laws of motion for bodies on which forces act.
C. Galilean Invariance
One can always coordinatize the space–time manifold in such a way that the parameter t, which labels the different planes of absolute simultaneity, is taken to be one of these coordinates. When this is done, the equation that defines these planes is simply
	t = const.	(5)
Furthermore, the remaining coordinates can be chosen so that the equations of the curves associated with the trajectories of the free bodies are linear in t; that is, they are of the form
	xi = vit + x0i,	(6)
where the index i takes on the values 1, 2, 3, and vi and x0i are constants. The constants vi are the components of the “velocity” of the free body whose trajectory is associated with this curve and the x0i are its initial positions. When expressed in terms of these coordinates, the laws of motion of Newtonian mechanics take on their usual form.
Since the planes of absolute simultaneity and the straight lines constitute the absolute objects of Newtonian mechanics and enter into the formulation of the laws of motion of all Newtonian systems, the subgroup of coordinate transformations that leave them invariant as a whole constitutes the invariance group of Newtonian mechanics. Inadditiontothegroupofspatialrotationsandtranslations and time translations, this group consists of the Galilean transformations given by
	xi = xi + Vit	(7a)
and
	t = t,	(7b)
where the Vi are the components of the velocity that characterize a particular transformation of the group. The requirement of invariance under this group of transformations is called the principle of Galilean relativity.
Intermsoftheprimedcoordinates,weseethattheequations of a straight line (6) take the form
	xi  i,	(8)
where the transformed velocity components vi are given by the Galilean law of addition for velocities:
	vi = vi + Vi.	(9)
III. SPECIAL RELATIVITY
A. Light Cones
The transition from Newtonian mechanics to special relativity in the early part of this century involved the abandonmentoftheNewtonianplanesofabsolutesimultaneity and their replacement by a new set of absolute objects, the light cones. With the completion of the laws of electrodynamics by Maxwell in the middle of the last century it became evident that electromagnetic interactions between charged particles were not instantaneous but rather were transmitted with a finite velocity, the speed of light. This fact,coupledwiththeGalileanvelocityadditionlaw,made itappearpossiblethatsomeelectromechanicalexperiment could be devised for the detection of a state of absolute rest and thus reinstate Newton’s absolute space. However, all attempts to do so, such as those of Michelson and Morley and Trouton and Noble, proved fruitless. In one way or another, these experiments sought to measure the absolute velocity of the earth with respect to this absolute space. Even though they were sensitive enough to detect a velocity as small as 30 km/sec, which is much less than the known velocity of the earth with respect to the galaxy, no such motion was ever detected.
Einsteinrealizedthatifallinteractionsweretransmitted with a finite velocity there was no way objectively to observe the Newtonian planes of absolute simultaneity and that they, like Newton’s absolute space, should be eliminated from the theory. It was his analysis of the meaning of absolute simultaneity and its rejection by him that distinguished his approach to special relativity from those of Lorentz and Poincare. Since, however, unlike absolute´ space, the planes of absolute simultaneity were needed in the formulation of the laws of motion for material bodies, it was necessary to replace them by some other structure. ThekeytodoingthislayinEinstein’spostulatethatthevelocityoflightisindependentofthemotionofthesource.If this is the case, and to date all experimental evidence supports this postulate, the totality of all light ray trajectories form an invariant structure and can be associated with a corresponding family of three-dimensional surfaces in the space–timemanifold,thelightcones.JustasinNewtonian mechanics,wherethrougheachpointtherepassesaunique planeofabsolutesimultaneity,inspecialrelativitythrough each point there passes a light cone that consists of all of the points on the curves passing through this point that correspond to the trajectories of light rays.
InNewtonianmechanicstheinteractionofparticleswas assumed to take place between the points on the curves associatedwiththeirtrajectoriesthatlayinthesameplaneof absolute simultaneity. In special relativity this interaction is assumed to take place, depending on the type of interaction that exists between the particles, either between points that lie in the same light cone or between one such point and points in the interior of the light cone associated with this point. The electromagnetic interaction, for example, takes place between points lying in the same light cone. Consequently, these light cones can be observed by giving an impulse to one member of a group of charged particles and noting where, on the trajectories of the other particles, the transmitted impulse acts.
B. Free Bodies
In addition to the absolute light cones, special relativity assumes, like Newtonian mechanics, a family of curves, the straight lines, that are associated with the trajectories of free bodies. There is, however, an important difference between the two theories. In Newtonian mechanics any straight line that intersects all of the planes of absolute simultaneity is assumed to correspond to the trajectory of afreebody.Inspecialrelativity,ontheotherhand,onlythe straight lines that correspond to free bodies with velocities less than or equal to the speed of light are assumed to correspond to observable free bodies. These straight lines are such that, given a point lying on one of them, the other points lying on it are either interior to or lie on the light cone associated with that point.
C. Lorentz Invariance
Together, the light cones and straight lines constitute the absolute objects of special relativity. It can be shown that one can coordinatize the space–time manifold in such a way that the points with coordinates xµ lying on a straight line are given by the equations
	xµ = vµλ + x0µ,	(10)
where the vµ and x0µ are constants and λ is a monotone increasing parameter along the line. For the straight lines that correspond to the trajectories of free bodies, the vµ are constrained by the condition that
	ηµνvµv	 0	(11)
where ηµν =diag(1,−1,−1,−1). Provided that ηµνvµvν
>0, it is always possible to choose the parameter λ such that ηµνvµvν =1. In this case the vµ are said to constitute the components of the four-velocity of the particle and τ =λ is called the proper time along the line.
In addition to the form (10) for the straight lines, coordinates can be chosen so that the points xµ lying on the lightconeassociatedwiththepoint x0µ satisfytheequation
	 .	(12)
For points interior to this light cone the quantity on the left side of this equation is greater than zero, while for points exterior to it it is less than zero. In what follows, coordinates in which the straight lines and light cones are described by Eqs. (10) and (12) will be called inertial coordinates.
Since the light cones and straight lines are absolute objects in special relativity, the coordinate transformations that leave these structures invariant constitute the invariance group of special relativity. In an inertial coordinate system, these transformations have the form
	x bµ,	(13)
where ανµ and bν are constants. The bµ are arbitrary while the ανµ are constrained to satisfy the conditions
	 .	(14)
These transformations form a group, the inhomogeneous Lorentz group, each member of which is characterized by the 10 arbitrary values one can assign to the ανµ and bµ. This group contains, as subgroups, the threedimensional rotation group and the group of spatial and temporaltranslations.ItalsoincludesthegroupofLorentz transformations,nowcalledLorentzboosts.Aboostalong the x axis takes the form x 
x 
(15)
x 	x x 	x ,
where γ =(1−β2)−1/2 and β is a parameter that characterizes the boost. These transformation equations take their more familiar form if we set xµ =(ct, x, y, z) and similarly for xµ and β =v/c, where c is the velocity of light, in which case v is the velocity associated with the transformation. In special relativity, the Lorentz boosts replace the Galilean transformations of Newtonian mechanics just as the light cones replace the planes of absolute simultaneity and the requirement of invariance under this group is called the principle of Special relativity. Also, the Galilean law of addition for velocities, Eq. (9), is no longervalid.Foraboostinthe x direction,thetransformed components vi of the velocity of a body are related to its original components vi by the equations
	 	 	 ,
(16)
where δ =(1+v1v/c2)−1.
D. The Space–Time Metric
Equations (10) and (12) for straight lines and light cones are given in a special coordinate system in which they assume these simple forms. It is possible to write generally covariant equations for these objects by introducing a symmetric second rank tensor gµν of signature −2 together with its inverse gµν. With its help, the light cones can be characterized by the surfaces φ(x)=0, where φ satisfies the covariant equation
	gµνφ,µφ,ν = 0.	(17)
To construct an equation for a straight line we first introduce the Christoffel symbols  defined by
	 .	(18)
These quantities constitute the components of a geometrical object that is linear but not homogeneous. With their help, the equations for the coordinates xµ(λ) of the points lying on a straight line can now be written as
	d2xµ/d ,	(19)
where again λ is a monotone increasing parameter along the curve. One can choose λ so that gµν dxµ/dλdxν/ dλ=1, in which case it is the proper time along the line. One can also use Eq. (19) to characterize the trajectories of light rays if one adds the condition that gµν dxµ/dλ dxν/dλ=0.Suchrayshavethepropertythattheyserveas the generators of the light cones. Equation (19) is usually referred to as the geodesic equation since it has the same formastheequationforageodesiccurve,thatis,acurveof minimum length connecting two points in a Riemannian space with a metric gµν.
Having introduced the tensor gµν, it now becomes necessary to construct a law of motion for it. In special relativity this law is taken to be
	Rµνρσ = 0,	(20)
where the tensor Rµνρσ, called the Riemann–Christoffel tensor, is constructed from the tensor gµν according to
R (gµρ,νσ + gνσ,µρ − gµσ,νρ − gνρ,µσ)
	 .	(21)
It appears in the equation of geodesic deviation that governs the separation between two neighboring, freely falling bodies. When all of the components of Rµνρσ vanish, this separation remains constant.
It can be shown that every solution of Eq. (20) can be transformed so that gµν =ηµν everywhere on the space– time manifold, in which case gµν is said to take on its Minkowski values. In a coordinate system in which gµν has this form, Eq. (17) becomes
	ηµνφ,µφ,ν = 0	(17a)
It is seen that the surface defined by Eq. (12) satisfies thisequation.Likewise,inthiscoordinatesystem,Eq.(19) reduces to
	d2xµ/dλ2 = 0	(19a)
and has, as its solution, the curves defined by Eq. (16).
Since gµν can always be transformed to its Minkowski values, it is seen to be an absolute object in the theory and the group of transformations that leave it invariant is again the inhomogeneous Lorentz group. In all respects gµν is equivalenttothestraightlinesandlightconesofthetheory. Furthermore, one can either construct laws of motion that employ inertial coordinates and that are covariant with respect to the inhomogeneous Lorentz group or construct generally covariant laws with the help of the gµν. When gµν is transformed to take on the values ηµν, the latter equations reduce to the former.
The Riemann–Christoffel tensor arose in the study of the geometry of manifolds with Riemannian metrics. In such a geometry one defines a distance ds between neighboring points of the manifold with coordinates xµ and xµ + dxµ to be ds2 = gµν (x)dxµ dxν, (22)
where gµν, a symmetric tensor field, is the metric of the manifold. The vanishing of the Riemann–Christoffel tensor can be shown to be the necessary and sufficient condition for the geometry to be flat; that is, the metric can always be transformed to a constant tensor everywhere on the manifold. Since the tensor gµν introduced above is an absolute object it is sometimes referred to as the metric of the flat space–time of special relativity. Although we will not need to make use of this geometrical interpretation, it will sometimes prove convenient to give an expression for ds as a way of specifying the components of gµν.
IV. GENERAL RELATIVITY
A. The Principle of Equivalence
After Einstein formulated the special theory of relativity he turned his attention to, among other things, the problem of constructing a Lorentz-invariant theory of gravity. Newton thought of gravity as an action-at-a-distance force between massive bodies and as transmitted instantaneously between them. Since special relativity required a finite speed of transmission, Einstein sought to construct a relativistic field theory of gravity. The simplest object to associate with the gravitational field was a scalar field. However,adifficultypresenteditselfwhenhecametoconstruct a source for this field. In the Newtonian theory, the gravitational attraction between bodies was proportional to their masses. In special relativity, however, energy has associated with it an equivalent mass through the relation E =mc2. Consequently, Einstein argued, mass density by itself could not be the sole source of the gravitational field. At the same time, energy density could not be used since it is not, by itself, associated with a geometrical object in special relativity but rather with one component of a tensor field.
While thinking about the problem of gravity, Einstein was struck by a peculiarity of the gravitational interaction between bodies, namely, the constancy of the ratio of the inertial to the gravitational mass of all material bodies. In Newtonian mechanics, mass enters in two essentially different ways—as inertial mass in the second law of motion and as gravitational mass in the law of gravitational interaction. Logically, these two masses have nothing to do with one another. Inertial mass measures the resistance of a body to forces imposed on it while gravitational mass determines, in the same way as electric charge determines the strength of the electrical force between charged bodies,thestrengthofthegravitationalforcebetweenmassive bodies. Galileo was the first to demonstrate this constancy by observing that the acceleration experienced by objects in the earth’s gravitational field was independent of their mass. In 1891, Eotv¨ os demonstrated it to an accuracy of¨ one part in 108. More recent determinations by groups in Princeton and Moscow have established this constancy to better than one part in 1011.
While there was no explanation for this constancy, Einstein realized that it called into question the existence of one of the absolute objects of both Newtonian mechanics and special relativity, the free bodies. If indeed this ratio was a universal constant, then there could be no such thingasagravitationallyunchargedbodysincezerogravitationalmasswouldthenimplyzeroinertialmass.Einstein also realized that this constancy meant that it would be impossible to distinguish locally, that is, in a sufficiently small region of space–time, between inertial and gravitational effects through their action on material bodies. An observer in an elevator being accelerated upward with an acceleration equal to that produced by the earth’s gravity would see objects fall to the floor of the elevator in exactly the same way that they fall on earth, that is, with an acceleration that is independent of their mass.
After this realization, Einstein made a characteristic leap of imagination. He postulated that it is impossible to distinguish locally between inertial and gravitational effects by any means. One of the consequences of this postulate, called by him the principle of equivalence, is that light should be bent in a gravitational field just as it would appear to be to an observer in an accelerating elevator. But if this is the case, the light cones of special relativity would no longer be absolute objects either, and this in turn would mean that the metric of special relativistic space–time would not be an absolute object.
The principle of equivalence however, implied even more.Ifinertialandgravitationaleffectsareindistinguishable from each other locally, then one and the same object could be used to characterize both effects. Since it is the metric gµν that is responsible for the inertial effects one observes in special relativity, gµν should also be associated with the gravitational field. In effect, geometry and gravity became simply different aspects of the same thing. Actually, one never needs to interpret gµν as a metric. One can identify it solely with the gravitational field.
This identification has, as a consequence, that gµν must be a dynamical object since the gravitational field clearly must be such. Having recognized this fact, Einstein then turned his attention to the problem of constructing a law of motion for this object.
B. The Principle of General Invariance
In his attempts to construct a law of motion for gµν, Einstein proposed that these laws should be generally covariant. However, we have already seen that the laws of motion of special relativity could be cast in generally covariant form with the introduction of a metric satisfying Eq. (20). But such a metric was absolute and Einstein wanted a law of motion for a dynamical gµν. Consequently,whatEinsteinwasreallyrequiringwasnotgeneral covariance but rather general invariance, that is, that the invariance group of the laws of motion should be the same astheircovariancegroup,namely,thegroupofallarbitrary coordinatetransformations.Aswehavearguedabove,this can be the case only if there are no absolute objects in the theory. The absence of absolute objects in the theory satisfies a version of Mach’s principle which states that there should be no absolute objects in any physical theory.
Although Einstein did not use precisely the reasoning outlined above, it was his recognition of the preferred role played by the inhomogeneous Lorentz group in special relativity that was crucial to the development of the general theory of relativity. And although he formulated his argument in terms of the relativity of motion, it is clear that he was referring to the invariance properties of the laws of motion. His argument that all motion should be relative—hence the term general relativity— was really a requirement, in modern terms, that these laws shouldbegenerallyinvariant.Thisisnotanemptyrequirement, as some authors have suggested, but rather severely limits the possible laws of motion one can formulate for gµν.
C. Dynamic Laws
1. Field Equations
The search for a generally invariant law of motion for gµν occupied a considerable portion of Einstein’s time prior to the year 1915. At one point he even argued that such a law could not exist. However, he did succeed in that year in finally formulating this law. If one requires that this law contain no higher than second derivatives of the gµν and furthermore that it be derivable from a variational principle,thenthereis,infact,essentiallyonlyonelawthat fills these requirements. This is in marked contrast to the situation in electrodynamics, where there are an infinite number of laws of motion for the vector potential Aµ that satisfy these requirements.
To formulate the law of motion for gµν, we first construct from the Riemann–Christoffel tensor (21) the Ricci tensor Rµν, where
Rµν = gρσ Rσµρν
and the curvature scalar R, where	(23)
R = gµν Rµν.	(24)
In terms of these quantities this law can be written as
	Rµν  gµν R + gµν = κTµν,	(25)
where  and κ are constants and Tµν is the energy– momentum tensor associated with the sources of the gravitational field.
In general, the components of the Riemann–Christoffel tensor will not vanish even when all of the components of the Ricci tensor do. As a consequence, it follows from the equationofgeodesicdeviationthattheseparationbetween neighboring freely falling masses will change with time. Since such changes appear due to tidal forces in manypracticle systems, the Riemann–Christoffel tensor is thus a measure of such forces and vice versa.
The so-called cosmological term gµν was originally not present in the Einstein field equations. It was later added by him to obtain a static cosmological model with matter. When it was discovered that the universe was expandingandthatthereweresolutionsofthefieldequations without the cosmological term that fit the then available data, Einstein dropped this term and for the most part it has not been included in the field equations. However, recent data suggest that the expansion of the universe is acceleratinginsteadofslowingdownasitdoesintheolder cosmological models. One way to take into account such a discovery would be to reintroduce the cosmological term in the field equations.
In addition to the law of motion for gµν it is necessary to formulate generally invariant laws of motion for the other geometrical objects that are to be associated with the physical quantities being observed. One way to do this is simply to take over the generally covariant form of the laws formulated for these objects in special relativity. The lawofmotionfortheelectromagneticfield,whenthisfield isassociatedwithavector Aµ,can,forexample,bewritten in the form
	g gµρgνσ F jν,	(26)
where g is the determinant of gµν, jµ the current density associated with the sources of the electromagnetic field, and
	Fµν = Aν,µ − Aµ,ν.	(27)
Such laws of motion are said to involve minimal coupling to the gravitational field. It is also possible to construct laws of motion that do not couple minimally to the gravitational field. In the case of the electromagnetic field, for example, one could include a factor of 1 + R, where R is the curvature scalar, inside the parentheses in Eq. (26). The only requirement these laws of motion should satisfy is that they reduce to their special relativistic form when the Riemann–Christoffel tensor vanishes.
2. Particle Dynamics
When Einstein proposed the general theory in 1915 he took the geodesic Eq. (19) to be the equation of motion for a test particle moving in an external gravitational field. Such a particle was assumed to have no effect on the sources of this external field. Since, however, even a test particle has a finite mass it cannot avoid having some small but finite effect on these sources. Hence, the geodesic equation yields at best an approximation to the true motion of both the test particle. Furthermore, this equation cannot be applied at all in the important case of the mutual interaction of bodies of comparable mass. And finally it cannot deal with gravitational radiation effects.
In 1939 Einstein together with Banesh Hoffmann and Leopold Infeld (hereafter referred to as EIH) made a fundamental advance in the problem of particle dynamics in general relativity. They were able to derive approximate equations of motion directly from the Einstein field equations for slowly moving, compact bodies without the need of additional assumptions. In the lowest, socalled Newtonian approximation, they obtained equations of motion identical in form to those of Newton for compact bodies interacting according to his inverse square law of gravitation. This result shows incidentally that general relativity encompasses all of the results of Newtonian mechanics. The EIH calculations also yielded directly the equivalence of inertial and gravitational masses.
Higher-order, post-Newtonian corrections to these laws correctly predict, among other observed effects, the perihelion advance of the planetary orbits. It is also possible to extend the EIH approximation method to obtain corrections that include the radiation reaction effects that have been observed in binary pulsar systems. Also, this author was able to derive the electromagnetic interaction force law between charged particles from the combined Einstein–Maxwell field equations.
In their original work EIH derived their equations of motion for bodies moving in an everywhere constant (gµν =ηµν) external gravitational field. One can also use their approach to derive approximate equations of motion for compact bodies moving in external fields that are slowly varying in space and time. In particular one can derive an approximate version of the geodesic Eq. (19) for a single body, making it unnecessary to postulate the latter equations.
To better appreciate the significance of the EIH results it is useful to compare the problem of motion in general relativity to that in special relativity and Newtonian mechanics. In those theories one must postulate not only the force law between bodies, such as the Lorentz force law in electrodynamics, but also the form of the inertial terms in the equations of motion for these bodies. General relativity is unique among field theories in that both the force laws and inertial terms follow from the field equations of the theory.
D. Clocks, Rods, and Coordinates
It has been argued that some kind of postulate concerning the behavior of clocks and measuring rods is required in general relativity. For example, it has been suggested that a class of objects, ideal clocks, measure proper time along their trajectories, where the proper time along a trajectory is defined to be the integral of the distance ds, given by Eq. (22), along this trajectory. In this view, clocks, and also measuring rods, are assumed to be primitive objects in the theory.
Actually,allsuchpostulatesareunnecessary,inboththe special and general theories. Clocks, and similarly measuring rods, are, in fact, composite physical systems with laws of motion governing their behavior. Once these laws have been established, there is no need to add additional postulates governing their behavior. It can be shown, for example, that if one takes, as a model for a clock, a classical hydrogen atom, then as long as the forces acting on this clock are small compared to the internal forces acting on its constituents and its dimensions are small compared to the curvature of its trajectory, it will indeed measure approximately the proper time along this trajectory. However, if the forces acting on it are sufficiently strong, the atom will be ionized and cease to measure any kind of time along its trajectory. Thus, the behavior of clocks is seen to be a dynamical question that cannot be decided a priori from any kinematic postulate.
In this view, then, clocks and measuring rods, and indeed all measuring devices, are considered to be physical systems with the geometrical objects associated with them obeying their own laws of motion. Furthermore, a physical description would have to be considered incomplete if it did not supply these laws of motion. To avoid the necessity of having to formulate and solve the laws of motion for a particular kind of clock, one may assume that it does satisfy the conditions for measuring proper time, with the proviso that if these conditions are violated it will no longer do so. If this assumption results in inconsistencies it does not mean that a principle of general relativity has been violated but only that these conditions have not been met.
While clocks and rods can be used to measure times and distances, it should be emphasized that these measurements bear no direct relation to the coordinates employed in the formulation of the laws of motion. Since, in all space–time descriptions, these laws are generally covariant, there are no preferred coordinate systems. Consequently, it follows that the predictions of a theory cannot depend on a particular coordinatization. In effect, the coordinates play the same role in space–time theories as do the indices that characterize the various components of a geometrical object and hence, like these indices, are not associated with any physical objects.
It is, however, often convenient to choose a particular coordinatization. Thus in Newtonian mechanics one usually chooses coordinates such that one of them is the parameter that characterizes the planes of simultaneity, and likewise in special relativity one usually employs inertial coordinates. In general relativity one also can employ a coordinatization that is particularly convenient for some purpose. One can, for example, choose coordinates in such a way that one of them corresponds to the time and distance intervals measured by a particular family of clocks and rods. Alternatively, one can choose coordinates so that certain components of the gravitational field have simple values. For example, one can choose coordinates so that g00 =1 and g01 = g02 = g03 =0. But in all cases such a choice is arbitrary and devoid of physical content.
V. GRAVITATIONAL FIELDS
A. Newtonian Fields
Since Newtonian theory describes, to a high degree of accuracy, the phenomena associated with weak gravitational fields, it is essential that this theory be an approximation to the general theory. Although originally formulated as an action-at-a-distance theory, the Newtonian theory of gravity can also be formulated as a field theory analogous to electrostatics. The gravitational field is characterized, in this version of the theory, by a single scalar field φ that satisfies, in suitable coordinates, the field equation
∇
2
	φ = 4πGρ,	(28)
where ρ is the mass density of the sources of the field and G =6.673 cm3 g−1 sec−2 is the Newtonian gravitational constant. For a point particle of mass m this equation has the well-known solution
	φ = −Gm/r.	(29)
In the general theory we assume that, in the case of weak fields, there exists a coordinate system such that gµν =ηµν +hµν, where hµν 1. We also assume that the velocities of the sources of the gravitational field are all vanishingly small compared to the velocity of light. In this case,theonlynonvanishingcomponentof Tµν is T00 =ρc2 and Eq. (25) can be shown to reduce to Eq. (28) if we set =0,κ =−8πG/c4, where G is the Newtonian gravitational constant, and take
	φ = (c2/2)h00.	(30)
B. The “Flat” Field
The simplest exact solution of the empty-space Einstein equations with vanishing cosmological constant (Eq. (25) with Tµν =0 and =0) is the so-called “flat” field. It satisfiesEq.(20),whencetheappellation“flat,”andinappropriate coordinates takes the form gµν =ηµν. By itself this solution would be rather uninteresting if it were not for the fact that it is the only stationary solution that is asymptotically flat and everywhere regular (no singularities) on the whole space–time manifold −∞≤ xµ ≤∞ as was first shown by A. Lichnerowicz. One consequence of this result is that there do not exist regular, stationary solutions of the empty-space field equations that are asymptotically flat and that could be interpreted as “particle” solutions, that is, solutions that are nonflat only in some localized region of space. Einstein had hoped that such solutions of his field equations existed so that he could dispense with the matter stress–energy tensor Tµν that appears in these equations.
C. The Schwarzschild Field, Event Horizons, and Black Holes
In spite of their enormous complexity, the Einstein field Eq. (25) possesses many exact solutions. One of the first and perhaps still the most important of these solutions was obtained by Schwarzschild in 1916 for the case =0 and Tµν =0 by imposing the condition of spherical symmetry on gµν. The nonvanishing components of gµν are given in spherical coordinates by
g00 = 1 − 2M/r g11 = −1/(1 − 2M/r) g22 = −r2 g33 = −r2 sin2 θ, (31)
where M is a constant of integration. This solution is seen to be independent of the coordinate x0 and hence is a static field. The condition that the field be independent of x0 was originally imposed by Schwarzschild in obtaining his solution of the field equations but has since been shown to be a consequence of the condition of spherical symmetry. The importance of the Schwarzschild solution lies in the fact that it is the general relativistic analog of the Newtonian field (29) of a point mass. By making use of Eq. (30) and Eq. (31) for g00 we see that M = Gm/c2. The constant 2M is refferred to as the Schwarzschild radius of the mass m. The Schwarzschild radius of the sun is 2.9 km and of the earth is 0.88 cm. For comparison, the Schwarzschild radius of a proton is 2.4 × 10−52 cm and that of a typical galaxy of mas∼1045 g is∼1017 cm.
The Schwarzschild field has a property that distinguishes it from the corresponding Newtonian field: at r =2M it becomes singular. Indeed, at this radius g11 is infinite! However, this is not a physical singularity, as Eddington first showed in 1924, but rather what is called a coordinate singularity. A final clarification of the structure of the Schwarzschild field came in 1960 with the work of M. Kruskal. He found a coordinate transformation from the Schwarzschild coordinates (x0,r,θ,φ) to the set (u, v, θ,φ), where
	u = a cosh(x0/4M)	v = a sinh(x0/4M)	(32)
with a =[(r/2M) − 1]1/2 exp(r/4M), such that the transformed components of the Schwarzschild field were given by
	g00 = f	g11 = −f	g22 = −r2
	g33 = −r2 sin2 φ,	(33)
where f =(8M/r)exp(−r/2M). In these latter expressions, r is a function of u and v obtained by solving Eq. (32) for this quantity. In this form the field is seen to be singular only at r =0, which is a true physical singularity.
Figure 1 depicts a number of the features of the Kruskal transformation in what is called a Kruskal diagram. In this diagram, curves of constant Schwarzschild r correspond to the right hyperbolas u2 −v2 =const, while curves of constant x0 correspond to straight lines passing through the origin. The region I to the right of the twor =2M lines corresponds to the entire region r >2M, −∞< x0 <∞.
Hence it follows that the transformation from Kruskal to Schwarzschild coordinates must be a singular transformation, and indeed it is the singular nature of this
 
 
FIGURE 1 Kruskal diagram for the Schwartzschild field. The hyperbola r =0 represents a real singularity of the field.
 
Relativity, General 
transformation that is responsible for the singularity of gµν at r = 2M in Schwarzschild coordinates.
Many of the properties of the Schwarzschild field can be understoodbyreferringtotheKruskaldiagram.InKruskal coordinates, light rays propagate along straight lines at 45◦ with respect to the u, v axes. As a consequence, it is seen that all of the rays emitted at a point P1 in region II above the two lines r = 2M will ultimately reach the singular curver = 0, so no information can be transmitted from this point into region I. Likewise, inward-directed rays emitted at a point P2 in region I will also reach the r = 0 curve while outward-directed rays will continue their outward propagation forever. And finally, some of the rays emitted from a point P3 in region IV below the two lines r = 2M will ultimately reach points in region I while others will reach the region III to the left of the two lines r = 2M.
Because of these features, the surface r = 2M is said to form an event horizon: an observer in region I can never receive information about events taking place in regions II and III of the diagram. In addition, it is seen to be a light cone.
Finally, we note that a material body starting from rest at P2 will fall into the singularity at r = 0 along the dashed path indicated in Fig. 1. Even though it reaches the event horizonat x0 =∞,thepropertimealongthecurvefromP2 to the point where it reaches the singularity is finite. A local observer falling with the particle would notice nothing peculiar as he passed through the horizon. As long as the particle is outside this horizon it is possible to reverse its motion so that it does not cross it. However, once it does its fate is sealed; its motion can no longer be reversed and it will ultimately reach the r =0 singularity in a finite amount of proper time. For this reason the source of a Schwarzschildfieldissaidtobeablackhole—nothingthat falls into it can ever get out again and any radiation generated inside the horizon can never be seen from the outside.
D. Kerr–Newman Fields, Naked Singularities
In addition to the Schwarzschild family of solutions, each member of which is characterized by a value of the parameter M, other stationary solutions of the empty-space Einstein field equations have been found by Kerr and Newman. Like the Schwarzschild solution, the Kerr– Newmansolutionsareasymptoticallyflat;thatis,thevalue of the Riemann–Christoffel tensor goes to zero as the coordinate r approaches infinity and also the physical singularity in the solution is surrounded by an event horizon. This family of solutions is characterized by three continuously variable parameters, which, because of the asymptotic form of these solutions, can be interpreted as the mass, angular momentum, and electric charge of the black hole.
After the discovery of the Kerr–Newman solutions it was shown by the work of Israel, Carter, Hawking, and Robinson that the Kerr–Newman solutions are the only asymptotically flat, stationary black hole solutions, that is, solutions with event horizons that depend continuously on a finite set of parameters. This result is a version of a conjecture of Wheeler to the effect that “a black hole has no hair.” What is still lacking is a proof of uniqueness of the Kerr–Newman solutions, that is, that not more than three parameters is sufficient to characterize completely all stationary, asymptotically flat black hole solutions. To date, the best one can do in this respect is to show that the only such static solutions and the only such neutral solutions belong to the family of Kerr–Newman solutions. In addition to the Kerr–Newman family of solutions there are solutions of the empty-space field equations that do not have event horizons surrounding the physical singularity in the solution. One such solution is obtained by letting the parameter M in the Schwarzschild solution become negative. Also, a charged Schwarzschild field has no horizon if the charge Q < M. In both cases the only singularity occurs at r =0. Because of the absence of a horizon surrounding this point, it is referred to as a naked singularity.
E. Fields with Matter—Gravitational Collapse
In addition to the empty-space solutions discussed here there are numerous solutions of the Einstein equations with nonvanishing energy–momentum tensors. One can, for example, construct a spherically symmetric, nonsingular interior solution that joins on smoothly to an exteriorSchwarzschildsolution.Thecombinedsolutionwould thencorrespondtothefieldofanormalstar,awhitedwarf, or a neutron star. What distinguishes these objects is the equation of state for the matter comprising them. It is surprising that no interior solutions that could be joined to a Kerr–Newman field have been found.
Normalstars,ofcourse,arenoteternalobjects.Theyare supportedagainstgravitationalcollapsebypressureforces whosesourceisthethermonuclearburningthattakesplace at the center of the star. Once such burning ceases due to the depletion of its nuclear fuel, a star will begin to contract. If its total mass is less than approximately two solar masses it will ultimately become a stable white dwarf or a neutron star, supported by either electron or neutron degeneracy pressure. If, however, its total mass exceeds this limit, the star will continue to contract under its own gravity down to a point, a result first demonstrated by Oppenheimer and Snyder in 1939. Although they treated only cold matter, that is, matter without pressure, their result would still hold once the star has passed a certain criticalstageeveniftherepulsionofthenucleicomprising the star were infinite. This critical stage is reached once the radius of the star becomes less than its Schwarzschild radius. When this happens, the surface r =2M becomes an event horizon and the matter is trapped inside, forming a black hole. Even an infinite pressure would then be unable to halt the continued contraction to a point because such a pressure would contribute an infinite amount to the energy–momentum tensor of the matter, which in turn would result in an even stronger gravitational attraction.
Because of the disquieting features of black hole formation (neither Eddington nor Einstein was prepared to accept their existence), theorists looked for ways to avoid their formation. However, theorems of Penrose and Hawking show that collapse to a singularity is inevitable oncethegravitationalfieldbecomesstrongenoughtodrag back any light emitted by the star, that is, when the escape velocity at the surface of the star exceeds the velocity of light.
What has not been proved to date is what Penrose calls thehypothesisof“cosmiccensorship.”Thishypothesisasserts that matter will never collapse to a naked singularity, but rather that the singularity will always be surrounded by an event horizon and hence not be visible to an external observer. While the hypothesis is suported by both numerical and perturbation calculations, it has so far not been shown to be a rigorous consequence of the laws of motion of the general theory.
The detection of black holes is complicated by the fact that they are black—by themselves they can emit no radiation. If they exist at all then, they can be detected only through the effects of their gravitational field on nearby matter. If a black hole were a member of a double star system, it would become the source of intense X rays when its companion expanded during the later stages of its own evolution. As matter from the companion fell onto the blackholeitwouldbecomecompressedandthusheatedto temperatures high enough for it to emit such high-energy radiation. Of course, it is not enough to find an x-rayemitting binary system in order to prove the existence of a black hole. It is also necessary that the mass of the x-ray-emitting component be larger than the upper limit on the mass of a stable neutron star, that is, larger than   denotes a solar mass of 1.99×1030 kg).
The first object to be definitely identified as a black hole in 1971 was a member of a binary system Cygnus X-1 in the constellation Cygnus which was an intense emitter of x-rays. Measurements established that the mass of the compact component of the system was about 8 M. Since then eight more black holes have been found in binary systems. In addition to stellar mass black holes there is now compelling evidence that massive black holes exist in the centers of galaxies. By measurements of the orbital speed of the gaseous disk around the nucleus of the spiral galaxy NGC 4258, Makoto Miyoshi and his collaborators were able to establish in 1995 that the mass of the central object is 4  and its diameter is a half a light year, thereby establishing its identity as a black hole. Our own galaxy has been shown to contain a black hole at its center of mass 2. . To date, there are about 15 masses that have been determined for black holes in the centers of nearby galaxies. The most massive such candidate for a black hole is in the giant elliptic galaxy M87 with an estimated mass of 3  although it is not certain that this object is indeed a black hole. Finally it is now believed that the energy source of quasars is the inflow of vast amounts of gas into massive black holes in the centers of very young galaxies.
F. Gravitational Radiation, the Quadrupole Formula
Shortly after he formulated the general theory, Einstein showed that, when linearized around the flat field gµν = ηµν, the empty-space field equations with zero cosmological constant possessed plane wave solutions similar to the plane wave solutions of electromagnetism. These waves propagate along the light cones defined by ηµν, that is, at thespeedoflight.Liketheirelectromagneticcounterparts, they are transverse waves and possess two independent states of polarization. However, unlike the dipole structure of plane electromagnetic waves, gravitational waves haveaquadrupolestructure,aswouldbeexpectedfromthe tensor nature of the gravitational field. Using coordinates suchthat gµν =ηµν +hµν andthedirectionofpropagation as the z axis, the two states of polarization are characterized by h  and h  with, in the two cases, the other components having the value zero.
Although the empty-space field equations have been shown to possess exact solutions with wavelike properties,theso-calledplanefrontedwaves,neithertheynorthe approximate wave solutions found by Einstein are associated with sources. In electromagnetic theory it is possible to find exact solutions of the field equations associated with sources with arbitrary motions. So far, no such solutions have been found for the highly nonlinear equations of the general theory. In order to construct radiative solutions associated with sources it is necessary to employ approximation methods.
Thefirstattemptstocarryoutsuchapproximationswere made by Einstein and Arthur Eddington. Einstein tried to calculate the energy radiated by a localized system of massesbyintroducingapseudo-energy-momentumtensor for the gravitational field. However, this object was not a true tensor and in fact it was later recognized that it was in generalnotpossibletointroduceatrueenergy-momentum tensorforthegravitationalfield.Asaconsequence,evenif
Relativity, General
itscomponentswereallzeroinonecoordinatesystemthey could be non-zero in some other system of coordinates. Using radiative solutions of the linearized gravitational field equations similar to the Lienard´ –Wiechert solutions of Maxwell’s equations for an arbitrarily moving point charge, he derived the now famous quadrupole formula for the “energy” emitted by these masses. The derivation howeverwasunsatisfactorybecauseofitsuseofapseudotensor to calculate the energy radiated by the system and the assumption that this “energy” loss was equal to the change in the energy of the radiating system. Eddington, on the other hand worked directly with the near field of a spinning rod held together with cohesive forces, which were assumed to be large compared to the gravitational forcesbetweenpartsoftherod.Healsousedthelinearized equations to calculate this field and used it together with the conservation laws derivable from the field equations to calculate the force exerted by one part of the rod on another. He was thus able to calculate the energy loss by the rod without having to make use of Einstein’s pseudotensor. The result he obtained for the rate of energy loss,  kI 2ω6, where k =2.7×10−60 for cgs units, ω is the angular frequency of the rod and I is its moment of inertia about the axis of rotation, agreed with the result obtained by Einstein. Eddington was careful to point out that this result could not be applied directly to systems such as binary stars held together by gravitational forces because in such systems non-linear gravitational effects can not be ignored.
After these initial derivations of Einstein and Eddington, much work went into a satisfactory derivation of the effects of gravitational radiation on gravitationally bound systems. In fact, for a time Einstein and others believed that real gravitational radiation did not exist. Because of the need to take account of the non-linear terms in the field equations many different approximation procedures were employed for this purpose. Today the best that can be done is to use an extension of the EIH procedure using matched asymptotic expansions and multiple time scale methods to calculate these effects. As a consequence these results can only be applied to systems whose component velocities are small compared to the speed of light and for which the separations between the components are large compared to their size. The net result of these calculations is the so-called quadrupole radiation formula dE/dt 
where the angle brackets denote an average over a period of oscillation of the source and the indices i and j take on the values 1 through 3. The quantities Qij are the components of the mass quadrupole moment:
	Qij kl xkxldv,	(35)
where ρ(x) is the mass density of the source. Finally, the quantity E appearing on the left side of this equation is the total Newtonian energy, kinetic plus potential, of the source. As a consequence, the quadrupole formula can be interpreted as an expression of energy conservation, in which case the quantity on its right side becomes the energy carried away by gravitational waves.
The quadrupole formula gives the main contribution to the energy loss of a system due to gravitational radiation. Changes in higher multipoles of the mass will also contribute to this loss, although in general their contribution will be much smaller than that of the quadrupole. However, unlike the electromagnetic case, there is no dipole contribution, since both the total momentum and angular momentum of the radiating system are conserved. And in both theories there is no monopole radiation because of conservation of charge in the one case and conservation of mass in the other.
The amount of energy emitted by slow-motion sources is in most cases very small. A beryllium rod of length 170 m and weighing 6×107 kg, spinning on an axis through its center as fast as it can without disintegrating (ω∼103 sec−1), would radiate energy at the rate of approximately 10−7 erg/sec. For the earth–sun system Eq. (34) yields a rate of energy loss of about 200 W. Only in the case of extremely massive objects moving at high speeds such as in the binary pulsar will the amount of energy radiated be significant.
VI. OBSERVATIONAL TESTS OF GENERAL RELATIVITY
A. Gravitational Red Shift
In general relativity the apparent rate at which clocks run is affected by the presence of a gravitational field. Like its counterpart in special relativity, this is a kinematic effect and hence is independent of any direct effect of the gravitational field on the internal dynamics of the clock. Only if gradients of this field result in tidal forces that are comparable to the nongravitational forces responsible for the functioning of the clock will this internal dynamics be altered.
The amount of red shift is most easily calculated in the case of a static gravitational field and for two clocks that are at rest in this field. We suppose that one clock, the emitter, sends out light waves whose frequency νem is the same as its own frequency. A receiving clock, which is identical in construction to the emitting clock, that is, has the same internal dynamics, is used to measure the frequency νrec of the received radiation. Then it can be shown that
Z := (νrec − νem)/νem = (1/c2)(φem − φrec), (36) where φem and φrec are the gravitational potentials at the locations of the emitter and receiver, respectively. If φem is less than φrec then the quantity Z is negative, hence the emitted light appears to be red shifted. This effect can be understood by noting that, in going from the emiter to the receiver, a photon will, in this case, gain potential energy. Since its total energy is conserved, its kinetic energy, which is proportional to its frequency, will decrease and hence so will its frequency. If either the emitter or receiver is moving with respect to the background field then Eq. (36) must be amended to take account of the Doppler shift produced by such motion.
The first attempts to observe the gravitational red shift were made on the spectral lines of the sun and known white dwarfs. For the sun, Z =−2.12×10−6 while for white dwarfs it would have values 10–100 times as large. In the case of the sun the shift was masked by the Doppler broadening of the spectral lines due to thermal motion. However, observations near its edge are consistent with a redshiftofthemagnitudepredictedbyEq.(36).Inthecase of the white dwarfs, it was not possible to measure their massesandradiiwithsufficientaccuracytodetermineφem, althoughagainredshiftswereobservedwhosemagnitudes were consistent with estimates of these quantities.
The first accurate test of the red shift prediction was carried out in a series of terrestrial experiments by Pound and Rebka in 1960, using the Mossbauer effect. The emit-¨ ter and detector used by them were separated by a vertical height of 74 ft. In this case the gravitational potential can be taken equal to gz, where g is the local acceleration due to gravity and z is the height above ground level. Equation (36) then yields the value Z =2.5×10−15. In spite of its small value, Pound and Rebka were able to observe a shift equal to 1.05±0.10 times the predicted Z. Later experiments with cesium beam and rubidium clocks on jet aircraft yielded similar results.
The possibility of testing the red shift prediction has improved dramatically with the development of highprecision clocks. In 1976 Vessot and Levine used a rocket to carry a hydrogenmaser clock to an altitude of about 10,000 km. Their result verified the theoretical value to within 2 parts in 10−4.
It has been argued that red shift observations do not bear on the question of the validity of general relativity but rather only on the validity of the principle of equivalence. This is, in fact, only partially true. If one assumes that the gravitational field of the earth is uniform over the 74 ft that separated the emitter and receiver of the Pound–Rebka experiment, then indeed their result can be calculated using only this principle. However, one cannot use it alone to determine the result of the Vessot–Levine experiment. In this case it is necessary to make direct use of Eq. (36). The derivation of Eq. (36), however, makes use of Eq. (19) for a light ray, which, in turn, is a consequence of the field equations (25) of general relativity. Also, although the present red shift measurements are not sufficiently accurate to distinguish between different possible equations for the gravitational field, there is nothing in principle that would preclude such a test.
B. Solar System Tests—The PPN Formalism
The first arena used for testing general relativity was the solar system and it remains so to this date. What has changed dramatically over the years, due to the rapid growthoftechnology,isthedegreeofaccuracywithwhich the theory can be tested. It is in the solar system that the gravitational field of the sun is of sufficient strength that deviations from the Newtonian theory are observable, but just barely.
In calculating the size of these effects one assumes that the trajectories of planets and light rays obey Eqs. (19). However,ratherthantakethesun’sgravitationalfieldtobe the Schwarzschild field in evaluating the Christoffel symbols appearing in these equations, it is useful to use what has become known as the parametrized post-Newtonian (PPN) formalism. In this formalism, first developed by Eddington and extended by Robertson, Schiff, Will, and others, one assumes a more general form for the postNewtonian corrections to the gravitational field of the sun than those given by general relativity. These corrections are allowed to depend on a number of unknown parameters that one hopes to determine by solar system and other observations. The reason for proceeding in this manner is that it allows one to test the validity of other competing theories of gravity in which these parameters have different values from those they would have if general relativity were valid.
In the most extreme versions of this formalism as many as 10 parameters are employed. However, a number of these parameters can be eliminated if one requires that the equation of motion (19) are a consequence of the field equations for the gravitational field, as they are in general relativity. Also, some of these parameters are known to be small from other experiments. In what follows we will use anabbreviatedversionofthePPNformalismemployedby Hellings in his analysis of the solar system data. In this version the components of the gravitational field have the form g 
g0i  c	(37b) gij = −(1 + 2γU)δij, (37c)
Relativity, General 
where β,γ, and α1 are PPN parameters U  2 is the Newtonian gravitational potential of the sun, and R and M are the radius and mass of the sun. Included in Eq. (37a) is a term proportional to J2, a dimensionless measure of the quadrupole moment of the sun. In this term P2 is the Legendre polynomial of order 2 and θ is the angle between the radius vector from the sun’s center and the normal to the sun’s equator. The so-called preferred frame velocity wi is taken to be the average of the determinations of the solar system velocity relative to the cosmic blackbodybackground.Ingeneralrelativity β =γ = 1and α1 = 0.
1. Bending of Light
One of the more spectacular confirmations of the general theory came in 1919, when the solar eclipse expedition headed by Eddington announced that they had observed bending of light from stars as they passed near the edge of the sun that was in agreement with the prediction of the theory. Derivations of the bending that use only the principle of equivalence or the corpuscular theory of light predict just half of the bending predicted by the general theory.
The angle of bending for light passing at a distance d from the center of the sun can be computed by using the equation of motion (19) with gµν dxµ/d λ dxν/d λ= 0. Using the form for the gravitational field given by Eq. (37), the angle of bending is given by
	 = (1 + γ )2GM . 	(38)
For light that just grazes the edge of the sun   when γ = 1. Because of this small value it is necessary to observe stars whose light passes very close to the edge of the sun, and this can be done only during a total eclipse. The apparent positions of these stars during the eclipse are then compared to their positions when the sun is no longer in the field of view in order to measure the amount of bending. Unfortunately, such measurements are beset with a number of uncertainties. Thus the measurements made by Eddington and his co-workers had only 30% accuracy. The most recent such measurements were made during the solar eclipse of June 30, 1973, and yielded the value
	 . 	(39)
The use of long-baseline and very-long-baseline interferometry, which is capable in principle of measuring angular separations and changes in angle as small as 3 × 10−4, has made possible much more accurate tests of the bending of light. These techniques have been used to observe a number of quasars such as 3C273 that pass very close to the sun in the course of a year. Beginning in 1970, these observations have yielded increasingly accurate determinations, and the most recent, in 1984, agrees with the general relativistic prediction to within 1%.
2. Time Delay
In passing through a strong gravitational field, light not only will be red shifted but also will take longer to traverse a given distance than it would if Newtonian theory were valid.Thereasonforthisdelayisthatthegravitationalfield acts like a variable index of refraction, so the velocity of light will vary as it passes through such a field. This effect was first proposed by Shapiro in 1964 as a means of testing general relativity. It can be observed by bouncing a radar signal off a planet or artificial satellite and measuring its round-trip travel time. At superior conjunction, when the planet or satellite is on the far side of the sun from the earth, the effect is a maximum, in which case the amount of delay is given by
 
	, 	(40)
where rc, rp, and d are, respectively, the distance from the sun to the earth, the distance from the sun to the target, and the distance of closest approach of the signal to the center of the sun. Since one does not have a Newtonian value for the round-trip travel time with which to compare the measured time it is necessary to monitor the travel time as the target passes through superior conjunction and look for a logarithmic dependence.
The use of a planet such as Mercury or Venus as a target is complicated by the fact that its topography is largely unknown. As a consequence, a signal could be reflected from a valley or a mountaintop without our being able to detect the difference. Such differences can introduce errors of as much as 5 µsec in the round-trip travel time. Artificial satellites such as Mariners 6 and 7 have been used to overcome this difficulty. Furthermore, since they are active retransmitters of the radar signal they permit an accurate determination of their true range. Unfortunately, fluctuations in the solar wind and solar radiation pressure produce random accelerations that can lead to uncertainties of up to 0.1 µsec in the travel time. Finally, spacecraft such as the Mariner 9 Mars orbiter and the Viking Mars landers and orbiters have been used as targets. Since they are anchored to the planet they will not suffer such accelerations. The most recent measurements by Reasenberg et al. in 1979 have yielded a value
	(1 + γ)/2 = 1.000 ± 0.001.	(41)
3. Planetary Motion
Long before the general theory was proposed, it was known that there was an anomalous precession of the perihelion (distance of closest approach to the sun) of the planet Mercury that could not be accounted for on the basis of Newtonian theory by taking into consideration the perturbations on Mercury’s orbit due to the other planets. At the end of the last century, Newcomb calculated this residual advance to have a value of 41  09 of arc per century.
The field values given by Eq. (37) and the equation of motion(19)togetheryieldanexpressionfortheperihelion advance per period that is given, to an accuracy commensurate with the accuracy of the observations, by
 
	 ,	(42)
where p =a(1−e2) is the semi-latus rectum of the orbit, a its semimajor axis, and e its eccentricity. Using the best current values for the orbital elements and physical constants for Mercury and the sun, one obtains from Eq. (38) a perihelion advance of 42 p of arc per century, where
 
The measured value of the perihelion advance of Mercuryisknowntoaprecisionofabout1%fromopticalmeasurements made over the past three centuries and of about 0.5% from radar observations made over the past two decades. If one assumes that J2 has the value ∼1×10−7, whichitwouldhaveifitweretheconsequenceofcentrifugal flattening due to a uniform rotation of the sun equal to its observed surface rate of rotation, then, using this value, Shapiro gives
	 ,	(43)
which is in excellent agreement with the prediction of general relativity.
This agreement has been called into question by some researchers, notably Dicke and Hill. Observations of the solar oblateness by Dicke and Goldenberg in 1966 led them to conclude that J2 actually has a value of (2.47±0.23)×10−5, leading to a contribution of about 4 per century to the overall perihelion advance. If true, this would put the prediction of general relativity into serious disagreement with the observations. On the other hand, it would agree with the prediction of the Brans– Dicke scalar tensor theory of gravity if an adjustable parameter in that theory were suitably chosen. However, a number of authors have disagreed with the interpretation of their observations by Dicke and Goldenberg. These authors argue that the observations could equally well be explained by assuming a standard solar model with J2 ∼10−7 and a surface temperature difference of about 1◦ between the pole and the equator. More recently Hill has given a value of J2 =6×10−6, based on his measurements of normal mode oscillations of the sun. If true, the general relativistic prediction for Mercury would be inconsistent with the observed value by about two standard deviations. Unfortunately, the present measurements of the orbit of Mercury are not sufficiently accurate to separate the post-Newtonian and quadrupole effects.
A resolution of this difficulty has come from an analysis of the ranging data for the planet Mars. Since the quadrupole contribution to the perihelion advance has a differentdependenceonthesemimajoraxisfromthegravitational effect, it is in principle possible to separate the twobyobservingtheadvancefordifferentplanets.Inspite of the smallness of these effects on the orbit of Mars, the accuracy of the Viking data from Mars, which are accurate to within 7 km, combined with the radar data from Mercuryallowssuchadetermination.Usingasolarsystem model that includes 200 of the largest asteroids. Hellings has found, with J2 =0, that
β − 1 = (−0.2 ±1.0) × 10−3	(44a)
γ − 1 = (−1.2 ±1.6) × 10−3	(44b)
α1 = (2.2 ±1.8) × 10−4.	(44c)
When J2 was allowed to have a finite value, he found that
and	J2 = (−1.4 ±1.5) × 10−6	(45a)
	β − 1 = (−2.9 ± 3.1) × 10−3	(45b)
	γ − 1 = (−0.7 ± 1.7) × 10−3	(45c)
	α1 = (2.1 ± 1.9) × 10−4.	(45d)
Hellings also used these data to analyze the nonsymmetric gravitational theory of Moffat, which was consistent with the Mercury data and Hill’s value for J2. The result was
that
	J2 = (1.7 ± 2.4) × 10−7.	(46)
From these results it appears that the predictions of general relativity are confirmed to about 0.1%. However, by a suitable adjustment of parameters, several competing theories also share this property. What distinguishes general relativity from these other theories is that, aside from the value for the gravitational constant G, it contains no other adjustable parameters.
4. Time Varying G
In addition to the tests discussed above, the solar system datacanbeusedtotestthepossibilitythatthegravitational constant varies with time. Such a possibility was first suggested by Dirac in 1937 on the basis of his large number hypothesis. He observed that one could form, from the atomicandcosmologicalconstants,severaldimensionless numberswhosevalueswerealloftheorderof1040.Rather
 
than being a coincidence that was valid only at the present time, Dirac proposed that the equality of these numbers was the manifestation of some underlying physical principle and that they held at all times. Since one of these numbers involves the present age of the universe through its dependence on the Hubble “constant” and hence decreases as one moves back in time, the other constants must also change with time in order to maintain the equality between the large numbers. One of these numbers, however, involves only atomic constants, being the ratio of the electrical to the gravitational force between an electron and a proton. Hence the Dirac hypothesis requires that one of these atomic constants must be changing on a cosmic time scale. The constant that is usually taken to vary with time in theoretical implementations of the large number hypothesis is the gravitational constant.
There are several ways of constructing a theory with an effective time-varying gravitational constant. In the Brans–Dicke theory, the effective gravitational constant itself varies with time:
	Geff = G[1 + (G˙/G)(t − t0)].	(47)
An alternative proposal by Dirac assumed that cosmic effects couple to local atomic physics so that the ratio of atomic to gravitational time is not constant. The rate of change of gravitational time τG with respect to atomic time τA is then given as
	dτG/dτA = 1 + φ˙(t − t0),	(48)
where φ is some cosmological field that is supposed to be responsible for the effect. In both cases, the net effect is to produce an anomalous acceleration in the equations of motion for material bodies.
Since the change in atomic constants is tied to cosmic evolution in the large number hypothesis, the expected rate of change in G should be proportional to the inverse Hubble time:
	G˙/G − H0 ∼= 5 ×10−11 year−1	(49)
On the basis of the Viking lander data, Hellings concludes that
	G˙/G = (0.2 ± 0.4) × 10−11 year−1	(50a)
	φ˙ = (0.1 ± 0.8) × 10−11 year−1	(50b)
Since these limits are an order of magnitude smaller than what one would expect from simple cosmic scale arguments, they cast serious doubt on the large number hypothesis.
C. The Binary Pulsar
Anew,andessentiallyunique,opportunityfortestinggeneral relativity came with the discovery of the binary pulsar PSR 1913+16 by Hulse and Taylor in 1974. It consists of a pulsar in orbital motion about an unseen companion with a period of 7.75 hr. Its relevance for general relativity is twofold: because v2/c2 ∼5×10−7 is a factor 10 larger than for Mercury, relativistic effects are considerably larger than any that have been observed in the solar system.Also,theshortperiodamplifiessecularchangesin the orbit. Thus the observed periastron advance amounts to4◦.2261±0.0007ofarcperyearcomparedtothe43 of arc per century for Mercury. Furthermore, the pulsar carries its own clock with a period that is accurate to better than one part in 1012. As a consequence, measurements of post-Newtonian effects can be made with unprecedented accuracy. If this were all, the binary pulsar would still be an invaluable tool for testing general relativistic orbit effects. However, it also provides us for the first time with a meansfortestinganessentiallydifferentkindofprediction of general relativity, namely the existence of gravitational radiation.
Considerable effort has gone into identifying the pulsar companion. It was soon found that the pulsar radio signals were never eclipsed by the companion. Also, the dispersion of the pulsed signal showed little change over an orbit, implying the absence of a dense plasma in the system. These two facts together ruled out the possibility of the companion being a main sequence star. Another possibility is that it is a helium star. However, since the pulsar is at a distance of only about 5 kpc from us, such a star would have been seen. In spite of intense efforts, no such star has been observed in the neighborhood of the pulsar. The remaining possibility is that it is a compact object, either a white dwarf, another neutron star, or a black hole.
In the case of conventional spectroscopic binaries, it is usually possible to measure only two parameters of the system, the so-called mass function of the two masses M1 and M2 of the components and the product of the semimajor axis a1 and the sine of the angle i of inclination of the plane of the orbit to the line of sight. However, in the case of the binary pulsar one can use general relativity to determineallfouroftheseparametersfrommeasurements of the periastron advance and the combined second-order Doppler shift and gravitational red shift of the emitted signals. One finds from these combined measurements that M . From the fact that the
Chandrasekhar limit on the mass of a nonrotating white dwarf is about 1. , it appears likely that the unseen companion is either a neutron star or a black hole.
In addition to the measurements discussed above, it was discovered that the orbital period P was decreasing with time. Later measurements gave a value for P˙ =(−2.30 ± 0.22)×10−12 sec/sec−1 or about 7×10−5 sec/year. If one computes the period change due to loss of energy by the emission of gravitational radiation using the quadrupole formula (34) one obtains a value for P˙ =−2.40×
10−12 sec/sec−1, in excellent agreement with the observed value.
Of course, there are other effects that could change the orbitalperiod,suchastidaldissipation,masslossoraccretion onto the system, or acceleration relative to the solar system. Furthermore, there could be other contributions to the periastron advance such as rotational or tidal deformation of the companion. Only in the case of a helium-star companion would any of these effects contribute significantly to the calculated or observed period change. Furthermore, it would be truly remarkable if some combination of these effects should conspire to give a value for the period change equal to that predicted by the quadrupole formula. It therefore appears safe to say that for the first time we have evidence of a qualitatively new prediction of general relativity, namely gravitational radiation. Finally, the data from the binary pulsar seem to rule out a number of competing theories of gravity such as the Rosen bimetric theory. In such theories this system can radiate dipole gravitational waves that result in a period increase. Only a very artificial mechanism could then give rise to the observed period decrease.
D. Gravitational Wave Detection
The first comprehensive attempt to detect gravitational waves impinging on the earth was begun by J. Weber in 1961. His antenna consisted of a large aluminum cylinder ∼1.5 m long with a resonant frequency of∼1660 Hz. In the early 1970s Weber announced the detection of coincident pulses on two of these antennae separated by a distance of ∼1000 mile. However, attempts to duplicate these results by a number of other groups, using somewhat more sensitive detectors than those used by Weber, proved fruitless, and it is now generally agreed that the events recorded by Weber were not caused by gravitational waves.
Since Weber’s pioneering efforts, about 15 different groups from around the world have undertaken the construction of gravitational wave detectors. The sensitivity of a detector can be expressed in terms of the smallest strain L/L, where L is a change in the length L of the detector, that can just be measured. This change in length is produced by tidal forces associated with the incident gravitational wave and hence its measurement leads to a determination of the Riemann–Christoffel tensor of the wave. Since this strain is approximately equal to the dimensionless amplitude h of a gravitational wave incident onthedetector,thesensitivityofadetectorisusuallygiven as the minimum value of h that can be detected.
The original Weber bars had a sensitivity h ∼10−16. At present one of the main limitations on the sensitivity of Weber bars is thermal noise. As a consequence, secondgeneration Weber bars are being constructed that will be cooled to liquid helium temperatures. Such bars are estimated to have sensitivities of h ∼10−19. It is technically feasible to construct bars for which h ∼10−21, although that would require cooling to the millidegree level. The latter value appears to be a lower limit to what can be attained with presently available technology.
One of the drawbacks of Weber bar detectors is that they are only sensitive to the Fourier component of the incoming signal whose frequency is equal to the resonant frequency of the bar. Furthermore, most bars have resonant frequencies in the kiloherts range with a smallest reported frequency of 60.2 Hz. Unfortunately, most continuous wave sources such as binary star systems have much lower frequencies. In an attempt to overcome this difficulty and to increase sensitivity, a number of groups have undertaken the construction of laser interferometer detectors. In these devices, a gravitational wave would change the lengths of the interferometer arms and one would measure the resulting fringe shifts. Such detectors can, in principle, record the entire waveform of an incoming wave rather than a single Fourier component. It is possible that sensitivities as low as h ∼10−22 might be achieved. The most ambitious of these projects to date is the LIGO (for laser interferometer gravitational wave observatory) project which is building two such detectors in the United States and is expected to go on line in the next few years. It has also been suggested that gravitational radiation could be detected by the accurate Doppler tracking of spacecraft. Such a scheme would, in principle, be able to detect waves with frequencies in the 1 to 10−4 range. Present technology is within one or two orders of magnitude of the sensitivity needed to detect possible signals in this frequency range.
Possible sources of gravitational waves can be divided into two groups, those that emit continuously and those that emit in bursts. Possible continuous wave sources are binary stars and vibrating or rotating stars. In the case of binary stars, the strongest emitter known is µ Scorpii, for which h =2.1×10−20. However, its frequency is 1.6×10−5 Hz. The largest binary frequency known is 1.9×10−3 Hz. However, for this system h ∼5×10−22.
Other possible continuous wave sources have values for h that are this small or smaller. Thus, estimates of h for waves from the Crab and Vela pulsars are of order 10−24 to 10−27, at frequencies between 10 and 100 Hz. In spite of these low amplitudes, signal integration over an extended time can effectively increase the sensitivity of a detector by an order of magnitude or more, so the detection of such signals is not totally out of the question.
Bursts of gravitational radiation can be expected to accompany cataclysmic events such as supernova explosions, stellar collapse to form neutron stars or black holes, or coalescence of the neutron stars or black holes in a binary system at the end stage of its evolution. One of the problems in dealing with such systems is the determination of the efficiency with which other forms of energy can be converted into gravitational radiation. Estimates range from a maximum of 0.5 to as low as 0.001. Such events would have characteristic frequencies in the range 102 to 105 Hz and those occurring in our galaxy would have amplitudes estimated to be in the range h ∼10−18 to 10−17. Here the problem for detection is not so much the frequency or the intensity, as it is in the case of continuous emitters, but rather the scarcity of such events. Thus, the supernova rate in our galaxy has been estimated to be 0.03 per year. If one includes such events in other galaxies the rate increases. For example, at a distance of 10 Mpc the estimated supernova rate is one per year. However,thecorrespondingamplitudewouldbeh ≈3×10−21 to 3×10−20.
By combining the sensitivity estimates for gravitational wave detectors now under construction and the expected amplitudes and frequencies of possible sources we see that the possibility for detection in the near future is good. Furthermore, as the technology improves, an era of gravitational wave astronomy may soon be possible. Since gravitational waves are not absorbed by intervening matter as is electromagnetic radiation, such an astronomy may allow us to explore regions of the universe, such as the centers of galaxies, that are now blocked to our view.
E. Gravitational Lenses
In many of its effects, a gravitational field acts like a medium with a variable index of refraction. Thus, two of the observed effects discussed above, the bending of light and the time delay of signals as they pass through a gravitational field, can be understood on this basis. A further consequence of this notion is that there should exist gravitational lenses with properties similar to those of ordinary optical lenses. The most likely candidates for such lenses are galaxies. If placed between us and a distant point source such as a quasar, a galaxy can, in effect, provide more than one path along which light from the source may reach the observer. As a consequence, one would see multiple images of the source. Applied to a galaxy, the bending formula (38) (with γ =1) gives typical bending angles of about 1 arcsec.
The first gravitational lens, predicted by Einstein in 1936,wasobservedin1979.In1998acomplete‘Einstein’ ring was observed and the Californian-Arizona Space Telescope Lens survey lists 43 probable examples of lensing including the most distant galaxy so far observed. In addition, a study of the multiple images produced by the light passing through a galactic cluster has enabled astronomers to calculate the mass distribution in this cluster including the contribution due to ‘dark matter.’
VII. GRAVITY AND QUANTUM MECHANICS
A. Hawking Radiation and Black Hole Thermodynamics
For most of its history, general relativity has stood apart from quantum mechanics. Early attempts to quantize the gravitational field proved to be largely unsuccessful and quantum theory usually neglected the presence of gravitational fields. For most problems one could justify this neglect. The radius of the first Bohr orbit of a hydrogen atom held together by gravitational rather than electrical forces, for example, would be about 5×1030 m, which is almost four orders of magnitude larger than the radius of the visible universe! However, one is not justified in ignoring the effects of strong gravitational fields, such as those that occur near the Schwarzschild radius of a black hole, on the behavior of quantum systems since gravity couples universally to all physical systems. When one takes account of the gravitational field in the quantum description of a system, qualitatively new features emerge. One such feature is the phenomenon of Hawking radiation.
Even in the vacuum, where there are no real quanta, pairsofvirtualquantaofthevariousmatterfieldsobserved in nature are being continually created and destroyed in equal numbers. Their presence is manifested in such phenomena as the Lamb shift in hydrogen and the Casimir effect. According to Hawking, a black hole can absorb one member of such a virtual pair, leaving its partner to propagateasarealquantumofthefield.Theenergyneeded for this process to occur is supplied by the gravitational energy of the black hole. Hawking was able to show that, asablackholeformed,suchafluxofrealquantashouldbe produced and that it would be equal to the flux produced by a hot body of temperature T given by
	kT = hg/2πc,	(51)
where k is Boltzmann’s constant, h is Planck’s constant, and g isthegravitationalaccelerationattheSchwarzschild radius of the black hole and is equal to c4/4GM, where M is its mass.
For a solar mass black hole this temperature would be 2.5×10−6 K. However, for a 1012 kg mass black hole it wouldbe5×1012 K.Suchablackholewouldemitenergy at a rate of about 6000 MW, mainly in gamma rays, neutrinos, and electron–positron pairs. Hawking has suggested that “primordal black holes” with such masses might have been formed by the collapse of inhomogeneities in the very early stages of the universe and that some of them might have survived to the present day. If so, they probably represent our only hope of observing Hawking radiation. However, measurements of the cosmic-ray background around 100 MeV place an upper limit for black holes with masses around 1015 kg of about 200 per cubic light-year.
The fact that a black hole can radiate real quanta might seem to contradict the fact that no radiation can escape from a black hole. However, that restriction is only true classically. One can think of the emitted radiation as having come from inside the event horizon surrounding the black hole by quantum mechanically tunneling through the potential barrier created by its gravitational field. Actually, it is possible for a black hole to emit almost any configuration of quanta, including macroscopic objects. Since we cannot have direct knowledge of the interior of a black hole, all we can determine are the probabilities for the emission of such configurations. The overwhelming probability is that the emitted radiation is thermal with a temperature given by Eq. (50).
That a black hole should have associated with it a temperature fits in with some analogies between black holesandthermodynamicsdiscoveredbyBardeen,Carter, Hawking, and Bekenstein. If the energy density of the matter that went to make up the black hole is nonnegative, it can be shown that, classically, the surface area of the event horizon surrounding it can never decrease with time. Moreover, if two black holes coalesce to form a single black hole, the area of its event horizon is greater than the sum of the areas of the event horizons surrounding the two original black holes. These properties are very similar to those of ordinary entropy. Furthermore, when a black hole forms, all information concerning its structure except its mass, charge, and angular momentum is lost, and when ordered energy is absorbed by a black hole it too is forever lost to the outside world. These considerations led Bekenstein to associate with a black hole an entropy S given by
	S = ckA/4h,	(52)
where A is the surface area of the event horizon surrounding the hole.
The existence of Hawking radiation raises the question of the ultimate fate of a black hole. As it radiates, its mass decreases. Its temperature therefore increases, and hence so does the rate of emission of radiation. What is left is, at this point, speculation. It might disappear completely, it might cease radiating when its mass reaches some critical value,oritmightcontinueradiatingindefinitely,creatinga negative-mass naked singularity. While the latter two possibilities seem unlikely, the first one implies that whatever matter went into making the black hole initially would simply cease to exist. In deriving the emission from black holes, the gravitational field was treated classically while the matter fields were treated quantum mechanically. It has been suggested that when the mass of the black hole becomes comparable to the Planck mass (MP), that is, the mass one can form from the constants c,h, and G, namely, (hc/G)1/2 ∼5×10−15 g, the gravitational field can no longer be treated as a classical field. If so, the fate of a black hole will be decided only when we have a consistent theory of quantum gravity.
B. Quantum Gravity
The search for a consistent quantum theory of gravity still stands as a major challenge for physics. Because of the extreme weakness of the gravitational force compared to the other fundamental forces in nature, the electro-weak and the strong, it is clear that the quantum effects of gravity would manifest themselves only at extremely short distances and correspondingly high energies. It has been argued that one measure of such a distance is the so-called Plank length L P formed from G,h, and c and given by
	L P   m,	(53)
sincethisistheradiusatwhichtheComptonwavelengthof a black hole is equal to its Schwarzschild radius. To probe such a small length would, it is further argued, require energies of the order of a Plank mass which, in energy units is about 1018 GeV. Thus one might expect that the effects of “quantum gravity” would become important for instance when the radius of the early universe was of the orderofaPlanklength.Putanotherway,onewouldexpect that the laws of classical gravity would no longer be applicable within such small distances so that any attempt to describe the evolution of the universe during this “Plank” era would require some kind of quantum theory of gravity. Furthermore the search for a “unified” theory of elementary particles could not be considered complete without the inclusion of the gravitational field and since such a theory must, of necessity be a quantum theory, it must include a quantum theory of gravity. The other argument for quantizing the gravitational field is that, if it were strictly a classical field, one would be able to determine both the position and momentum of its sources simultaneously and thus violate the uncertainty principle.
One possible approach to the construction of a quantum theory of gravity is to proceed along the lines used to quantize other fields such as the electromagnetic field. One constructs a Hamiltonian version of the theory and then applies the rules of quantum mechanics. The fields and their conjugate momenta are taken to be operators andonewritesdownanappropriateSchrodingerequation.¨ However,whenoneattemptstoapplythisprescriptionone runs into apparently insurmountable difficulties. The classical Hamiltonian theory possesses a number of so-called constraint equations, algebraic relations between the field variables and their conjugate momenta, which have been studied by Peter Bergmann and his students and by Paul Dirac.Theseconstraintsaregeneratorsoftheinfinitesimal coordinate transformations under which the theory is invariant and as such must satisfy a specific Poisson bracket algebra.Unfortunately,inthequantizedversionofthetheory using the gravitational field as the basic field variables no factor ordering of the constraints satisfies an analogous commutation algebra. Furthermore, only “observables,” i.e., quantities that are themselves invariant under the invariant transformations of the theory are quantized. The problem of finding such observables in general relativity is a still an unsolved problem.
If, on the other hand, one proceeds to quantize the linear Einstein equations and treat the nonlinear terms as perturbations one also runs into serious difficulties. As in all quantum field theories one encounters divergent integrals. In successful theories such as quantum electrodynamics where there only a finite number of such integrals, they can be “renormalized” away. However, in the gravitational field case one encounters new divergent integrals at each new order of approximation making the theory non-renormalizable.
In recent times there have been several new attempts to construct a quantum theory of gravity. One such approach is supergravity.
It is an extension of supersymmetric quantum field theory in which every boson in the theory has associated with it a fermion and vice versa. Furthermore, the theory is invariant under the interchange of bosons and fermions. Such theories have been used to construct a unified theory of the strong and electroweak interactions between elementary particles. In supergravity, one associates a spin 3/2 particle called the gravitino with the quantum of the gravitational field. This theory has been shown to have no logarithmic divergences in the lowest two orders of perturbation theory even when gravity is coupled to matter. Whether supergravity or one of its extensions proves to be a viable theory is a matter for future investigation.
The two most recent attempts to construct a quantum theory of gravity are Superstring theory and canonical (Hamiltonian) quantization using so-called Ashtekar variables. Both approaches show considerable promise at this time. Superstring theory replaces the point particles of quantum field theory by strings, membranes or higher dimensional extended structures called p-branes. In these theories p-brane excitations correspond to particle states and since one of these excitations corresponds to a massless spin 2 state, that state was identified with a graviton, the putative quanta of the gravitational field. Also, the metric used to construct the string or p-brane action must satisfy the Einstein equations, albeit in eleven or more dimensions,inordertoinsurethecancellationofadilational anomaly in the theory. Most recently it was shown by A. Strominger and C. Vafa that by counting the energy levels of the superstring gravitational field for a black hole one obtains the Bekenstein formula (52) for the entropy of a black hole. What is still lacking in the theory at this time however is a reduction, in some classical limit, of the full Einsteinfieldequations.Suchaderivationwouldshowjust howtheclassicalgravitationalfieldarisesasan‘emerging’ property of a more basic underlying structure in much the same way as the hydrodynamic variables of fluid mechanics arise from the Boltzmann equation, which itself arises from classical many-body theory. It might even show how the very notion of a space-time point arises from such a structure.
The Ashtakar approach to constructing a theory of quantum gravity is much less radical than that taken by string theory. Ashtakar starts from the classical Einstein equations but rather than working with the gravitational field as the fundamental variable he tries to recast the theory into a form resembling a Yang-Mills gauge quantum field theory. In effect he uses the connection which, in terms of the field gµν is given by Eq. (18) and an additional tetrad field. In addition the connection is complexified, that is, treated as a complex field. They resulting field equations, though equivalent to the Einstein equations as far as their physical content is concerned, have the form of Yang-Mills equations. As in the hamiltonian version of the Einstein equations, the Ashtakar variables satisfy a number of algebraic constraints. These latter constraints however are not as formidable as those between the gµν and their conjugate momenta and it appears that they can by solved nonperturbatively.
Thetwoapproaches,stringtheoryandcanonicalquantizationusingAshtakarvariables,appeartobeincompatible sincetheformerisbasedonelementaryexcitations(gravitons) while the latter, being nonperturbative, does not. At present, however, the physical consequences of neither theory have been explored sufficiently to allow one to decide if indeed they are equivalent or whether in fact either one agrees with observation.
SEE ALSO THE FOLLOWING ARTICLES
CELESTIAL MECHANICS • COSMOLOGY • GRAVITATIONAL WAVE PHYSICS • MANIFOLD GEOMETRY •
MECHANICS, CLASSICAL • MOSSBAUER¨	SPECTROSCOPY
•	QUANTUM MECHANICS • QUANTUM THEORY • RELATIVITY, SPECIAL • STELLAR STRUCTURE AND EVOLUTION
•	X-RAY ASTRONOMY
BIBLIOGRAPHY
Anderson, J. L. (1967). “Principles of Relativity Physics,” Academic Press, New York.
Bergmann, P. G. (1968). “The Riddle of Gravitation,” Scribner’s, New York.
Bertotti, B., de Felice, F., and Pascolini, A. (eds.) (1984). “General Relativity and Gravitation,” Reidel, Dordrecht, Netherlands.
Blair, D. G., and Buckingham, M. J. (eds.) (1989). “Fifth Marcel Grossman Meeting on Recent Developments in General Relativity,” World Scientific, New Jersey.
Cooperstock, F. I. (ed.) (1990). “Developments in General Relativity,” I.O.P., Bristol, U.K.
Evans, C. R., Finn, L. S., and Hobill, D. W. (eds.) (1989). “Frontiers in
Numerical Relativity,” Cambridge University Press, Cambridge, U.K.
Hawking, S. W. (1988). “A Brief History of Time,” Bantam Books, New York.
Hawking, S. W., and Israel, W. (eds.) (1979). “General Relativity,” Cambridge University Press, Cambridge, U.K. Hawking, S. W., and Israel, W. (eds.) (1987). “300 Years of Gravitation,” Cambridge University Press, Cambridge, U.K.
Kaufman, W. J., III. (1977). “The Cosmic Frontiers of General Relativity,” Little, Brown, Boston, MA.
Misner, C. W., Thorne, K. S., and Wheeler, J. A. (1971). “Gravitation,” Freeman, San Francisco.
Rindler, W. (1977). “Essential Relativity,” 2nd ed., Springer Verlag, New York.
Sexl, R., and Sexl, H. (1979). “White Dwarfs, Black Holes,” Academic Press, New York.
Smarr, L. (ed.) (1979). “Sources of Gravitational Radiation,” Cambridge University Press, Cambridge, U.K.
Thorne, K. S. (1994). “Black Holes and Time Warps: Einstein’s Outrageous Legacy,” Norton, New York.
Wald, R. M. (1984). “General Relativity,” Univ. of Chicago Press, Chicago.
Weinberg, S. (1972). “Gravitation and Cosmology,” Wiley, New York. Wheeler,J.A.(1989).“AJourneyintoGravityandSpacetime,”Freeman, New York.
Will, C. (1981). “Theory and Experiment in Gravitational Physics,” Cambridge University Press, Cambridge, U.K.
 
 
Relativity, Special
Kathleen A. Thompson
 
Stanford University
I.	Observers, Reference Frames, and OtherPreliminaries
II.	Historical Background and Motivation
III.	Foundations of Special Relativity
IV.	Consequences of the Lorentz Transformation
V.	Relativistic Treatment of Energyand Momentum
VI.	Special Relativity and Electromagnetism
VII.	Special Relativity and Quantum MechanicsVIII. General Relativity
GLOSSARY
Antiparticle The partner of a subatomic particle which has the same mass but has electric charge (and certain other quantum numbers) of the opposite sign.
Conserved quantity A quantity which, although it may be different in different inertial reference frames, does notchangewithtimeasviewedinanyparticularinertial frame.
Event Apointinspace–time,i.e.,themathematicalidealization of “something happening” at a particular point in space at a particular moment in time.
Inertial frame A reference frame in which Galileo’s law of inertia holds—an object that is at rest and subject to no external forces remains at rest, and an object in motion continues to move at a constant velocity. (An inertial frame is also sometimes called a Lorentz frame.)
Invariant quantity A quantity that is the same in all inertial frames.
Mechanics The science of the laws governing the motion of material objects.
Proper length Length as observed in a frame which is at rest with respect to the length being measured.
Proper time Time (between two events) as measured by a clock carried at constant velocity from one event to the other.
Referenceframe Aspatialcoordinatesystem,alongwith synchronizedclockswhichareatrestinthatcoordinate system.
World line A curve representing a series of events in space–time (for example, the history of a particle).
 	117
SPECIAL RELATIVITY is the branch of physics formulatedbyAlbertEinsteinin1905thatsuccessfullydescribes the motion of objects, even when they are moving at extremely high speeds with respect to each other. At the beginning of the 20th century many physicists were aware that there were some difficulties in existing physics theories. On the one hand there was a theory of mechanics (the theory of motion of bodies) that had been developed by Galileo, Newton, and others in the 17th century. This theory was well established and had many successes. There was also a newer but also very successful theory of electromagnetism that had been put forth by the Scottish physicist James Clerk Maxwell in 1861. However, these two theories were hard to reconcile with certain experimental observations, and they did not seem to fit together consistently.
One symptom of the problems was the fact that the speed of light in empty space seemed to be always the same, no matter how fast the source of the light and/or the observer were moving. Based on Newtonian mechanics (and on everyday experience with velocities), it was expected that if an observer is traveling in the same direction as a beam of light, the light should appear to him/her to have a slower speed than it does to an observer moving opposite to the direction of the light. Of course, since lightmovesatextremelyhighspeed,itrequiresverysensitive experiments to accurately measure its speed and look for a dependence on the motion of the source and/or the observer.
Asweshallsee,itturnsoutthatNewtonianmechanicsis really only an approximate theory, useful when the velocities involved are not too high. Special relativity replaces Newtonian mechanics and is consistent with Maxwell’s theory of electromagnetism. Although special relativity is elegant, logical, and one of the cornerstones of modern physics, some of its consequences can seem bizarre and paradoxical at first. This is because our everyday experience and perceptions involve objects that have speeds much less than the speed of light. The speed in light in empty space, denoted by c, is equal to 2.99792458× 108 m/sec (this number is exact, since the meter is now defined to make it so). At this speed, a beam of light can travel all the way around the earth about seven times in a second.
When velocities are much lower than c, the differences between the predictions of special-relativistic and Newtonian mechanics are very slight. However, in situations where the differences between the two theories are large enough to be measured, special relativity has always turned out to be right. Special relativity is now an essential tool in many scientific and technical fields, including nuclear physics and reactors, astrophysics, acceleration and control of high-energy particles, and our fundamental theories of the elementary particles from which the universe is made.
I. OBSERVERS, REFERENCE FRAMES, AND OTHER PRELIMINARIES
The process of making measurements and observations involves some subtleties in relativity. In everyday life we don’tnormallyworryaboutthedistinctionbetween“when an event happens” and “when we see an event happen” because the speed of light is so high that the time for it to travel to our eyes is undetectably small. When dealing with velocities near the speed of light, as in relativity, we must be more careful. So to begin, we need to discuss observers in the context of relativity.
We define an observer’s reference frame to be a spatial coordinate system in which the observer is at rest, along with clocks at locations of interest. These clocks are at rest in the spatial coordinate system, and we assume a clock is conveniently located in the vicinity of any event whose time of occurrence we need to measure. An event is the mathematical idealization of the concept of something happening at a particular place at a particular time. Obviously an event (e.g., a handclap) has an existence independent of anyone’s frame of reference. But to specify an event in a given reference frame, we can give three spatial coordinates to tell where it occurs and a time coordinate to tell when.
The observer can specify where an object is located by giving its spatial coordinates (x, y, z) in his coordinate system. We will use bold-faced notation to denote such three-dimensional vectors, in particular we use x as a short-hand for the position vector (x, y, z). Our observer also needs a fourth coordinate so that he can specify the time t when the object is at the location (x, y, z). The observer in a given reference frame may specify the motion of an object by giving its three spatial coordinates (x, y, z) in that frame as a function of the time. We imagine that the time of arrival at a given spatial location is to be read from a nearby (“local”) clock.
The observer (or observers) in a given reference frame are assumed to have access to the data in a given frame, even if the events being measured are distantly located. However, if the space and time coordinates of a number of events are recorded in that frame, it may take some time for an observer located at a given place to gather together all that data. The observer cannot instantaneously find out what is happening at distant locations—it takes time to transmit information to him. For instance, if a lightning flash occurs at time t at a distance D from the observer, he will not actually see the lightning flash with his eyes until time t + D/c, where c is the speed of light. Nevertheless, wesayheobservesittooccurattimet,sinceheisassumed to be able to measure how far it is away, and he can take the light travel time into account. Alternatively, another observer in the same frame could record the time on a local clock in that frame (i.e., from a frame clock located very near the lightning flash). Assuming the clocks have been properly synchronized (we will discuss this in more detail later), he/she can simply report the time read from that clock.
Typically we shall be concerned with reference frames moving at constant velocity with respect to each other. The velocity is a vector v representing the rate of change of position with respect to time, i.e.,
	v = dx/dt = (dx/dt,dy/dt,dz/dt).	(1)
The speed, which is just the magnitude of the velocity, is
	 .	(2)
The acceleration is the rate of change of velocity, i.e.,
	a = dv/dt = d2x/dt2.	(3)
When an object is moving at constant velocity, its acceleration is therefore zero.
Wherever possible, we will keep things simple by choosing coordinate systems so that all motion takes place along just one axis, which we will take to be the x-axis. Suppose there is a second observer moving along the xaxis at constant velocity v with respect to the first observer. [NOTE: Here and elsewhere in this article, when we are talking about motion confined to a line, typically chosen to be the x-axis, we will represent the velocity by a nonboldface symbol (in this case v) which, unlike a speed, does have a sign according to whether the motion is in the positive or negative x-direction.] We may attach a second coordinate system to the second observer. To distinguish space and time coordinates in this system from those in the first system, we put a prime on them, i.e., we write x , y , z ,t instead of x, y, z,t.
Throughout this article we shall often use two such coordinate systems oriented so that corresponding axes are parallel. The “primed” frame is moving with constant velocity v along the x-axis of the unprimed frame (see Fig. 1). We choose our reference of time in each system so that t  0 at the moment when the origins of the two spatial coordinate systems are at the same place.
II. HISTORICAL BACKGROUND AND MOTIVATION
A. Pre-relativity Mechanics of Newton and Galileo
1. The Galilean Transformation
As a simple example, suppose the primed frame is fixed with respect to a passenger coach on a train, and the
 
FIGURE 1 Two reference frames in motion with respect to each other at constant velocity. Coordinates are chosen so that the primed frame (x ) moves with velocity v along x-axis with respect to unprimed frame (x, y,z).
unprimed frame is fixed with respect to the train tracks (assumed to be straight). We choose the x direction to be along the tracks. If a ball is thrown forward at speed dx  30 km/hr by a passenger sitting on the train, and the speed of the train with respect to the tracks is v =90 km/hr, then the ball will have speed dx/dt =120 km/hr as observed by a person standing beside the tracks.
This conclusion follows not only from common sense but also from an essential part of Newtonian mechanics— theGalileantransformation.Giventhetwocoordinatesystems described above, the Galilean transformation takes the form:
  vt
  y
(4)
z = z
 .
This transformation makes explicit some of our common sense ideas about space and time. Time flows at the same rate for observers in both frames. Furthermore, differentiating the first equation with respect to time (and using the fact that, from the last equation, d/dt =d/dt) shows that if the Galilean transformation is valid, then velocities along the same line of motion combine as we expect from everyday experience:
	dx  /dt	dx/dt − v.	(5)
Inotherwords,ifanobjecthasvelocityV along the x axis according to an observer in the primed frame, then its speed along the x-axis according to an observer in the unprimed frame will be V .
Before special relativity, it was generally assumed that the Galilean transformation is exactly true. For the train and ball example, it is an extremely good approximation. But suppose the train were instead a very futuristic rocket moving away from some star at 90% of the speed of light. Suppose also that the ball were moving toward the front of the rocket at 30% of the speed of light (with respect to the rocket). Then, as we shall see, it would be completely wrong to conclude that the ball is moving away from the star at 120% of the speed of light.
2. Mass, Energy, and Momentum in Newtonian Mechanics
Beforeproceedingfurtherintorelativityweneedtobriefly review the concepts of mass, energy, and momentum in Newtonianmechanics.Themassisameasureoftheinertia of a body, which may be thought of as its “resistance” to the action of a force. In Newtonian mechanics, the total amountofmassinanisolatedsystem(thatis,asystemthat has negligible interaction or exchange with the rest of the universe) is a conserved quantity, i.e., it does not change with time. Also, the mass of an object does not depend on how fast it is moving or on its temperature.
In Newtonian mechanics, the momentum p of an object is defined to be mv where v is the velocity of the object and m is its mass. Thus momentum is a vector with three components
px = m dx/dt,	py = m dy/dt,	pz = m dz/dt.	(6)
Thetotalamountofmomentuminanisolatedphysicalsystemisalsoconserved.However,theamountofmomentum depends on the reference frame. As a very simple example, consider a single object with mass m that is at rest in some reference frame. If it is isolated from all outside influences, it remains at rest—its momentum is zero. In a reference frame moving with velocity v with respect to the object’s rest frame, the object has momentum equal to −mv, also unchanging with time.
A system consisting of several objects interacting with each other can have the objects’ momenta redistributed, but the sum of the momenta remains constant. For example, in a system consisting of two bodies, the Newtonian law of momentum conservation says
	m1v1,i + m2v2,i = m1v1, f + m2v2, f ,	(7)
where the subscript “i” labels quantities before the collision and the subscript “ f ” labels quantities after the collision.
There are two basic forms of energy: (1) kinetic energy, the energy of motion of a body, which is defined in Newtonian mechanics by  mv2; and (2) potential energy, which may be regarded as “stored” energy. A common example of potential energy is the energy a ball has by virtue of being held above the ground, in the gravitational field of the Earth. A soon as the ball is let go, it accelerates toward the Earth, gaining kinetic energy and losing an (approximately) equal amount of potential energy. The reason we say “approximately” is that the friction of the air through whichtheballfallsdissipatesasmallamountoftheenergy asheat.Heatis“internal”kineticenergy,i.e.,theenergyof motion of the molecules comprising the ball and the surrounding air. In an isolated system, the total sum of all the different forms of energy is a constant in any given frame of reference. This is the law of conservation of energy.
Newton’s Second Law tells how the momentum p of an object changes with time when a force F is applied:
	F = dp/dt.	(8)
In Newtonian mechanics, this can also be written F = ma, where a = dv/dt is the acceleration of the object.
3. Galilean Relativity Principle
A principle of relativity had been formulated by Galileo long before Einstein developed the special theory of relativity. Galileo considered the example of a ship in smooth waters, carrying passengers who cannot see out, but who have with them a bowl of fish, a bottle dripping water into a bowl, and some birds and butterflies. From their observations, the passengers cannot tell whether the ship is at rest or moving forward in a straight line at constant speed. As Galileo said,
...the little animals fly with equal speed to all sides of the cabin. The fish swim indifferently in all directions, the drops fall into the vessel beneath, and in throwing something to your friend you need throw it no more strongly in one direction than another....
More formally, this means that the if the fundamental laws of motion hold in one reference frame, then they also hold in any reference frame moving at constant velocity with respect to the first frame. This is the Galilean relativity principle.
To see one example of this, consider the law of momentum conservation as expressed in Eq. (7). If we change to a frame of reference moving with velocity V with respect to the original frame, then according to the Galilean transformation we simply subtract V from each of the velocities in Eq. (7). to get the velocities in the new frame
 ,i −V, etc.). The masses m1 and m2 are not changed by transforming to a different reference frame. Thus, transforming to the new frame is equivalent to subtracting (m1 +m2)V from both sides of Eq. (5). So, momentum conservation also holds in the new frame:
	m  .	(9)
As another example, we can check that Newton’s Second Law is invariant under Galilean transformations. Differ-
entiating Eq. (5) gives d , since t 
and v is constant. This just says that a , i.e., the acceleration of an object is the same as measured in any two frames moving at constant velocity with respect to each other. Furthermore, in Newtonian mechanics, the masses and forces are the same in the two frames. Thus Newton’s Second Law is valid in the primed frame, if it is valid in the unprimed frame.
B. Propagation of Light
Maxwell’s theory of electromagnetism showed how electric and magnetic fields are related to each other and to the presence and motion of electric charges. The heart of the theory is Maxwell’s equations for the fields, along with an equation (Lorentz electromagnetic force law) that gives the force on a charge in terms of the local electric and magnetic field and the velocity of the charge. In Maxwell’s theory, light is a wave consisting of undulating patterns of electric and magnetic fields. Visible light is just a small slice of a spectrum of electromagnetic waves ranging from long wavelength radio waves to very short wavelength gamma rays. We use the term “light” to refer to electromagnetic waves of any wavelength, even if they are outside the range visible to our eyes.
Special relativity was originally motivated by the observation of several fairly subtle effects involving light. To understand the issues involved, we must review some of what was known about light. Early in the 19th century (1801–1804), Thomas Young carried out a quantitative demonstration of interference in light, using a doubleslit experiment. Interference is characteristic of waves—it simplymeansthatwhentwowavesinteract,theyreinforce or cancel each other depending on their relative phases of oscillation. Young’s experiments were followed by detailed studies of interference, diffraction, and polarization of light, by A. J. Fresnel and others. Thus by Maxwell’s time, it was well established that light exhibited many of the properties of a wave.
1.	The “Luminiferous Ether” Hypothesis
All waves familiar at that time (e.g., sound waves, water waves) were known to take place in a material medium. Allthesewaveshavethepropertythattheirapparentspeed depends on the motion of the observer with respect to the medium. It was natural to assume that there exists some kind of medium to “carry” light waves. It was difficult to account for the properties of such a medium in terms of a mechanical model. It was known that the speed of light was very high (which would imply that the medium exerts very strong restoring forces when displaced from equilibrium and yet there was no direct evidence for its existence). Nevertheless, it was assumed by many people that there does exist a “luminiferous ether” permeating all space, to play this role. It was expected that the speed of light should appear different depending on the observer’s motion with respect to the ether.
The ether hypothesis ran into difficulties, although it managed to survive a number of experimental tests by introducing further hypotheses. For example, in order to avoid contradictions with some of the experiments, it was necessary to assume that the ether is partially dragged along with moving material media in a very specific way that depends on the index of refraction of the medium.
2.	The Michelson–Morley Experiment
It was important to look for direct evidence of the preferred frame of reference that the ether was supposed to provide (if it existed at all). The most famous such attempts were carried out by A. A. Michelson and E. W. Morley. Their goal was to detect an effect on the measured speed of light due to motion of the observer through the ether. The experiments used an interferometer invented by Michelson (1881), and later refined in collaboration with Morley (1887).
ThebasicdesignoftheinterferometerisshowninFig.2. It is essentially a device in which a beam of monochromatic (single-wavelength) light is split, follows two
 
FIGURE 2 Schematic of Michelson–Morley experiment.
different paths, and is recombined. A small difference in the two optical pathlengths (i.e., a difference in the number of wavelengths of light along the two paths) can be detected by looking at the interference pattern created by the recombined beams. The beam of monochromatic light originates from a source S. The plate P partly reflects and partly transmits the light. Thus there is one path that reflects from P to mirror M1 and goes back through P to the observation telescope T. There is a second path that goes through P to the mirror M2, is reflected back to P where it is reflected to the observation telescope T. The distances from P to M1 and to M2 respectively are L1 and L2.
When the interferometer is rotated the optical path difference along the two arms would change, if the ether hypothesis is correct. The expected change depends on its speed v with respect to the ether and on its orientation with respect to the direction of motion. For example, if the interferometer is first oriented so that one arm is pointing along the direction of motion through the ether, and is then rotated by 90◦ so that the other arm is along the direction of motion, one can show that the change in optical path difference would be
	δ ,	(10)
where λ is the wavelength of the light. Michelson and Morley expected that for at least some orientations of the apparatus and some times of year, the speed v of the apparatus through the ether should be greater than or equal to the earth’s orbital speed of about 30 km/sec. The resulting value of δ should have been large enough for them to detect, but their result was null—no change in the optical pathdifferencewasobserved,nomatterhowtheapparatus was rotated.
C. Lorentz–Fitzgerald Contraction and Lorentz Transformations
1.	Lorentz–Fitzgerald Contraction
It appeared to be impossible to detect and measure motion with respect to an ether. Shortly after the conclusion of the Michelson–Morley experiments, a possible explanation for their null result was proposed separately by both H. A. Lorentz and G. F. Fitzgerald. Their suggestion was that an object is contracted along its direction of motion by the factor (1−v2/c2)1/2, where v is the speed with respect to the ether. This would lead to a difference in the lengths of the two arms of the interferometer that would be just right to cancel the expected effects of motion through the ether. At first this proposal seemed to be little more than another ad hoc assumption introduced to keep alive the notion of an ether.
2.	Lorentz Transformations
Lorentzandotherphysicistshadalsobeenalsotroubledby the fact that Maxwell’s equations are not invariant when a Galilean transformation of the coordinates is applied. However, Lorentz and the mathematician H. Poincare noticed that Maxwell’s equations were invariant under a different transformation, whose significance and fundamental nature were not clear at the time. This transformation, which has come to be known as the Lorentz transformation, is as follows:
 
  y
(11)
z = z
 .
Here γ is defined by:
	 ,	(12)
and is called the Lorentz factor. Note that γ ≥1 and that 1/γ is the Lorentz–Fitzgerald contraction factor. As discussed earlier for the Galilean transformation, we have set up our coordinate systems so that the primed system with respect to the unprimed system has velocity v along the x axis, and the origins of the two coordinate systems coincideattimet =0.Atthetime,thisinvarianceofMaxwell’s equations under the Lorentz transformation was intriguing,butthefullimplicationsofthetransformationwerenot understood. It does predict an apparent contraction along thedirectionofmotion,justasisneededtoexplainthenull result of the Michelson–Morley experiment. However, if the last of Eq. (11) is correct, time flows differently for different observers—a major departure from Newtonian mechanics!
The Lorentz transformation, if valid, also suggests that the constant c, the speed of light in vacuum, is a “universal speed limit.” As v approaches c, the factor γ approaches infinity. If v were to become larger than c, γ would be the squarerootofanegativenumber,whichsuggeststhatv >c does not occur in reality. All existing experiments and observationsareindeedconsistentwiththehypothesisthat no material object or causal influence propagates faster than c.
One of the key contributions of Einstein was to derive the Lorentz transformation from basic principles and to show that it, rather than the Galilean transformation, is the correct way to relate the coordinates in two reference frames in uniform motion with respect to each other. He then proceeded to build a theory that ended up revising many of the accepted ideas in physics.
3. Invariance of Transverse Distances
As we have just discussed, physicists were forced to consider the possibility that observed lengths may be contracted along the direction of motion. Note that in both the Galilean and the Lorentz transformations, distances transverse (i.e., at right angles ) to the direction of motion do not change. The necessity for this invariance of transverse dimensions follows from simple symmetry considerations.
For example, suppose a piston fits exactly inside a cylinder when it is at rest. Then suppose the piston and cylinder are moving toward each other at very high speeds as shown in Fig. 3. What happens when the piston and cylinder meet? We might choose to analyze the situation in either the rest frame of the piston or the rest frame of the cylinder. If the observed transverse coordinates of a moving object either grew or shrank, then according to one of the frames the piston would be smaller transversely, and should be able to sail into the cylinder and make a dent in the back wall. In the other frame, the piston would have the larger diameter, so it would collide with the outer rim of the cylinder and never reach the back wall at all. But the resultcannotdependontheobserver’sframe—eitherthere is a dent on the back wall or there isn’t! So the assumption that the transverse dimensions depend on the frame must be wrong.
Even more fundamentally, there is no sensible way to define an axis toward which the transverse coordinates in a given frame would grow or shrink—it was really quite arbitrary to choose this to be the axis of symmetry of the piston and cylinder in Fig. 3. In summary, if we assume the direction of relative motion is along the x-axis,
 
FIGURE 3 A situation illustrating the invariance of transverse dimensions.
there is no consistent way to define a transformation of y and z other than the identity transformation
  y
(13)
z .
III. FOUNDATIONS OF SPECIAL RELATIVITY
A. Inertial Reference Frames
In order to develop relativity, we first need to revisit the concept of the observer and his reference frame. Specifically, we need to define what we mean by an “inertial
reference frame.”
Galileopostulated,baseduponsimpleexperiments,that a body which is moving at constant velocity (i.e., in a straight line at constant speed) continues to move with that same velocity provided that no forces act upon it. This is known as Galileo’s law of inertia (and was later postulated by Newton as his First Law). We define an inertial reference frame to be a reference frame in which Galileo’s law of inertia holds.
Oneexampleofaninertialframeisanunpoweredspace capsule drifting freely through space. The interior of an elevator that has broken loose from its cable and is freely falling in the gravitational field of the earth is also a good approximation to an inertial frame until the elevator crashes into the ground. An observer inside the falling elevator will find that if an object is given a small push, it will move in a straight line as seen in a spatial coordinate system fixed in the elevator.
Strictly speaking, an inertial frame is always only an approximation to reality since it can never be completely free of extraneous influences. If the observer’s measurements are sensitive enough, deviations from Galileo’s law of inertia can in general be detected. In the freely falling elevator, if position and time measurements are sensitive enough it will be possible to observe small effects due to the fact that the strength and direction of the gravitational field are very slightly different at different locations in the elevator.
Inthecontext of both Newtonian mechanics and special relativity, it is common to think of an inertial frame as a frame that is moving with “constant velocity.” Of course (as Newton himself realized) this leaves open the question “constant velocity with respect to what?” With the above definition of an inertial frame, we are able to leave aside the question of whether motion at constant velocity has a meaning in any absolute sense (for example, with respect to the average distribution of matter in the universe). There is no requirement that the motion be at constant velocity with respect to the rest of the universe. The freely falling elevator is an example of an inertial frame that is not moving at constant velocity—it is accelerating toward thecenteroftheearth.Allthatwerequireofaninertialreference frame is that Galileo’s law of inertia hold to within the sensitivity of our measurements, in the region of space and for the duration of time that we are concerned with.
Hereafter when we say “reference frame” or just “frame,” we shall mean an inertial reference frame unless otherwise specified.
B. Postulates of Relativity
According to the Galilean relativity principle, the laws of motion are the same in all inertial frames. Einstein extended the relativity principle to ALL the laws of physics, not just the laws of motion, and took it as one of the basic postulates of his special theory of relativity.
1.	Postulate 1 (Principle of Relativity): The fundamental laws of physics are the same in every inertial reference frame.
Einstein, in recalling a paradox he had first thought about when he was sixteen, wrote:
If I pursue a beam of light with the velocity c (velocity of light in a vacuum). I should observe such a beam of light as a spatially oscillatory electromagnetic field at rest. However, there seems to benosuchthing,whetheronthebasisofexperienceoraccording to Maxwell’s equations.
In other words, Einstein began to question whether it was possible even in principle to “catch up with” a beam of light. This, along with the failure of all experiments to detect any changes of the speed of light in empty space, motivated him to assume.
2.	Postulate 2 (Invariance of the Speed of Light): The speed of light in vacuum is the same in all reference frames.
In particular, the observed speed of light depends neither on the speed of the source of light nor on the speed of the observer. As noted earlier, Newton’s Laws were assumed to be valid in all inertial frames, and these laws of motion are invariant under Galilean transformations. Special relativity modifies this by assuming that ALL correct fundamental laws of physics are valid in all inertial frames, and the fundamental laws of physics are invariant under Lorentz transformations. Newton’s Laws and the Galilean transformation are good approximations in many situations, but fail badly when dealing with speeds close to the speed of light.
C. Synchronization of Clocks
Inordertomakemeaningfulcomparisonsoftimeatdifferent locations in a given frame, it is necessary to synchronize the clocks being used in that frame. Since the speed of light c is constant in any frame if Postulate 2 is true, we could proceed as follows. Choose one of the clocks to be the reference clock, and set its time to zero. Set the time on each of the other clocks to time Di/c, where Di is the distance from the reference clock to clock i, and hold clock i’s time at this value. Now let a flash of light be emitted from the reference clock, and at the same time let it begin to run starting at time t =0. At the moment when the flash arrives at any other clock, let it begin to run starting at its preset value. In this way, all the clocks will be synchronized, since the time lag needed for the flash to reach each clock will be exactly the preset value for that clock. It is important to note that this procedure synchronizes the clocks according to observers at rest in a particular reference frame. As we shall see, the clocks will be noticeably out of synchronization according to observers in a frame moving at high speed with respect to the first frame.
D. Time Dilation in Relativity
The postulate that the speed of light in empty space is constantisthebasisformanyoftheresultsinrelativitythat go against our normal intuition. As one example of this, consider the following situation. Suppose that there are two parallel mirrors a distance D apart. We can use them to make a clock consisting of a light flash that bounces back and forth between the two mirrors. The clock “ticks” each time the light flash hits either mirror. Suppose that this clock is put on a high-speed rocket.
Firstconsiderhowtheclocklookstoanobserver(whom weshallcallO)whoismovingwiththerocketandisatrest withrespecttotheclock.ObserverO seesthelightmoving straightupanddownalongthedistance D betweenmirrors as shown in Fig. 4(a). According to observer O, each tick of the clock takes a time T  = D/c.
Let the rocket be moving to the right at speed v with respect to another observer whom we shall call observer O (see Fig. 4(b)). Common sense would lead us to expect that each tick of the clock takes the same time for observer O as it does for O, but from the following arguments we see that this cannot be true if relativity is valid.
First, the dimensions transverse to the direction of motion are invariant. In the present situation this means that observer O agrees with observer O that the distance between the two mirrors is D.
Next, we note that while the light is going from one mirrortotheother,therocketmovestotherightinobserver
 
FIGURE 4 Clock consisting of a light flash bouncing back and forth between two mirrors. (a) Path of light flash as seen by an observer at rest with respect to the clock. (b) Path of light flash as seen by an observer with respect to whom the clock is moving to the right with speed v.
O’s frame by the distance vT, where v is the speed of the rocket with respect to observer O and T is the time that observer O says it takes the light to travel between mirrors. So according to observer O, the light must travel a longer path between mirrors than it travels according to observer O. From Einstein’s second postulate, the speed of light has the same value c in the frame of the observer O as it does for the observer O. Therefore, observer O will say that a tick of the clock takes longer than does observer O!
It is straightforward to derive the factor by which the time per clock tick differs for these two observers. From the Pythagorean theorem, the distance travelled by the light during one tick, as seen by observer O, is  . Thus the time for one tick is T =
 /c. Using D 	cT to eliminate D, we find
	T  ,	(14)
where γ is the Lorentz factor. The faster the rocket goes, the more slowly the clock ticks, according to observer O. Although we have been talking about a particular type of clock, it follows from the principle of relativity that all other clocks must run slow by the same factor. For if they did not, then the very fact that clocks get out of synchronization in a moving frame could be used to distinguish a moving frame from one at rest. This would contradict the postulate that the laws of physics are the same in all inertial frames.
Furthermore, there is no inherent asymmetry between observers O and O. From the point of view of O, it is O who is moving (at velocity −v along the x-axis). By the same kind of argument as given above, observer O will observe clocks that are moving with O to run slow (by the factor γ) compared to his own clocks.
E. Derivation of the Lorentz Transformation
The Lorentz transformation, originally postulated in an ad hocmannertoexplaintheMichelson–Morleyexperiment, can now be derived. Assuming Einstein’s two postulates, we now show that the Lorentz transformation is the only possible transformation between two inertial coordinate systems moving with constant velocity with respect to each other.
The transformation must be linear in the time and space coordinates because of the Principle of Relativity (Postulate 1). If the transformation were not linear, then uniform motion in a straight line in one frame would no longer appear as uniform straight-line motion in another frame moving at constant velocity with respect to the first. This would contradict the requirement that Galileo’s law of inertia hold in all inertial frames.
We use the fact that the transformation must not change the coordinates transverse to the axis of relative motion of the two frames (which, as usual, we take to be along the x and x axes for simplicity). Then  y and z = z, just as in the Galilean transformation. With this choice, the transformation equations for x and t must be independent ofthetransversecoordinatesbysymmetry(thereisnoway to single out a particular location or direction of rotation relative to the axis of motion).
Therefore the transformation in x must be of the form x .	(15)
Our analysis of the light-flash clock showed that when x  0 we have t  so that x . This is consistent with Eq. (15) only if B =γv. Furthermore, the motion of the origin of the unprimed system (x =0), as expressed in the coordinates of the primed system, is given by x  0. Again comparing with Eq. (15) we must have B/A =v, resulting in
	x .	(16)
Since we can invert the roles of the primed and unprimed coordinates by reversing the sign of v, we must also have
	 .	(17)
Equations (16) and (17) may be solved for t in terms of the primed variables:
	t 	(18)
and for t in terms of the unprimed variables:
	 .	(19)
Thus we have reproduced the Lorentz transformation given previously as Eq. (11). It may be summarized in a slightly different form—it is often useful to regard all fourspacetimedimensionsashavingthesameunits,either conventional length units (e.g., meters) or conventional time units (e.g., seconds). We can do this by multiplying the time in conventional units by c. Then ct would be replaced by t (and ct ) in Eq. (11). Or we could equally well divide each of the space dimensions in conventional units by c. In either case, the Lorentz transformation with timeandspaceexpressedinthesameunitstakesthesimple form
 
  y
(20)
z = z
 .
Here β ≡v/c is the velocity of the primed frame with respect to the unprimed frame, expressed as a fraction of the speed of light, and v2/c2 is the Lorentz factor. The inverse transformation, again with time and space in the same units, is obtained by simply reversing the sign of v (and thus of β) when the roles of the primed and unprimed cooordinates are reversed:
x  
y  
(21)
	z	 z
t  .
Note that the Lorentz transformation reduces to the Galilean transformation when v c and x/t c.
F. The Invariant Interval
The space and time coordinates differ in different frames, but there is an important function of the coordinates that is an invariant, i.e., the same in all frames. This quantity is called the space–time interval (or just interval) between two events. For two events with space–time coordinates
(t1, x1, y1, z1) and (t2, x2, y2, z2) we define the square of the interval by
 
With a bit of algebra one can show that the interval is invariant under Lorentz transformations. In other words, the interval between two events is the same regardless of which inertial frame it is calculated in:
 	(23)
if the primed and unprimed coordinates are related by a Lorentz transformation.
If (s)2 >0, we say the interval is time-like. When the interval between two events is time-like it is possible for an observer to be present at both events, since he does not need to travel faster than the speed of light c to get from one event to the other. If (s)2 =0, we say the interval is light-like—a light ray can depart from Event 1 and arrive exactly at the right time to be present at Event 2, or vice versa.If(s)2 <0,wesaytheintervalisspace-like.When the interval between two events is space-like then no object or signal can get from one event to the other because it would be necessary to exceed the speed of light. Since the speed of light is assumed to be the maximum speed with which any physical influence can propagate, there cannot be a causal connection between two such events. Furthermore, it can be shown that if two events have spacelike separation, then and only then is it possible for observers in different reference frames to disagree about the time ordering of the two events.
G. Minkowski Diagrams and World Lines
Diagrams in space–time are often referred to as Minkowski diagrams, after H. Minkowski who pointed out a “geometric” way of looking at relativity. The concept of distance in ordinary space is replaced by the concept of the interval between two events in space–time. Just as distance between two points in ordinary space is an invariant regardless of rotations of the coordinate system, the interval between two events in Minkowski space (i.e., space–time) is an invariant regardless of the inertial frame. Of course, the presence of the relative minus sign between space and time coordinates in the definition of interval means that the geometry of Minkowski space is fundamentally different from that of ordinary Euclidean space.
Figure5isanexampleofsuchadiagram(whereforsimplicity only one of the three space dimensions is depicted. The entire “history” of a moving particle is represented by
 
FIGURE 5 A Minkowski diagram (including only one spatial dimension), showing the world-line of a particle and the past and future light-cones of the event at O. [Reproduced with permission from Jackson, J. D. (1975). “Classical Electrodynamics,” 2nd ed., p. 519, Wiley, New York.]
a curve in space–time. This curve is called the particle’s world line. An example of a world line starting at event A and proceeding to event B is shown in Fig. 5.
Note that the absolute value of the slope of a world line must never be less than one (when plotted with time on the vertical axis as shown), since the particle may not exceed the speed of light. For a particle which passes through O, all points in the white region marked “future” are in principle reachable by the particle at later times, since it could get to any of these events without exceeding the speed of light. Similarly, a particle at O could in principle have taken a path that allowed it to have been present at any event in the white region marked “past.” However, all events in the cross-hatched region are inaccessible in the sensethattheycannotcausallyinfluence,norbeinfluenced by, an event at O. This region is sometimes referred to as “elsewhere” with respect to event O.
H. Proper Time
We saw earlier that an observer who is in motion with respect to a clock will always observe it to run slower than clocks at rest in his own frame. This leads us to the notion of proper time. Suppose that the time between two events is to be measured. Assume also that the space– time interval between the two events is timelike, so that is possible for a clock to be present at both events. If the clock is carried at constant velocity from Event 1 to Event 2, then the time between the events as read by that clock is called the proper time between the events, i.e., τ is equal to t2 −t1 in that frame (we use the Greek letter tau (τ) to represent proper time). Both events occur at the same place in the rest frame of the proper clock, that is, the spatial separation (x)  between the two events is zero. Therefore the proper time τ is simply related to the space–time interval between two time-like events by
	τ = s/c.	(24)
Carrying a clock at constant velocity from one event to another means that the portion of the clock’s world line between the two events is a straight line in Minkowski space.IftheMinkowskidiagramisplottedintherestframe of the clock, the line is vertical—there is no change in any of the spatial coordinates anywhere along the path—not only is x  0 for the path as a whole, but dx =dy =dz =0 for any short segment along the path.
Thus, in this frame
	dτ = dt	(25)
for each short segment along the path.
Suppose the clock instead takes a less direct route, but is still present at both events, i.e., the clock still departs from x1, y1, z1 at time t1 and arrives at x2, y2, z2 at time t2, butitdoesnottravelatconstantvelocity.Inthiscaseitwill not be true that dx =dy =dz =0 for all segments along the path. The total elapsed time on the clock is obtained by integratingthepropertimealongthenewpath.Weassume that the proper time along each short space–time segment of the path may be calculated treating each sufficiently small segment of the world-line as a straight line, and we calculate the proper time assuming the clock moves with constant velocity along each short segment. The proper time along each such segment is then
	d .	(26)
Comparing segments that range over the same values of the time coordinates, it is obvious that the proper time along the indirect path (Eq. (26)) is less than the proper time along the direct path (Eq. (25)) We see that taking a more circuitous route in spacetime will make the integrated proper time less than it is if the clock takes the most direct route! This peculiar feature of the geometry of space-time is due to the relative minus sign between the space and time coordinates.
IV. CONSEQUENCES OF THE LORENTZ TRANSFORMATION
A. Proper Length and Lorentz Contraction
A well-known result of relativity is that objects are observed to be shorter along their direction of motion than when they are at rest. This follows directly from the Lorentz transformation, but may also be derived by the following simple argument involving time dilation.
The proper length of an object is defined to be its length as measured in its own rest frame, Suppose the object is a straight stick having proper length L0. Let a bee fly directly from one end of the stick to the other at constant speed v with respect to the rest frame of the stick. Then according to an observer in the stick rest frame, the trip will take a time t0 = L0/v. The bee sees the stick going backwards, also at speed v. But according to the bee, from our previous discussion of time dilation, the trip will take less time—the time as measured in the frame of the bee is tbee . Therefore, in the frame of the bee, the distance travelled in going from one end of the stick to the other is only L =vtbee, i.e.,
	L = L0/γ.	(27)
Of course, for real bees, the factor γ is so close to 1 that tbee and t0 are for all practical purposes indistinguishable. However,subatomicparticlesareoftenacceleratedinhigh energy physics laboratories to speeds very close to c, so that  1. For example at Stanford University, electrons are accelerated in a 3-km (approximately 2-mile)-long straight machine called a linac. By the time an electron gets to the end of the linac, its speed is so close to c that the Lorentz factor γ ≈105. In the rest frame of an electron with this speed, the apparent length of the linac is only about three centimeters (little more than an inch!).
B. Velocity Combination Formula
Consider two inertial frames such that the velocity of one frame (the primed frame) with respect to the other frame (the unprimed frame) is v along the x-axis. We now suppose there is an object having velocity V , also along the x-axis, as observed in the primed frame. What is the velocity V of the object as observed in the unprimed frame? Commonsense experience would lead us to expect that the velocity in the unprimed frame is just V .
As shown earlier, this is what the Galilean transformation gives. However, relativity tells us that the correct transformation between frames is the Lorentz transformation, which gives dx  
	dt  .	(28)
Dividing the first equation by the second, and using the fact that V  dx /dt and V = dx/dt, we obtain
v 
	V .	(29)
The closer the velocities are to the speed of light, the more this expression disagrees with simple addition of velocities. Note that if either of the velocities v or V  is equal to c, then V is equal to c. So this is consistent with the postulate that the speed of light in vacuum looks the same in all reference frames. We also see that so long as both v and V  are less than c, the magnitude V of the combined velocity willalsobelessthanc.Moregeneralvelocitycombination formulas, where the velocities are not all along the same axis, may similarly be derived from the Lorentz transformation, and these conclusions still hold.
C. Relativistic Doppler Effect
It is familiar from our everyday experience that the pitch of a siren is higher when it approaches and lower when it recedes. This is an example of the Doppler effect, which is a change in the observed frequency of a periodic disturbance, arising from the motion of the source and/or the observer. In the case of sound waves, the observed speed of the waves, as well as the observed frequency, depends on the motion of the observer with respect to the transmitting medium. In other words, sound waves have a “preferred” frame, namely, the frame in which the transmitting medium, typically air, is at rest. Light and other electromagneticwaves,however,donothaveapreferredframe— we have seen that attempts to find an “ether” failed.
For comparison, we will first derive the nonrelativistic Doppler formula for sound waves. Then we will derive the relativistic Doppler effect for light, i.e., for electromagnetic waves. Throughout the discussion we use the general relationship
	V = λf	(30)
between the propagation speed V, wavelength λ, and frequency f of a wave or other periodic disturbance. Also, the frequency of the wave is just the reciprocal of its period T:
	f = 1/T.	(31)
1. Nonrelativistic Doppler Effect for Sound Waves
The speed of sound is much less than c, so if we assume the speeds of the source and observer are also much less than c, then Newtonian mechanics is valid to an excellent approximation. Suppose that a source of sound waves S and a receiver R are moving along the same line which we take to be the x-axis, and suppose that their velocities with respect to the air are vS and vR, respectively (we speak of velocities vR and vS here rather than just speeds, since these quantities do have a sign according to whether they are in the direction of the positive or negative x-axis). Let
 
FIGURE 6 (a) Diagram for analyzing nonrelativistic Doppler effect for sound waves. The effect depends on the velocities of the source S and the receiver R with respect to the transmitting medium (typically air). (b) Diagram for analyzing relativistic Dopplereffectforelectromagneticwaves.Theeffectdependsonly on the relative velocity of the source S (whose rest frame is the unprimed frame) and receiver R (whose rest frame is the primed frame).
R be to the right of S, as shown in Fig. 6(a). Let S be emitting a sound wave of frequency f (and thus period T =1/f ), and suppose that the speed of sound in the air is w. The time between emission of successive crests of the wave is T =1/f . The distance between crests of the wave would be λ=w/f if the source were at rest. However, the velocity of these crests relative to the source is w −vS. so for nonzero vS the distance between crests is modified to
	λmod = (w − vS)/f.	(32)
If R were at rest, the time between the arrivals of successive crests would be λmod/w. But for nonzero vR, the velocity of the wave with respect to R is w −vR, so that the time between arrivals of successive crests is Tmod = λmod/(w −vR). The received frequency fmod is just 1/Tmod, so that we end up with
	f .	(33)
1 − vS/w
This formula relates the frequency f emitted by S and the frequency fmod received by R. The velocities vR and vS are positive toward the right and negative toward the left. Note that the effect depends on both vR and vS and cannot be reduced to an expression involving only their relative velocity vR–vS.
2. Relativistic Doppler Effect for Electromagnetic Waves
We now analyze the relativistic Doppler effect for electromagneticwaves.Weagainassumethatthevelocitiesofthe source and observer are along the x-axis, and we choose the unprimed frame to be the rest frame of the source and the primed frame to be the rest frame of the receiver [see Fig. 6(b)].Then the velocity v of the primed frame with respect to the unprimed frame is just the relative velocity of the source and receiver. In the frame of the source, let the period of the wave be T, i.e., T is the time between emission of wave crests as seen in the source frame. The wavelength in the source frame is then λ=cT.
Now let us consider two events and how they look in the two frames. Let Event 1 be the arrival of the crest of the nth wave at the receiver, and let Event 2 be the arrival of the crest of the n +1st wave at the receiver. From the point of view of the source frame, the velocity of the wave train with respect to the receiver is c −v. Thus, in the source frame, the time separation between Event 1 and Event 2
is
t ≡ t	−	−	.	(34) c	v	c
Since the receiver is traveling at velocity v in the source frame, the distance between the two events in the source frame is
vcT
x ≡ x2 − x1 = vt =	 −	.	(35) c	v
Now we need only Lorentz transform from the source frame (the unprimed frame) to the receiver’s frame (the primed frame) to find the time separation between the two events as observed in frame of the receiver. This is just the period of the waves as seen by the receiver:
	Tmod = t  .	(36)
Substituting for t and x from Eqs. (34) and (35), we find
T 
Using the usual definitions  , and f =1/T as well as fmod =1/Tmod we may simplify this
to
	f  f.	(38)
Note that v (and thus β) is positive if the source and receiver are moving away from each other, and is negative if the source and receiver are moving toward each other. Since there is no “preferred frame” as there was in case of sound waves, the result depends only on the relative velocity of the source and receiver.
D. Relativity of Simultaneity: Einstein’s Train Paradox
It is necessary to be extremely careful about using the phrase “at the same time” when dealing with relativity. The Newtonian and Galilean concept of an absolute time, flowing uniformly and at the same rate for all observers, is notstrictlytrue.Thenotionofanabsolutetimeisanexcellent approximation in our everyday experience. However, it breaks down when considering situations involving relative motion at very high speed.
To see this, we examine a situation sometimes referred to as “Einstein’s train paradox.” Consider a (very highspeed!) train moving along a straight track. Let a woman be at sitting on the train exactly equidistant from its two ends, and let a man be standing on the ground right next to the tracks. Suppose that the man sees the flashes from two bolts of lightning striking the ends of the train at the exactsamemomentwhenthewomanispassinghimonthe train. At this moment the man knows he is also equidistant from both ends of the train (from symmetry, assuming he knows the woman is sitting equidistant from both ends). So, knowing that the speed of light is c, he concludes that the light flashes from each end will take the same amount of time to reach him and therefore the strikes at each end of the train occurred simultaneously. He also concludes that the flash from the front of the train will arrive at the woman before the flash from the back arrives, because she is moving toward the front flash and away from the back flash.
Now, what does the woman say about these events? The mere fact of changing reference frames, e.g., from the man’s frame to the woman’s frame, cannot change the time ordering of events which occur at the same location in some frame (in this case, at the location of the woman in her frame). To see this, suppose for example that the woman is carrying a device which does nothing if it receives the front flash first, and explodes if it receives the back flash first. Obviously, the functioning of the device must be independent of whose frame the situation is analyzed from—the explosion either occurs or does not occur in both frames. So the device must receive the flashes in the same order in both frames.
At first glance there is nothing surprising about the fact that the woman sees the front flash before the back flash. Based on our ordinary experience with velocities we would be tempted to say that in the woman’s reference frame, the front flash travels faster than c and the back flash travels slower than c, if c is the speed of light in the man’s frame. However, one of the postulates of relativity is that the speed of light is observed to be the same in any frame, regardless of the state of motion of the observer. So the front and back flashes also both travel with speed c in the woman’s frame. A consequence of this is that the two observers do not agree about whether the two flashes are simultaneous.
This may seem paradoxical at first, because it is not somethingwearefamiliarwithfromeverydayexperience. We see that accepting Postulate 2 (invariance of the speed of light) forces us to revise the concept of simultaneity. Relativity of simultaneity applies to any two events which are separated along the line of relative motion of two different inertial frames: If the two events are simultaneous in one of the frames, they will not be simultaneous in the other—this follows directly from the Lorentz transformation. The train “paradox” is just one illustration of this general statement.
Most“paradoxes”inrelativitycanintheendbereduced to some confusion arising from the fact that whether or not two events are simultaneous depends on the observer’s frame of reference. With this in mind, it is instructive to look at two more famous relativistic paradoxes and how they are resolved.
E. The Twin Paradox
According to the principle of relativity, all processes in a givenframe,includingthebiologicalworkingsofahuman body, must undergo the same amount of time dilation as all the other clocks and physical processes in that frame. Anyinertialframeissupposedtofollowthesamephysical laws as any other inertial frame, and this would be violated if a person saw a clock in his own frame run slower with respect to his own heartbeat when he changed his speed (of course, if this happens to a race car driver, it is a psychological and not a relativistic effect!)
A very famous paradox involving relativistic time dilation is the twin paradox. Suppose there are twins, Astro and Homer, and that Astro makes a round trip journey to a star 20 light-years away while Homer remains on the Earth. A light-year is the distance light travels in 1 year. [Here we use the convenient device of measuring time and distance in the same unit, the year.] To make the analysis simple, we assume that Earth and the destination star are both at rest in the same inertial frame, and that Astro travels at constant speed (say 80% of the speed of light) straighttothestar,instantaneouslyreversesdirectionupon getting there, and returns at the same speed. Since the oneway distance L is 20 light-years in Homer’s rest frame and β =v/c =0.8, Homer calculates that the total time T for the trip will be 2L/v =50 years.
However, from the Lorentz time dilation, Homer knows that Astro’s clock will be running slow by the factor γ =[1−(0.8)2]−1/2 =5/3≈1.67 compared to his own, on both the outbound and inbound parts of the trip. So he would expect Astro to have experienced an elapsed time of T  = T/γ =50/(5/3)=30 years, and indeed this is what would happen. Another way to see this is to note that from Astro’s point of view, the one-way distance is Lorentz contracted to L = L/γ =20/(5/3)=12 lightyears. Astro sees Earth and the star speeding past himself at speed v =0.8c, so according to him the journey takes T  30 years. The net effect is that when Astro returns he is 20 years younger than Homer.
The “paradox” consists of the fact that in accord with Lorentz time dilation, Astro should also expect Homer’s clock to be running slow relative to his own, by the same factor γ, since Homer is in motion with respect to Astro at the same speed v. So, exactly how does the difference in their ages come about?
We already know the answer if we recall our discussion of proper time. We saw that the time between two events is maximized for a clock which goes from one event to another by staying in the same inertial frame all the way. It is true that while each twin is in an inertial frame, and thus moving at constant velocity with respect to other twin, each will observe the other’s clock to be ticking more slowly than his own. The difference is that Homer remains in the same inertial frame throughout, while Astro changes inertial frames when he reverses direction. There are real physical effects felt by Astro when this acceleration occurs—he is dragged toward one end of the ship as it turns around (in fact the extreme acceleration assumed in this example would kill a real human!).
Thechangeofinertialframesisassociatedwithashiftin Astro’s definition of simultaneity at locations away from himalonghislineofmotion.Inparticular,hisdefinitionof which events on earth are simultaneous with events ocurring at his location will abruptly shift when he changes reference frames. To see this, let us denote the rest frame of Homer by S, the rest frame of Astro on the outbound leg by S, and the rest frame of Astro on the inbound leg by S. Take frame S to be moving with speed v in the positive x direction with respect to S, and take frame S to be moving with speed v in the negative x direction with respect to S. A space–time diagram of the trip as viewed in the S frame is shown in Fig. 7. The solid line is Astro’s world line—he travels 20 light-years in an elapsed time of 25 years, then reverses direction and returns to his starting point in another 25 years of elapsed time. In Fig. 7, all events lying on any given horizontal line are simultaneous in the S frame since they have the same t coordinate. But observers in frames moving with respect to the S frame have different definitions of simultaneity. If an observer is moving along the x direction of
 
FIGURE 7 Spacetime diagram of Astro’s journey, as seen in the rest frame of Homer. The heavy line is Astro’s world-line. The dotted lines show the lines of simultaneity with the turnaround point, in Astro’s outgoing and ingoing frames.
frame S, his lines of simultaneity will not be horizontal in Fig. 7.
The upward-sloping dotted line in Fig. 7 is the line containing events simultaneous with the turnaround event, according to observers in frame S. We may easily calculate the slope of this line by applying the Lorentz transformation. Let t1, x1 and t2, x2 be the coordinates of any two events in the S frame. Then the time coordinates in the S frame are given by the Lorentz transformation, which, with time and distance measured in the same units, becomes
	t )	(39)
	t .	(40)
so that
	 ,	(41)
where t ≡t1 − t2, x  , and t  . If the two events are simultaneous in S (i.e.,   0), then
t/x =β =v/c. Thus all lines of simultaneity in frame S, the frame of Astro during his outbound journey, have slope v/c in Fig. 7. We show one such line, in particular, the line of all events simultaneous with the turnaround event, according to Astro while he is in the outbound frame.
This line of simultaneity for the outbound frame S intersects the t-axis, where x =0 (i.e., at the location of Earth), at t =9 years. This is in agreement with the assertion that Astro sees Homer’s clock run slow by the factor γ—the outbound trip takes 15 years according to Astro, thus 15/γ =9 years should elapse on Homer’s clock, according to Astro’s definition of simultaneity.
Bysimilarreasoning,thelinesofsimultaneityforframe
S, the frame of Astro during his inbound journey, have slope−v/c. The downward-sloping dotted line is the line of all events simultaneous with the turnaround event, according to Astro when he is in the inbound frame. The intercept on the t-axis is at t =41=50 − 9 years, again consistent with Astro’s expectation that 9 years should elapse on Homer’s clock during Astro’s return journey. However,Astro’sdefinitionofsimultaneitywitheventson Earth jumps ahead by 41−9=32 years when he changes frames! Of course, no sudden jump occurs on the clocks in any frame! It is just that the definition of simultaneity of events is relative—it depends on the observer’s frame of reference. Clocks at a given location (say at the earth) which have been synchronized in different frames will in general have different readings. Suppose that the twins wereexactly30yearsoldwhenAstrodepartedonhisjourney. If Astro has just reached the turnaround point, he will say that it is his own 45th birthday and if he is still in the outbound frame, he will say that back on Earth it is “now” Homer’s 39th birthday. However, if an instant later he has made the transition to the inbound frame, he will say that Homer is “now” celebrating his 71st birthday. According to Astro’s clocks it takes 15 years to return, making him 60 years old at the twins reunion. As noted before, according to Astro, 15/γ =9 years will elapse for Homer during the return journey, making Homer 80 years old at their reunion.
We can gain further insight by looking at how the situation evolves if each twin is periodically sending out a light flash at some frequency f as measured by his own clock, say one flash at each birthday. Then each twin can count the flashes received from the other, and by the time the twins come back together again, each twin must have receivedallthesignalssentoutbytheotherduringthetrip. To be consistent with Homer’s faster aging, Astro should receive a total of 20 more flashes than Homer does over the course of the trip.
First consider what Homer sees. He says each leg of the trip takes 25 years. Thus the flash from the turnaround event originates 25 years after Astro’s departure from Earth, according to Homer. However, he doesn’t see it until 45 years after Astro’s departure from Earth because the turnaround point is 20 light-years away and so this flash takes another 20 years to get back to Earth. According to the Doppler formula, Homer receives pulses originating during the outbound leg at the rate   flash per year) = 1/3 flash per year.
(42)
Therefore he receives a total of
	(45 years)(1/3 flash per year) = 15 flashes.	(43)
During the inbound leg he receives pulses at the rate flash per year) = 3 flashes per year.
(44)
He receives these flashes over the course of the remaining 5 years, for a total of 5 · 3=15 more flashes. Thus he has received a total of 15+15=30 flashes, as he should since Astro ages 30 years and therefore sent Homer 30 flashes during the trip.
Now let us calculate how many flashes Astro sees. According to him the outbound leg of the trip takes 15 years, during which time he receives flashes at the rate of 1/3 per year, for a total of 5 flashes. The inbound trip also takes 15 years, during which time he receives flashes at the rate of 3 per year, for a total of 45 flashes. Thus over the course of the entire trip he receives 45+5=50 flashes, in agreement with the fact that Homer has aged 50 years when they are reunited.
If a real human were going on such a journey, he or she would need to be accelerated gradually rather than instantaneously. The calculation of the age difference of the twins, although more complicated, could still be done and would still show Astro to end up younger than Homer. Our civilization does not yet have the technology and resourcestosendlivingbeingsonsuchhigh-speedjourneys, so this particular experimental test has not been done! However, time-dilation effects have been experimentally verified by observing subatomic particles. For example, there is a type of particle called a muon, which has only a short lifetime before it disappears, producing other particles. (The produced particles are the familiar electron and
particles called neutrinos.)
It cannot be predicted exactly when this “decay” of a given muon will occur, but the average lifetime before decay is about 2×10−6 sec. This is the lifetime of a muon as observed in its rest frame. However, muons often travel at speeds very close to the speed of light relative to observers on the Earth. When a large number of muons having a given speed are observed, it is found that the average of their lifetimes does indeed increase by the factor γ.
Time dilation is the reason that significant numbers of muons from cosmic rays are observed at the Earth’s surface. Muons are produced high in the atmosphere of the Earthwhencosmicraysenterfromouterspace.Iftheirlifetimes were not increased due to travelling near the speed of light, very few of them would reach the surface of the Earth before decaying.
F. The Pole and Barn Paradox
Another famous paradox has to do with Lorentz contraction of moving objects. Suppose that there are a long pole and a barn which both have proper length L. The barn has a door at each end that may be quickly opened and closed. An unbelievably fast runner carries the pole and runs through the barn with it, with the pole horizontal and pointed in the runner’s direction of motion. In the rest frame of the barn, the pole is moving and so it would appearshorterthanthebarn.Thereforethepoleshouldeasily fit into the barn. It should be possible to close both doors for a short time, with the pole entirely inside the barn. But in the rest frame of the pole, it is the barn that is moving, and so it would appear shorter than the pole. Therefore the pole should be too long to fit completely inside the barn at any time. At first glance, it seems that we have a contradiction.
The resolution of course has to do with the differing definitions of simultaneity in the two frames. To be definite, suppose that the pole is being carried so fast that the Lorentz factor γ =2. Then the moving pole, as seen in the rest frame of the barn, is contracted to half its proper length. [This would mean that in the barn frame
 2, i.e., the pole is moving at about 87% of the speed of light.]
A spacetime diagram plotted in the frame of the barn
(which we take to be the unprimed frame) is shown in
Fig. 8(a). The world lines of the front door of the barn (labeled F), the back door of the barn (labeled B), the head of the pole (labeled H), and the tail of the pole (labeled T) are straight lines as shown. We assume that the front door is closed immediately after the tail of the pole has passed throughit.Theworldlineofthefrontdooriscross-hatched while the front door is closed. We also assume that the back door is opened immediately before the head of the pole passes through it. The world line of the back door is cross-hatched while the back door is closed. We label four events as follows:
1.	Event HF. Head of pole passes through front door ofbarn
2.	Event TF. Tail of pole passes through front door ofbarn
3.	Event HB. Head of pole passes through back door ofbarn
4.	Event TB. Tail of pole passes through back door ofbarn
 
FIGURE 8 (a) Spacetime diagram in rest frame of barn. (b) Spacetime diagram in rest frame of pole. H labels world-line of head of pole, T labels world-line of tail of pole, F labels world-line of front of barn, and B labels world-line of back of barn. Event HF=“head of pole passes through front door of barn,” event TF=“tail of pole passes through front door of barn,” event HB=“head of pole passes through back door of barn,” event TB=“tail of pole passes through back door of barn.” Cross-hatching on the world line of a door means the door is closed.
We have chosen the origin of coordinates to be the at event TF. Figure 8(a) shows that in the frame of the barn, the four events take place in the order in which we have just listed them. In this frame both doors are closed during the time interval between TF and HB. This is fine, since in this frame the pole is only half as long as the barn, so it easily fits inside for the period of time between events TF and HB.
Figure 8(b) depicts the same situation plotted in the rest frame of the pole (the primed frame, moving at velocity v  2withrespecttotheunprimedframe.Thisfigure shows that the time order of the events TF and HB is different in the two frames! In the pole’s rest frame, the back door is opened, allowing the head of the pole to pass through before the tail of the pole passes through the front door. In this frame, there is never a time when both doors are simultaneously closed. There had better not be, because in this frame the pole is twice as long as the barn, so it cannot fit completely inside at any time. In neither frame does the pole touch either door. Something would be wrong if our reasoning told us the pole could dent a door in one frame but not in the other. We could look at the doors after the fact, and whether or not there is a dent cannot depend on the observer’s frame of reference. However, the answer to the question “Was the pole ever entirely inside the barn?” does depend on the observer’s frame of reference.
Suppose that an observer in the barn rest frame decides she will “prove” that the pole is “really” shorter than the barn by suddenly bringing it to rest while (according to her)itistotallyinsidethebarn.However,“suddenlybringing the pole to rest” means that all pieces of it are brought to rest simultaneously. As we already know, events along the direction of motion—in this case along the length of the pole—that are simultaneous in the barn frame are not simultaneous in the pole frame. Furthermore, no causal influence can go faster than c. It would not be sufficient for the barn-frame observer to just grab the pole at its center with a single short clamp. There is no immediate effect on the rest of the pole—it takes a nonzero amount of time for the ends of the pole to even “know” that the clamp has taken hold of the middle, since no causal influence can go faster than c. Thus we need many clamps stationed along the path of the pole if we want to stop all parts of the pole simultaneously.
So, let us assume that the observer in the barn rest frame times her clamps so that all parts of the pole stop at the sametimeinherframe.Whenthepolehasbeenbroughtto restinthebarn,ithasbeencrushedtoalengthof L/2.This isnowtheproperlengthofthepolesincethepoleisnowat rest in the barn frame. The structure of the pole really has been changed—the barn observer has crushed the pole to half its original proper length using her stopping method. How does this look to an observer in the original rest frame of the pole? His frame continues to move at velocity v  2 with respect to the barn. According to him, clamps near the head of the pole take hold before clamps near the tail of the pole. So he agrees that the pole will get crushedtoashorterlength.Butthefinallengthasobserved in his frame is not its proper length, since the pole does not end up at rest with respect to his frame. He continues to move at speed v with respect to the barn frame, which is the new rest frame of the pole. Therefore the pole is Lorentz contracted from its new proper length of L/2 by another factor of γ =2, to an apparent length of L/4 in his frame.
Other stopping methods are of course possible. All segments of the pole could be brought to rest with respect to the barn by stopping each piece simultaneously as measured in the initial rest frame of the pole. This means that each segment of the pole is given a backwards velocity of−v as observed in the initial rest frame of the pole. The length of the pole in the initial pole rest frame would still be L but this would no longer be its proper length since it endsupmovingat−v withrespecttothatframe,andhence is Lorentz-contracted by the factor γ =2. Once again, the pole has been deformed to a new proper length—this time it is stretched or pulled apart to a new proper length of γ L =2L.
Stopping the pole while maintaining its original proper length throughout the transition from the original pole rest frame to the barn rest frame is more complicated to analyze. In this case, the pole moves smoothly through an infinite sequence of different Lorentz frames. Einstein’s general theory of relativity is better suited to handling such situations involving continuous acceleration than is special relativity.
Obviously, runners carrying poles do not really run fast enough for relativistic effects to be significant! But the electrons in the Stanford linac typically travel down the linac in groups (“bunches”) that are about a centimeter long as observed in the rest frame of the linac. For a Lorentz factor γ =105, the proper length of a bunch (that is, the length as observed in the rest frame of the bunch) is therefore about a kilometer. As noted earlier, in the frame of an electron with this value of γ the linac is only about three centimeters long, obviously much shorter than the properlengthofthebunch.Whetherornotthebunch“fits” inside the linac depends on your reference frame!
V. RELATIVISTIC TREATMENT OF ENERGY AND MOMENTUM
Twoveryfundamentallawsofmechanicsareconservation of energy and momentum. These laws are extremely useful in analyzing physical situations. They say that the total amountofenergyandthetotalamountofmomentuminan isolated physical system do not change with time. Since they are so useful, we would hope to have similar conservation laws in special relativity. We will also want the new relativistic definitions of mass, energy, and momentum to reduce to the old Newtonian ones in situations where the velocities involved are much less than the speed of light. Allthiscanbedone,butsomemodificationstoournotions of mass, energy, and momentum are required. To motivate the new definitions, we will look at situations involving collisions between two objects. Even in these simple situations the arguments are a little more complicated than in most of this article. However, following through the reasoning will yield some further insight into the analysis of relativistic problems. The main results are summarized at the end of this section. The usefulness and validity of the new definitions have been borne out by all known relevant experimental evidence.
A. Relativistic Momentum
Momentum conservation would not be preserved under Lorentz transformations, if we used the Newtonian definition of momentum p=mv, where m is the mass. Let us try introducing a multiplicative function f (v) that is a function of the speed v of the object (remembering that speedv isjustthemagnitudeofthevelocityv,i.e.,v =|v|). We start by guessing that the momentum in a frame where the object moves with velocity v is given by
	mf (v)v.	(45)
Our first goal is to see if we can find a functional form for the dependence of f (v) that satisfies both momentum conservation and the principle of relativity (i.e., momentum conservation holds in all inertial frames). For v c we want the momentum to agree with the Newtonian definition, thus we require f (v)→1 as v →0.
To find out what f (v) must be, we consider an elastic collision between two objects of equal mass m. “Elastic” means that the two objects bounce apart without dissipating any of their incoming kinetic energy as other forms of energy. We will look at this collision from two different inertial frames. Choose one frame to be the center of mass (CM) frame, which is the frame in which the total momentum is zero. In this frame the momenta of A and B are equal in magnitude and opposite in direction. We can choose the spatial coordinate axes in this frame, which we will label the unprimed frame, so that the collision looks as shown in Fig. 9(a). [Note this is not a diagram in space– time; it is simply a diagram of the paths of the objects in two space dimensions.] Since the masses are equal and the collision is symmetric in this frame, A has an equal and opposite velocity to B, both before and after the collision. Since the collision is elastic, the speed of each object before the collision is the same as its speed afterwards.
In this frame, we assume that A departs from the line y =−D/2 at the same time B departs from the line y =+D/2,andtheyhaveequalspeedsv.Atatime TCM/2 later,theycollideattheoriginandeachreversesitscomponent of velocity along the y-axis. After an additional time TCM/2, A returns to the line y =−D/2 and B returns to the line y =+D/2. Since the total distance travelled by each object along the y direction during the time TCM is
D, the magnitude of the y velocity component is D/TCM.
Since each object reverses the direction of its y velocity
 
FIGURE 9 Elastic collision of particles A and B. (a) As viewed in center of mass frame (chosen to be unprimed frame). (b) As viewed in frame moving with longitudinal velocity of particle A (primed frame).
component during the collision, the y component of momentum change in the collision is −2mf (v)D/TCM for A and +2mf (v)D/TCM for B. From the symmetry of the collision as viewed in this frame, it is obvious that the total momentum is conserved—it is zero both before and after the collision.
Now we impose the requirement that momentum conservation should hold for any other inertial frame as well. In particular, we consider a (primed) frame that is moving to the right at speed vx with respect to the unprimed frame. We choose vx to be the velocity component of A along the x-axis, as observed in the unprimed frame. Thus in the primed frame A just moves straight up the y axis and back down, while B follows a longer path, as shown in Fig. 9(b), with velocity component vx ,B along the x-axis. [Note that vx ,B is NOT the value −2vx that we would get if the Galilean transformation, and hence straightforward addition of velocities, were valid.]
We know that Lorentz transformations along a given direction do not change the observed distances transverse to that direction, so the total distance in the y direction travelled by each object is also D in the primed frame. We also know that events which are simultaneous in one frame are not simultaneous in another, when the events are separated along the direction of relative motion of the two frames. By symmetry, the departure events were simultaneous in the unprimed frame and so were the return events; we implicitly assumed this when we said that the total time of the trip for each object was the same value TCM. But this is not true in the primed frame, contrary to what nonrelativistic intuition would lead us to expect. The departure and return events for A occur at the same place in the primed frame. So, the time between these events as measured in the primed frame is the proper time between theevents,whichwewillcall T0.Therefore,asobservedin the primed frame, the momentum change in the collision for A is
	 D/T0,	(46)
where vA = D/T0 is the total speed of A in the primed frame.
Now let us calculate the momentum change of B during the collision, as observed in the primed frame. If we had been in a frame in which B moved straight down and then back up the y-axis, then by symmetry B’s round trip time would have been T0 in that frame. But the primed frame moves at velocity vx ,B with respect to such a frame. Therefore, from Lorentz time dilation, the time between the departure and return of B in the primed frame is
T0
	T .	(47)
So, as observed in the primed frame, the momentum change in the collision for B is
	pB	 B D/T.	(48)
where (D/T)2 is the total speed of B in the primed frame.
The momentum changes in Eqs. (46) and (48) must
sum to zero if conservation of momentum is to hold in the primed frame. Using Eq.(47) to eliminate T/T0, this requirement gives
	mf	 A	mf  .	(49)
Thefinalstepinthisargumentistotakethelimitofthisexpression as D approaches zero, so that the y-components of the velocities of both objects approach zero. In other words, we consider the extreme case where A and B just graze each other. In this limit, A is at rest in the primed frame so that f  1. Also, in this limit B’s velocity is entirely along the x-axis, so that   is its total speed. Thus we obtain
m
	mf (v.	(50)
B
This example shows that our initial assumption [that momentumisgivenbymf (v)v]canonlyholdifthefunctional form for f (v) is
	f  ,	(51)
where v is the speed. Thus f (v) is just the Lorentz factor γ introduced previously. The resulting definition of momentum is
	p = γmv = γm dx/dt.	(52)
This prescription gives consistent results in agreement with experiment and is what is adopted in special relativity.
B. Relativistic Energy and the Momentum-Energy Four-Vector
Notethattherelativisticdefinitionofmomentum,Eq.(52), can also be expressed as
	p = m dx/dτ.	(53)
Here we simply differentiate with respect to proper time along the world line of the object.
Given this way of writing p, it is natural to try adding a fourth component
	pt = md(ct)/dτ = mcγ	(54)
and see whether the resulting four-vector is a useful concept. Consider the quantity analogous to the space–time interval, but replacing t, x, y, z by pt, px, py, pz:
pt2  
	[c2 dt2	dx2	dy2	dz2]
	2	−	−	−
= m.
dτ2
(55)
The expression in brackets in the last line is just the space– time interval ds2. Assuming that this interval is timelike (as it must be if the object is traveling at less than the speed of light), we have ds2 =c2 dτ2 so we are left with
	pt2  .	(56)
Like the space–time interval, this quantity is an invariant since it depends only on the mass m and the speed of light c, both of which are the same in all frames. But what is the realsignificanceof pt?Wehavealreadyconcludedthatthe momentum vector (px, py, pz) is conserved. It therefore seems natural to guess that pt might also be conserved and related to the energy. Multiplying pt by another factor of c to get energy in the usual units, we make the guess that γmc2 is the energy of an object with mass m and speed v. If we define the total energy in this way, we see that there is a new contribution to the energy. Even when the speed of the object is zero, it still has an nonzero energy, the rest energy given by
	Erest = mc2,	(57)
where m is the object’s mass. As stated earlier, we define the energy of a moving object to be
	Etot = γmc2,	(58)
where   and v is the object’s speed.
Toseethatthisdefinitionoftheenergyreducestosomething reasonable in the nonrelativistic limit v c, we expand it in a power series in v/c:
E = γmc 
	 	(59)
Thus in this limit the energy is the sum of the rest energy, the nonrelativistic kinetic energy  mv2, and higher order terms in v2/c2 that are much smaller than the first two terms when v c.
Let us verify that energy defined in this way is conserved in an inelastic collision, namely one in which two objects collide head-on and stick together. Suppose the two objects have equal masses m and we view the collision in a frame (call it the primed frame) where the objects approach each other with equal speeds v along opposing directions, say parallel to the x-axis [see Fig. 10(a)]. Since the masses of the two incoming objects are equal, this is the center-of-mass (CM) frame, i.e., the frame in which the total momentum of the system is zero. From momentum conservation, the objects will be at rest in this system after they collide and stick together.
We have chosen A to be the object moving to the right and B the one moving to the left. Now let us Lorentz transform to the rest frame of B; call this the unprimed frame. The primed frame moves with speed v to the right with respect to the unprimed frame. The collision as observed in the unprimed frame is shown in Fig. 10(b). From the velocity combination formula, the velocity of A in the unprimed frame is
2v
	V  .	(60)
A little algebra then gives
	 .	(61)
Therefore the energy of A in the unprimed frame is
	mc2	2 (1 + v2/c2)
EA  = mc  
 
FIGURE 10 Inelastic collision of particles A and B. (a) As viewed in center of mass frame (chosen to be primed frame). (b) As viewed in rest frame of particle B (unprimed frame).
Object B is at rest in the unprimed frame, so the total incoming energy as observed in this frame is
(1 + v2/c2) Ein
After the collision, the composite object C (formed when A and B stick together) is at rest in the primed frame and moves with speed v in the unprimed frame. Thus the energy of C in the unprimed frame (which is the total energy going out from the collision as observed in this frame) is related to the total outgoing energy in the primed frame by
Eout
	Eout.	(64)
1 − v2/c2
Applying momentum conservation in the unprimed frame and denoting the mass of C by M, we have
	Mv	mV
	 m · 0.	(65)
Substituting for V and 1− V 2/c2 from Eqs. (60) and (61) we find
2m
	M .	(66)
Clearly mass is not conserved in the collision, since the total mass of the incoming objects was 2m. The final mass is increased—we will discuss this further. For the moment we simply note that unlike in Newtonian physics, in relativity, the total mass is not a conserved quantity.
The outgoing energy in the unprimed frame is Eout =
Mc . From Eq. (66), this may be written
	Eout .	(67)
Comparing Eqs. (64) and (67) for Eout we see that the energy Eout of C in the primed frame is given by
	Eout	 .	(68)
Thus, at least for this example and in the primed frame, we have shown that energy is conserved in the collision, since the energy of each of the incoming objects is mc . Furthermore, from Eqs. (63) and (67), it is obvious that conservation of energy holds in the unprimed frame as well.
C. Summary
1. Definitions of Momentum and Energy
In summary the relativistic definitions of momentum and energy of an object with mass m, in a frame where it is moving with velocity v, are as follows:
p = γmv = γm dx/dt = m dx/dτ.	(69)
E = γmc2.	(70)
Here γ is the Lorentz factor 1/ .
Sometimes the quantity γm is called the relativistic mass and m itself called the rest mass. Modern convention is to simply refer to m as the mass and to avoid the term
“relativistic mass.”
Energy and momentum are conserved in an isolated system, that is, in a given frame the value of the total energy(summedoverallpartsofthesystem)andthevalue of the total momentum does not change with time. Mass, however, is not conserved in general.
On the other hand, the mass of an object at any given moment is an invariant, that is, it is the same as observed in all frames. The values of the energy and momentum, however, depend on the observer’s reference frame.
2.	Relativistic Relationship BetweenEnergy, Momentum, and Mass
Equations (57) and (58) are two correct interpretations of Einstein’s famous equation E =mc2. The general equation, however, is
	E2 = p2c2 + m2c4.	(71)
This is simply a rewrite of Eq. (56) in terms of E =cpt and p . Eq. (71) is the correct relativistic relationship between the total energy, momentum, and mass of an object.
3.	Lorentz Transformation of Momentum-EnergyFour-Vector
We have shown that the component pt = E/c which we introduced to make a four-vector is just the total energy apart from the factor of c. Our discussion has shown that the momentum-energy four-vector, defined as (E/c, px, py, pz) satisfies a relation reminiscent of the invariance of the spacetime interval, i.e., the same combination of its components is also an invariant.
Like the space–time components t, x, y, z, the components of the momentum-energy four-vector transform according to the Lorentz transformation. Assuming that the primed frame moves with velocity v along the x-axis with respect to the unprimed frame, we have: px = γ(px − βE/c)
py = py
(72)
pz = pz
E/c = γ(E/c − βpx).
4.	Particles with Zero Mass
Wenotedthatanobjectwithnonzeromasscanneverreach or exceed the speed of light. However, there are particles withzeromassthattravelwithspeedexactlyc.Thegeneral relationship Eq. (71) between mass, energy, and momentum says that if m = 0 then
	E = pc.	(73)
The quantum theory asserts that light has a dual waveparticle nature; the particles which make up light are particles with zero mass called photons. The relationship E = pc is indeed consistent with all experiments and observationsinvolvingphotons,forexample,observationsof collisions of photons with electrons (the Compton effect).
5.	Conversion Between Different Forms of Energy
Note that even in nonrelativistic physics, if energy is to be conserved in an inelastic collision, then the kinetic energy of the incoming objects must go into some other form of energy—after all, in the center of mass frame, the kinetic energy is zero after the collision. For example, the initial kinetic energy of the incoming particles may be absorbed as an increase in the internal energy of motion of the molecules comprising the composite body formed in the collision (and perhaps its environment). This means that the temperature is very slightly increased. What is different in relativity is that when the internal energy and temperature change, so does the mass. The change in mass is extremely tiny in situations we are familiar with in everyday life, since the conversion factor c2 between “mass” and “energy” is so huge. As we have already noted, mass (and thus rest energy) is not a conserved quantity in relativity.
Conversion of rest energy to other forms of energy occurs on a significant scale in nuclear reactions. These are of two basic types, fission reactions and fusion reactions. In a fission reaction, a single atomic nucleus dissociates into two or more pieces, where the sum of the masses of the pieces is less than the mass of the original nucleus. The difference in rest energy is transformed into kinetic energyofthepieces.Inafusionreaction,twonucleifuseto form a nucleus that has less mass than the sum of original nuclei. The corresponding leftover rest energy is released partly as high energy electromagnetic radiation (including ordinary visible light). This is the mechanism by which the sun and other stars shine.
On a much smaller scale, the same type of thing happens when energy is released or absorbed in normal chemical reactions. The amount of energy involved is so small however, that the fractional difference in mass between the initial and final constituents is extremely tiny.
D. Force and Newton’s Second Law in Relativity
Newton’s Second Law, which relates the change in momentum of an object to the force F acting upon it, may be written in the form
	F = dp/dt.	(74)
It turns out to be useful to define force such that this equation may still be used in relativity. In non-relativistic physics, Eq. (74) is equivalent to both F=ma and F=mv/dt.Thisisnotthecaseinrelativitysincep=γmv andγ dependsonthevelocity.Infact,inrelativitytheforce and the acceleration are not necessarily even in the same direction.
As v approaches c, the Lorentz factor γ approaches infinity and thus so do the momentum and the energy. This is consistent with the observation that an object with nonzero mass can never quite reach the speed of light, no matter how much force is exerted on it.
VI. SPECIAL RELATIVITY AND ELECTROMAGNETISM
Maxwell’s equations are one example of the postulate that fundamental laws of physics should be invariant with respect to changes from one inertial frame to another via a Lorentz transformation. Relativity shows that electric and magnetic fields are aspects of the same entity—the electromagnetic field. Indeed Einstein said,
What led me more or less directly to the special theory of relativity was the conviction that the electromotive force acting on a body in motion in a magnetic field was nothing else but an electric field.
More precisely, when a pure electric field in one frame
(e.g., the unprimed frame) is viewed from another frame (theprimedframe)inmotionwithrespecttothefirst,there can be a nonzero magnetic field in the second frame.
As usual we will assume the primed frame is moving with speed v along the x-axis, and that the x and xaxes are in the same direction. In this case, the transformation of the components of the electric field and the magnetic field is given by
Ex = Ex,
Ey = γ[Ey − (v/c)Bz],
Ez = γ[Ez + (v/c)By],	Bx = Bx
By = γ[By + (v/c)Ez]
Bz = γ[Bz − (v/c)Ey].	(75)
We shall not derive this result here. However, it follows from the Lorentz transformation plus one additional assumption.
ThisadditionalingredientisCoulomb’sLaw,whichwas formulated in the 18th century. Coulomb’s Law gives the force F exerted by one charge (with charge q1) upon another charge (with charge q2), assuming both charges are at rest:
q q
F.	(76) r2
Here r is the distance between the two charges, k is a constant, and the force F acts along the line through the two charges. If q1 and q2 have the same sign, the force is repulsive; if they have the opposite sign, the force is attractive. Coulomb’s Law may be rewritten as
	F = q2E,	(77)
where E is the magnitude of the electric field at q2:
q1
E = k  .	(78) r2
The magnetic field is an effect that may arise simply because one has changed reference frames. This is apparent from the above transformation. For example, suppose that in the unprimed frame there is no magnetic field, that is, Bx = By = Bz =0.FromEq.(75)weseethatintheprimed frame there are nonzero magnetic field components By and Bz transverse to the direction of motion of the primed frame if Ey or Ez is non-zero. Furthermore the transverse components of the electric field are different in the primed and unprimed frames.
Consider, for example a single point charge at rest in the unprimed frame. From Coulomb’s law, we know that the electric field is radially symmetric as shown on the left hand side of Fig. 11. The field is stronger where the field lines are closer together. Suppose the charge is in motion with velocity v as shown on the right hand side of Fig. 11. Then the electric field is “flattened” along the direction of motion as shown. The field strength is increased transverse to the direction of motion and decreased parallel to the the direction of motion. In this particular example, v/c  9, so that γ =3. For larger v (and thus larger γ), the field would be flattened even more.
This transformation of the electric and magnetic fields is relevant in high energy particle accelerators, such as the linac discussed earlier. A linac accelerates a large number of charged particles, for example electrons, in a single short bunch. The mutual electrical repulsion of the electrons would be extremely strong if such a bunch were so short when at rest. However when the speed of the bunch is high enough, the forces between the electrons become almost negligible. This is due to two effects, both arising from the Lorentz transformation of the fields. One effect is that the electric field is mostly transverse as shown, so that it becomes small for electrons having different x coordinates.Theothereffectisthatevenforelectronshaving essentiallythesame x coordinate,thenetforceapproaches zero as v approaches c, because the electric and magnetic forces tend to cancel each other in this limit. The calculation of the magnetic force on a charge is slightly more complicated than the calculation of the electric force—the magnetic force is perpendicular both to the direction of B and the direction of the velocity of the charge, and it depends on the magnitude of the velocity. However, the net result is that the electric and magnetic forces between two electrons having essentially the same x coordinate nearly cancel, if they are moving at sufficiently high speed along the x-axis.
Another way to see that the electrons are not much affected by each others’ electric and magnetic fields is to take account of Lorentz contraction of the bunch. In the frame where the compact bunch is moving at very high speed, it is Lorentz contracted by a factor γ compared to its proper length. In the rest frame of the bunch, the bunch length (its proper length) is much longer so that the forces (given by Coulomb’s Law) are reduced due to the increased distance between particles.
VII. SPECIAL RELATIVITY AND QUANTUM MECHANICS
 
FIGURE 11 Electric field of a charged particle at rest (left), and of a charged particle moving with uniform velocity v such that γ =3 (right). [Reproduced with permission from Jackson, J. D. (1975). “Classical electrodynamics,” 2nd ed., p. 555, Wiley, New York.]
OtherdevelopmentsoccurringinparalleltoEinstein’sformulation of special relativity eventually led to an entirely new picture of the behavior of matter at the subatomic level, the realm of quantum phenomena. Quantum mechanics, a branch of physics that was motivated by studies of atomic structure and radiating bodies, eventually led to modifications of mechanics, in addition to those required in going from Newtonian mechanics to special relativity. According to quantum mechanics, light exhibits both particle properties and wave properties, and so do other “objects” (e.g., electrons).
Special relativity retains in common with Newtonian mechanics the assumptions that (1) light is a wave, and (2) Newtonian determinism is valid (that is, there is no limitation in principle on how precisely we can simultaneously measure positions and velocities in a system, and we can use these measurements to predict the state of the system at later times). Quantum mechanics, ontheotherhand,saysthatthereisaninherentuncertainty in the measurement process. The minimum uncertainty in theproductofthepositionuncertaintyx andthemomentumuncertaintyp isgivenbytheHeisenberguncertainty principle
	xp ≥ h,	(79)
whereh isPlanck’sconstant.Planck’sconstantisanumber so small that this uncertainty is irrelevant in everyday life wheretheobjectswedealwitharemuchlargerthanatoms. The combination of special relativity and quantum mechanics has been very fruitful, leading to the formulation of quantum field theory. This synthesis was achieved by the middle of the 20th century, and is our current framework for describing and understanding the behavior of the most elementary particles observed in nature. As we have seen, the main motivation driving the development of special relativity was the desire to account correctly for electromagnetic phenomena. When electrodynamics was extendedintothequantumdomain,theresultwasquantum electrodynamics, the prototype quantum field theory. The underlying principles were further generalized to allow theincorporationofadditionalphenomena—inadditionto electromagnetism, there exist other interactions between certain particles. These include the “strong” and “weak” forces, that are important, for example, in understanding how the nuclei of atoms are constructed.
A. Antiparticles
One consequence of quantum field theory is the necessity for the existence of antiparticles. This comes about because it is possible for Lorentz transformations to reverse the time order of two events x1 and x2 that have a space-like separation. “Space-like separation” means that the spatial separation of the two events is greater than c times their time separation. Thus, special relativity would say that there is no way for a particle to propagate from one event to the other, if quantum mechanics is ignored. But due to the uncertainty principle in quantum mechanics, there is a nonzero probability for a particle originating at x1 to be absorbed at x2 even when the two events have space-like separation. If the separation is space-like, in some other frame it can look like a particle originated at x2 and was absorbed at x1. If the particle was electrically charged, then from charge conservation its “timereversed” form must appear to have the opposite charge. The mass is invariant, the same in all frames. Each type of charged subatomic particle is therefore required to have a corresponding type of antiparticle with opposite charge and identical mass.
Acharacteristicfeatureofveryhighenergycollisionsof subatomic particles is that new particle–antiparticle pairs are sometimes created. In some experiments, an electron may collide with its antiparticle (the positron) after both particles have been accelerated to very high energy. The electron and positron can annihilate each other—all of their rest energy plus their incoming kinetic energy is then available to produce other particles, so long as the sum of the rest energies of the produced particles is less than the original total energy and all other conservation laws (momentum, charge, etc.) are satisfied.
VIII. GENERAL RELATIVITY
The term “special” in special relativity refers to the fact that it is really only a restricted version of a more general theory of relativity which was put forth by Einstein in 1916. General relativity treats all reference frames—not just all inertial reference frames—on an equal basis. General relativity can readily be used to analyze situations in which observers are accelerating and/or gravitational fields are present.
SEE ALSO THE FOLLOWING ARTICLES
COSMOLOGY • ELECTRODYNAMICS, QUANTUM • ELECTROMAGNETICS • MECHANICS, CLASSICAL • OPTICAL
INTERFEROMETRY • PARTICLE PHYSICS, ELEMENTARY • QUANTUM THEORY • RELATIVITY, GENERAL • STELLAR
STRUCTURE AND EVOLUTION • TIME AND FREQUENCY
BIBLIOGRAPHY
Feynman, R. P., Leighton, R. B., and Sands, M. (1963). “The Feynman Lectures on Physics,” Addison-Wesley, Reading, Massachusetts. French, A. P. (1968). “Special Relativity,” W. W. Norton and Company, New York.
Jackson, J. D. (1975). “Classical Electrodynamics,” 2nd ed., Chapters 11 and 12, Wiley, New York.
Rindler, W. (1969). “Essential Relativity,” Van Nostrand Reinhold, New York.
Sartori, L. (1996). “Understanding Relativity,” University of California Press, Berkeley and Los Angeles, CA.
Stachl, J. (1998). “Einstein’s Miraculous Year,” Princeton University Press, Princeton, NJ.
Taylor,E.F.,andWheeler,J.A.(1992).“SpacetimePhysics:Introduction to Special Relativity,” 2nd ed., W. H. Freeman, New York.

"""
start = time.time()
n = Encryption(n,N,PNA)
end = time.time()
print("암호화 :",end - start,"s")

start = time.time()
n = Decryption(n,N,PNB)
end = time.time()
print("복호화 :",end - start,"s")