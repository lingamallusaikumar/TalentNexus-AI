document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialize Real-Time WebSocket Connection
    const socket = io(window.location.origin, {
        transports: ['websocket', 'polling']
    });

    socket.on('connect', () => {
        const badge = document.getElementById('socket-status');
        if (badge) {
            badge.innerHTML = '<i class="fa-solid fa-circle"></i> Live WebSocket';
            badge.className = 'socket-badge connected';
        }
    });

    socket.on('disconnect', () => {
        const badge = document.getElementById('socket-status');
        if (badge) {
            badge.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> Disconnected';
            badge.className = 'socket-badge disconnected';
        }
    });

    // Real-time ranking update listener
    socket.on('ranking_updated', (data) => {
        console.log('Live Candidate Ranking Event received:', data);
        // Animate table refresh
        const tbody = document.getElementById('ranking-table-body');
        if (tbody) {
            tbody.style.opacity = '0.5';
            setTimeout(() => { tbody.style.opacity = '1.0'; }, 300);
        }
    });

    // 2. Initialize ATS Funnel Chart
    const ctx = document.getElementById('funnelChart');
    if (ctx) {
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Applied', 'AI Screened', 'Shortlisted', 'Interview', 'Offer', 'Hired'],
                datasets: [{
                    label: 'Candidates in Stage',
                    data: [1428, 1120, 310, 85, 24, 18],
                    backgroundColor: [
                        '#3b82f6',
                        '#8b5cf6',
                        '#10b981',
                        '#f59e0b',
                        '#06b6d4',
                        '#14b8a6'
                    ],
                    borderRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    },
                    y: {
                        grid: { color: '#374151' },
                        ticks: { color: '#9ca3af' }
                    }
                }
            }
        });
    }

    // 3. Global Natural Language Search Handler
    const searchInput = document.getElementById('global-search');
    if (searchInput) {
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const query = searchInput.value.trim();
                if (query) {
                    window.location.href = `/api/v1/search/candidates?q=${encodeURIComponent(query)}`;
                }
            }
        });
    }
});

function triggerResumeUploadModal() {
    alert("Select a PDF or DOCX resume to upload. Celery will parse it in the background and update the ranking live!");
}
