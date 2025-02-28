console.log('Found js file')

$(document).ready(function() {
    document.getElementById('highFiveBtn').addEventListener('click', function() {
        const recipient = document.querySelector('input[name="recipient"]:checked');
        
        if (recipient === null) {
            alert('Please select a person to give a high five.');
            return;
        }

        const data = {
            recipient: recipient.value, 
            message: 'High five a legend!',
            timestamp: new Date().toISOString()
        };

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/payload', true);
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                alert('High five sent successfully to: ' + recipient.value + '!');
                window.location.reload();
            } else if (xhr.readyState === 4) {
                alert('Failed to send high five.');
            }
        };

        xhr.send(JSON.stringify(data));
    });

});

console.log('loading dashboard')
document.addEventListener('DOMContentLoaded', function() {
    var iframe = document.getElementById('grafanaDashboard');
    var dashboardURL = "https://GrafanaURL";
    // If using API Token
    var apiToken = '';
    iframe.src = dashboardURL;
    iframe.onload = function() {
        iframe.contentWindow.postMessage({ message: 'set_token', token: apiToken }, '*');
    };
});