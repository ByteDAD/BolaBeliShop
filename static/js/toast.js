function showToast(title, message, type = 'normal', duration = 20000) {
    const toastComponent = document.getElementById('toast-component');
    const toastTitle = document.getElementById('toast-title');
    const toastMessage = document.getElementById('toast-message');
    const toastIcon = document.getElementById('toast-icon');
    
    if (!toastComponent) return;
    
    // Remove all type classes first
    toastComponent.querySelector('div').classList.remove(
        'from-purple-600', 'to-pink-600', 'border-purple-400',
        'from-green-600', 'to-emerald-600', 'border-green-400',
        'from-red-600', 'to-rose-600', 'border-red-400',
        'from-blue-600', 'to-indigo-600', 'border-blue-400'
    );
    
    // Set type styles and icon
    if (type === 'success') {
        toastComponent.querySelector('div').classList.add('from-green-600', 'to-emerald-600', 'border-green-400');
        toastIcon.textContent = '✅';
    } else if (type === 'error') {
        toastComponent.querySelector('div').classList.add('from-red-600', 'to-rose-600', 'border-red-400');
        toastIcon.textContent = '❌';
    } else if (type === 'info') {
        toastComponent.querySelector('div').classList.add('from-blue-600', 'to-indigo-600', 'border-blue-400');
        toastIcon.textContent = 'ℹ️';
    } else {
        toastComponent.querySelector('div').classList.add('from-purple-600', 'to-pink-600', 'border-purple-400');
        toastIcon.textContent = '🎉';
    }
    
    toastTitle.textContent = title;
    toastMessage.textContent = message;
    
    toastComponent.classList.remove('opacity-0', 'translate-y-16');
    toastComponent.classList.add('opacity-100', 'translate-y-0');
    
    setTimeout(() => {
        toastComponent.classList.remove('opacity-100', 'translate-y-0');
        toastComponent.classList.add('opacity-0', 'translate-y-16');
    }, duration);
}

function hideToast() {
    const toastComponent = document.getElementById('toast-component');
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-16');
}