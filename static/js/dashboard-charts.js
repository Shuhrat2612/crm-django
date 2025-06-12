document.addEventListener('DOMContentLoaded', function () {
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: true, // Fix: keep natural aspect ratio
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    padding: 20,
                    usePointStyle: true
                }
            },
            tooltip: {
                backgroundColor: 'rgba(0,0,0,0.8)',
                padding: 12,
                titleFont: { size: 14 },
                bodyFont: { size: 13 }
            }
        }
    };

    // 🥧 Leads Pie Chart
    new Chart(document.getElementById('leadsChart'), {
        type: 'pie',
        data: {
            labels: leadsStatusLabels,
            datasets: [{
                data: leadsStatusData,
                backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
                borderWidth: 2
            }]
        },
        options: {
            ...commonOptions,
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Lead Distribution',
                    font: { size: 16 }
                }
            }
        }
    });

    // 📈 Deals Line Chart
    new Chart(document.getElementById('dealsChart'), {
        type: 'line',
        data: {
            labels: dealsMonths,
            datasets: [{
                label: 'Deal Value ($)',
                data: dealsValues,
                borderColor: '#36A2EB',
                backgroundColor: 'rgba(54, 162, 235, 0.1)',
                tension: 0.3,
                fill: true,
                borderWidth: 2,
                pointRadius: 4,
                pointHoverRadius: 6
            }]
        },
        options: {
            ...commonOptions,
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Deals Over Last 6 Months',
                    font: { size: 16 }
                },
                tooltip: {
                    ...commonOptions.plugins.tooltip,
                    callbacks: {
                        label: function (ctx) {
                            return `${ctx.dataset.label}: ${new Intl.NumberFormat('en-US', {
                                style: 'currency',
                                currency: 'USD'
                            }).format(ctx.parsed.y)}`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: value => '$' + value.toLocaleString()
                    }
                },
                x: { grid: { display: false } }
            }
        }
    });

    // 📊 Tasks Bar Chart
    new Chart(document.getElementById('tasksChart'), {
        type: 'bar',
        data: {
            labels: tasksPriorityLabels,
            datasets: [{
                label: 'Tasks',
                data: tasksPriorityData,
                backgroundColor: [
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(255, 159, 64, 0.7)',
                    'rgba(255, 99, 132, 0.7)'
                ],
                borderColor: [
                    'rgb(75, 192, 192)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 99, 132)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            ...commonOptions,
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Task Distribution by Priority',
                    font: { size: 16 }
                }
            },
            scales: {
                y: { beginAtZero: true },
                x: { grid: { display: false } }
            }
        }
    });

    // 🍩 Deals Status Doughnut Chart
    new Chart(document.getElementById('dealsStatusChart'), {
        type: 'doughnut',
        data: {
            labels: dealsStatusLabels,
            datasets: [{
                data: dealsStatusCounts,
                backgroundColor: [
                    'rgba(255,99,132,0.8)',
                    'rgba(54,162,235,0.8)',
                    'rgba(255,206,86,0.8)',
                    'rgba(75,192,192,0.8)'
                ],
                borderColor: [
                    'rgb(255,99,132)',
                    'rgb(54,162,235)',
                    'rgb(255,206,86)',
                    'rgb(75,192,192)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            ...commonOptions,
            cutout: '60%',
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Deal Status Distribution',
                    font: { size: 16 }
                }
            }
        }
    });
});
