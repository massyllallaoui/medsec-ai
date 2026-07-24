'use client';
import { useState } from 'react';

export default function Home() {
  const [email, setEmail] = useState('radio@example.com');
  const [password, setPassword] = useState('azerty123');
  const [token, setToken] = useState('');
  const [statusMsg, setStatusMsg] = useState('');
  const [file, setFile] = useState(null);
  
  const [currentScanId, setCurrentScanId] = useState(null);
  const [aiDiagnosis, setAiDiagnosis] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // --- SIMULATION API : CONNEXION ---
  const handleLogin = async (e) => {
    e.preventDefault();
    if (email === 'radio@example.com' && password === 'azerty123') {
      setToken('demo-jwt-token-12345');
      setStatusMsg('');
    } else {
      setStatusMsg('Identifiants incorrects (Essayez radio@example.com / azerty123)');
    }
  };

  // --- SIMULATION API : UPLOAD ---
  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file) return alert("Veuillez sélectionner une imagerie médicale.");
    
    setCurrentScanId(null);
    setAiDiagnosis('');
    setStatusMsg('Transmission chiffrée en cours...');
    setIsLoading(true);

    // On simule 1.5s de temps d'upload
    setTimeout(() => {
      setCurrentScanId('demo-' + Math.random().toString(36).substring(2, 10));
      setStatusMsg('Image sécurisée. Analyse tensorielle en cours...');
      setIsLoading(false);
    }, 1500);
  };

  // --- SIMULATION API : RÉSULTAT IA ---
  const checkResult = async () => {
    if (!currentScanId) return;
    setAiDiagnosis("Calcul des couches ResNet-50 en cours...");
    
    // On simule 2s de calcul PyTorch
    setTimeout(() => {
      setAiDiagnosis("Structure tissulaire analysée sans anomalie majeure. (Confiance IA : 94.2%)");
      setStatusMsg('Analyse terminée.');
    }, 2000);
  };

  // --- INTERFACE DE CONNEXION ---
  if (!token) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-100 px-4">
        <div className="max-w-md w-full bg-white rounded-2xl shadow-xl border border-slate-100 p-8">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">MedSec <span className="text-blue-600">AI</span></h1>
            <p className="text-sm text-slate-500 mt-2">Portail d'Imagerie Clinique Sécurisé (Mode Démo)</p>
          </div>
          <form onSubmit={handleLogin} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Identifiant Praticien</label>
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} 
                className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition" />
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Mot de passe</label>
              <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} 
                className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition" />
            </div>
            <button type="submit" 
              className="w-full bg-slate-900 hover:bg-slate-800 text-white font-semibold py-3 px-4 rounded-lg transition duration-150 ease-in-out shadow-md">
              Authentification Sécurisée
            </button>
          </form>
          {statusMsg && <p className="mt-4 text-center text-sm text-red-500 font-medium">{statusMsg}</p>}
        </div>
      </div>
    );
  }

  // --- DASHBOARD CLINIQUE ---
  return (
    <div className="min-h-screen flex bg-slate-50">
      <aside className="w-64 bg-slate-900 text-slate-300 flex flex-col hidden md:flex">
        <div className="p-6">
          <h2 className="text-2xl font-bold text-white tracking-tight">MedSec <span className="text-blue-500">AI</span></h2>
          <p className="text-xs uppercase tracking-wider text-slate-500 mt-2">Secteur: Radiologie</p>
        </div>
        <nav className="flex-1 px-4 space-y-2 mt-4">
          <a href="#" className="flex items-center px-4 py-3 bg-blue-600/10 text-blue-400 rounded-lg font-medium border border-blue-500/20">
            <svg className="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
            Nouvelle Analyse
          </a>
          <a href="#" className="flex items-center px-4 py-3 text-slate-400 hover:bg-slate-800 rounded-lg font-medium transition">
            <svg className="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            Historique Patients
          </a>
        </nav>
        <div className="p-4">
          <button onClick={() => setToken('')} className="w-full px-4 py-2 text-sm text-slate-400 hover:text-white border border-slate-700 rounded-lg transition">Déconnexion</button>
        </div>
      </aside>

      <main className="flex-1 p-8 md:p-12 overflow-y-auto">
        <header className="mb-10">
          <h1 className="text-3xl font-bold text-slate-900">Acquisition d'Imagerie</h1>
          <p className="text-slate-500 mt-1">Plateforme propulsée par PyTorch & ResNet-50. (Mode Démo)</p>
        </header>

        <div className="max-w-3xl">
          <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
            <form onSubmit={handleUpload}>
              <div className="border-2 border-dashed border-slate-300 rounded-xl p-10 text-center hover:bg-slate-50 transition cursor-pointer relative">
                <input type="file" onChange={(e) => setFile(e.target.files[0])} className="absolute inset-0 w-full h-full opacity-0 cursor-pointer" />
                <svg className="mx-auto h-12 w-12 text-slate-400 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path></svg>
                <p className="text-slate-600 font-medium">Cliquez ou glissez une imagerie médicale ici</p>
                <p className="text-xs text-slate-400 mt-2">DICOM, PNG, JPG jusqu'à 50MB</p>
                {file && <div className="mt-4 inline-block bg-blue-50 text-blue-700 font-medium px-4 py-2 rounded-full text-sm border border-blue-100">Fichier prêt : {file.name}</div>}
              </div>
              <button type="submit" disabled={isLoading} 
                className={`mt-6 w-full font-semibold py-3 px-4 rounded-xl transition shadow-sm ${isLoading ? 'bg-slate-400 cursor-not-allowed text-white' : 'bg-blue-600 hover:bg-blue-700 text-white'}`}>
                {isLoading ? 'Chiffrement et envoi...' : 'Transmettre au moteur IA'}
              </button>
            </form>
          </div>

          {currentScanId && (
             <div className="mt-8 bg-slate-900 rounded-2xl p-8 shadow-lg text-slate-100 relative overflow-hidden">
                <div className="absolute top-0 right-0 p-4 opacity-10">
                  <svg className="w-24 h-24" fill="currentColor" viewBox="0 0 24 24"><path d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                </div>
                
                <h3 className="text-xl font-bold mb-2 flex items-center">
                  <span className="w-3 h-3 rounded-full bg-green-400 mr-3 animate-pulse"></span>
                  Rapport de Diagnostic Tensoriel
                </h3>
                <p className="text-xs font-mono text-slate-400 mb-6">ID Scan : {currentScanId}</p>
                
                <div className="bg-slate-800 rounded-xl p-5 border border-slate-700 mb-6">
                  {aiDiagnosis ? (
                    <p className="text-lg font-medium text-white">{aiDiagnosis}</p>
                  ) : (
                    <div className="flex items-center text-slate-400">
                      <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-blue-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Traitement asynchrone dans le Worker Celery...
                    </div>
                  )}
                </div>

                <button onClick={checkResult} className="bg-slate-700 hover:bg-slate-600 text-white text-sm font-medium py-2 px-6 rounded-lg transition border border-slate-600 shadow-sm">
                  Actualiser le Résultat
                </button>
             </div>
          )}
        </div>
      </main>
    </div>
  );
}
