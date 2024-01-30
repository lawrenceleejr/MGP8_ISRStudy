# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-00073-fragment.py --python_filename SUS-RunIISummer20UL18wmLHEGEN-00073_1_cfg.py --eventcontent RAWSIM,LHE --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN,LHE --fileout file:SUS-RunIISummer20UL18wmLHEGEN-00073.root --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN --geometry DB:Extended --era Run2_2018 --mc -n 100000
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('GEN',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIISummer20UL18wmLHEGEN-00073-fragment.py nevts:100000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:SUS-RunIISummer20UL18wmLHEGEN-00073.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:SUS-RunIISummer20UL18wmLHEGEN-00073_inLHE.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')

process.dirhadrongenfilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(100.0, 100.0),
    MinEta = cms.untracked.vdouble(-100, -100),
    MinP = cms.untracked.vdouble(0.0, 0.0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    ParticleCharge = cms.untracked.int32(0),
    ParticleID1 = cms.untracked.vint32(
        1000993, 1009213, 1009313, 1009323, 1009113, 
        1009223, 1009333, 1091114, 1092114, 1092214, 
        1092224, 1093114, 1093214, 1093224, 1093314, 
        1093324, 1093334
    ),
    ParticleID2 = cms.untracked.vint32(
        1000993, 1009213, 1009313, 1009323, 1009113, 
        1009223, 1009333, 1091114, 1092114, 1092214, 
        1092224, 1093114, 1093214, 1093224, 1093314, 
        1093324, 1093334
    ),
    Status = cms.untracked.vint32(1, 1)
)


process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 147', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 2', 
            'JetMatching:doShowerKt = off', 
            '6:m0 = 172.5', 
            '24:mMin = 7', 
            'Check:abortIfVeto = on'
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'JetMatchingParameters', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'SUSY:all = off', 
            'SUSY:gg2gluinogluino = on', 
            'SUSY:qqbar2gluinogluino = on', 
            'RHadrons:allow  = on', 
            'RHadrons:allowDecay = off', 
            'RHadrons:setMasses = on', 
            'RHadrons:probGluinoball = 0.1'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    SLHATableForPythia8 = cms.string('\nBLOCK MASS\n   2000001     1.00000000E+05\n   2000002     1.00000000E+05\n   2000003     1.00000000E+05\n   2000004     1.00000000E+05\n   2000005     1.00000000E+05\n   2000006     1.00000000E+05\n   2000011     1.00000000E+05\n   2000013     1.00000000E+05\n   2000015     1.00000000E+05\n   1000001     1.00000000E+05\n   1000002     1.00000000E+05\n   1000003     1.00000000E+05\n   1000004     1.00000000E+05\n   1000005     1.00000000E+05\n   1000006     1.00000000E+05\n   1000011     1.00000000E+05\n   1000012     1.00000000E+05\n   1000013     1.00000000E+05\n   1000014     1.00000000E+05\n   1000015     1.00000000E+05\n   1000016     1.00000000E+05\n   1000021     1500\n   1000022     1.00000000E+00\n   1000023     750\n   1000024     750\n   1000025     1.00000000E+05\n   1000035     1.00000000E+05\n   1000037     1.00000000E+05\n#\nDECAY   2000001     0.00000000E+00\nDECAY   2000002     0.00000000E+00\nDECAY   2000003     0.00000000E+00\nDECAY   2000004     0.00000000E+00\nDECAY   2000005     0.00000000E+00\nDECAY   2000006     0.00000000E+00\nDECAY   2000011     0.00000000E+00\nDECAY   2000013     0.00000000E+00\nDECAY   2000015     0.00000000E+00\nDECAY   1000001     0.00000000E+00\nDECAY   1000002     0.00000000E+00\nDECAY   1000003     0.00000000E+00\nDECAY   1000004     0.00000000E+00\nDECAY   1000005     0.00000000E+00\nDECAY   1000006     0.00000000E+00\nDECAY   1000011     0.00000000E+00\nDECAY   1000012     0.00000000E+00\nDECAY   1000013     0.00000000E+00\nDECAY   1000014     0.00000000E+00\nDECAY   1000015     0.00000000E+00\nDECAY   1000016     0.00000000E+00\n\nDECAY   1000021     1.00000000E+00\n     0.00000000E+00    3         -6          6    1000022\n     1.00000000E-01    3         -1          1    1000023\n     1.00000000E-01    3         -2          2    1000023\n     1.00000000E-01    3         -3          3    1000023\n     1.00000000E-01    3         -4          4    1000023\n     1.00000000E-01    3         -5          5    1000023\n     1.25000000E-01    3         -2          1    1000024\n     1.25000000E-01    3          2         -1    -1000024\n     1.25000000E-01    3         -4          3    1000024\n     1.25000000E-01    3          4         -3    -1000024\n\nDECAY   1000023     1.00000000E-01\n     1.00000000E+00    2         22    1000022\nDECAY   1000024     1.00000000E-01\n     0.0000000    3     1000022        -1      2\n     1.0000000    2     1000022        24\n\nDECAY   1000022     0.00000000E+00\n'),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    hscpFlavor = cms.untracked.string('gluino'),
    massPoint = cms.untracked.int32(1800),
    maxEventsToPrint = cms.untracked.int32(1),
    particleFile = cms.untracked.string('Configuration/Generator/data/particles_gluino_1800_GeV.txt'),
    pdtFile = cms.FileInPath('Configuration/Generator/data/hscppythiapdtgluino1800.tbl'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    slhaFile = cms.untracked.string('Configuration/Generator/data/HSCP_gluino_1800_SLHA.spc'),
    useregge = cms.bool(False)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/UL/13TeV/madgraph/V5_2.6.5/sus_sms/SMS-GlGl/SMS-GlGl_mGl-1500_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(100000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.dirhadrongenfilter)

# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step,process.LHEoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
