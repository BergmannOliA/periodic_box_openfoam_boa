// Solve the Momentum equation

MRF.correctBoundaryVelocity(U);

const dimensionedVector BodyForce("BodyForce", dimensionSet(0,1,-2,0,0,0,0), vector(-0.0025,0,0));

tmp<fvVectorMatrix> tUEqn
(
    fvm::ddt(U) + fvm::div(phi, U)
  + MRF.DDt(U)
  + turbulence->divDevReff(U)
 ==
    fvOptions(U)
  + BodyForce
);
fvVectorMatrix& UEqn = tUEqn.ref();

UEqn.relax();

fvOptions.constrain(UEqn);

if (pimple.momentumPredictor())
{
    solve(UEqn == -fvc::grad(p));

    fvOptions.correct(U);
}
